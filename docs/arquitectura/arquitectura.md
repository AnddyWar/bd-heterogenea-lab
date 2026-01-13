# Arquitectura del sistema

El proyecto se ejecuta sobre una máquina virtual con Ubuntu Server 24.04.

La arquitectura integra:
- MariaDB instalado de forma nativa
- SQL Server 2022 en contenedor Docker
- Oracle Database 23ai Free en contenedor Docker

Oracle actúa como origen de datos, MariaDB como destino de sincronización,
y SQL Server como motor independiente.
