# Proyecto Base de Datos Heterogénea

## Descripción
Proyecto académico que integra múltiples motores de base de datos heterogéneos
en una sola infraestructura Ubuntu Server 24.04.

## Motores utilizados
- MariaDB (nativo)
- SQL Server 2022 (Docker)
- Oracle Database 23ai Free (Docker)

## Arquitectura
- Oracle sincroniza datos hacia MariaDB mediante Python
- SQL Server funciona como motor independiente
- Automatización mediante cron

## Tecnologías
- Docker
- Python 3.12
- MariaDB
- SQL Server
- Oracle Database
- DBeaver (cliente gráfico)

## Scripts
- `seed_clientes.py`: Inserta datos en los tres motores
- `sync_oracle_to_mariadb.py`: Sincronización incremental Oracle → MariaDB

## Evidencias
Las capturas de conexión y consultas se encuentran en la carpeta `/docs`.

## Autor
Anddy Andrade
benerice Tupiza
