import pymysql
import oracledb
from datetime import datetime

# ===== MariaDB =====
MARIADB = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "appmaria",
    "password": "MariaDB#2026!",
    "db": "db_mariadb",
}

# ===== Oracle =====
ORACLE = {
    "host": "127.0.0.1",
    "port": 1522,            # desde el host
    "service": "FREEPDB1",
    "user": "APPORACLE",
    "password": "OracleApp123!",
}

def main():
    # Conectar Oracle
    dsn = oracledb.makedsn(ORACLE["host"], ORACLE["port"], service_name=ORACLE["service"])
    oconn = oracledb.connect(user=ORACLE["user"], password=ORACLE["password"], dsn=dsn)
    ocur = oconn.cursor()

    # Conectar MariaDB
    mconn = pymysql.connect(
        host=MARIADB["host"], port=MARIADB["port"],
        user=MARIADB["user"], password=MARIADB["password"],
        database=MARIADB["db"], autocommit=False
    )
    mcur = mconn.cursor()

    # Traer IDs ya sincronizados
    mcur.execute("SELECT oracle_id FROM sync_oracle")
    synced = {row[0] for row in mcur.fetchall()}

    # Leer clientes desde Oracle
    ocur.execute("SELECT id_cliente, nombre, email, telefono FROM clientes")
    rows = ocur.fetchall()

    inserted = 0
    for oid, nombre, email, telefono in rows:
        oid_int = int(oid)
        if oid_int in synced:
            continue

        # Insertar en MariaDB
        mcur.execute(
            "INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)",
            (nombre, email, telefono)
        )
        # Marcar como sincronizado
        mcur.execute(
            "INSERT INTO sync_oracle (oracle_id) VALUES (%s)",
            (oid_int,)
        )
        inserted += 1

    mconn.commit()
    print(f"[{datetime.now().isoformat(timespec='seconds')}] Insertados desde Oracle -> MariaDB: {inserted}")

    # Cerrar
    ocur.close(); oconn.close()
    mcur.close(); mconn.close()

if __name__ == "__main__":
    main()
