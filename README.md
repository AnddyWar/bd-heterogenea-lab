# Proyecto Base de Datos Heterogénea

## 1. Descripción
Este proyecto implementa una base de datos heterogénea integrando
diferentes motores de bases de datos en una misma infraestructura,
permitiendo demostrar interoperabilidad, automatización y sincronización
de datos.

## 2. Arquitectura del sistema
El sistema está compuesto por:
- MariaDB instalado de forma nativa
- SQL Server 2022 desplegado en contenedor Docker
- Oracle Database 23ai Free desplegado en contenedor Docker
- Scripts en Python para inserción y sincronización de datos
- Automatización mediante cron

## 3. Tecnologías utilizadas
- Ubuntu Server 24.04
- Docker
- Python 3.12
- MariaDB
- SQL Server 2022
- Oracle Database 23ai Free
- DBeaver (cliente gráfico)

## 4. Estructura del proyecto
/scripts
seed_clientes.py
sync_oracle_to_mariadb.py
/docs
evidencias
README.md


## 5. Despliegue del sistema
1. Se instalan los motores de base de datos.
2. Se ejecuta el script `seed_clientes.py` para poblar las bases.
3. Se configura un cron job para ejecutar la sincronización periódica.
4. Se valida el funcionamiento mediante consultas SQL.

## 6. Uso del sistema
- Oracle actúa como origen de datos.
- MariaDB recibe los datos sincronizados.
- SQL Server funciona como motor independiente.
- La verificación se realiza mediante DBeaver y consultas SQL.

## 7. Evidencias
Las evidencias de conexión, consultas y ejecución del sistema se
encuentran en la carpeta `/docs`.

## 8. Conclusión
El proyecto demuestra el funcionamiento de una base de datos heterogénea,
cumpliendo con los requisitos académicos y técnicos establecidos.
