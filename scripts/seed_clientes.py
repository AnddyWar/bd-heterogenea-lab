from faker import Faker
import pymysql
import pyodbc
import oracledb

fake = Faker("es_ES")

# ===== MariaDB =====
MARIADB = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "appmaria",
    "password": "MariaDB#2026!",
    "db": "db_mariadb",
}

# ===== SQL Server =====
SQLSERVER = {
    "server": "127.0.0.1,1433",
    "database": "HeterogeneaLab",
    "user": "appuser",
    "password": "DbLab#2026!Xy",
    "driver": "ODBC Driver 18 for SQL Server",
}

# ===== Oracle =====
ORACLE = {
    "host": "127.0.0.1",
    "port": 1522,
    "service": "FREEPDB1",
    "user": "APPORACLE",
    "password": "OracleApp123!",
}

def gen_cliente():
    return fake.name(), fake.email(), fake.msisdn()[:10]

def insert_mariadb(n):
    conn = pymysql.connect(
        host=MARIADB["host"],
        port=MARIADB["port"],
        user=MARIADB["user"],
        password=MARIADB["password"],
        database=MARIADB["db"]
    )
    cur = conn.cursor()
    for _ in range(n):
        cur.execute(
            "INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)",
            gen_cliente()
        )
    conn.commit()
    cur.close()
    conn.close()
    print(f"[OK] MariaDB: {n} registros")

def insert_sqlserver(n):
    conn_str = (
        f"DRIVER={{{SQLSERVER['driver']}}};"
        f"SERVER={SQLSERVER['server']};"
        f"DATABASE={SQLSERVER['database']};"
        f"UID={SQLSERVER['user']};PWD={SQLSERVER['password']};"
        f"Encrypt=yes;TrustServerCertificate=yes;"
    )
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    for _ in range(n):
        cur.execute(
            "INSERT INTO dbo.clientes (nombre, email, telefono) VALUES (?, ?, ?)",
            gen_cliente()
        )
    conn.commit()
    cur.close()
    conn.close()
    print(f"[OK] SQL Server: {n} registros")

def insert_oracle(n):
    dsn = oracledb.makedsn(
        ORACLE["host"],
        ORACLE["port"],
        service_name=ORACLE["service"]
    )
    conn = oracledb.connect(
        user=ORACLE["user"],
        password=ORACLE["password"],
        dsn=dsn
    )
    cur = conn.cursor()
    for _ in range(n):
        cur.execute(
            "INSERT INTO clientes (nombre, email, telefono) VALUES (:1, :2, :3)",
            gen_cliente()
        )
    conn.commit()
    cur.close()
    conn.close()
    print(f"[OK] Oracle: {n} registros")

if __name__ == "__main__":
    n = 10
    insert_mariadb(n)
    insert_sqlserver(n)
    insert_oracle(n)
