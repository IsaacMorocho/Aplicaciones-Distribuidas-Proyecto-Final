# Configuración Manual de Replicación MySQL (Master-Slave)

Este documento detalla los pasos exactos para configurar la replicación desde cero una vez que los contenedores `db-master` y `db-slave` están corriendo.

## Paso 1: Crear el usuario de replicación en el Master
Conéctate al contenedor `db-master` y ejecuta:

```sql
CREATE USER 'repl'@'%' IDENTIFIED BY 'repl_password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
FLUSH PRIVILEGES;
```

## Paso 2: Obtener el estado del Master
En el mismo contenedor `db-master`, verifica las coordenadas actuales del log binario:

```sql
SHOW BINARY LOG STATUS;
```

Toma nota de los valores devueltos en las columnas `File` y `Position`.
*(Ejemplo: File = `mysql-bin.000003`, Position = `859`)*

## Paso 3: Configurar el Slave
Conéctate al contenedor `db-slave` y ejecuta el siguiente comando, reemplazando `MASTER_LOG_FILE` y `MASTER_LOG_POS` con los valores que anotaste en el paso anterior. En MySQL 8, utilizamos la nueva sintaxis `CHANGE REPLICATION SOURCE TO`:

```sql
CHANGE REPLICATION SOURCE TO 
  SOURCE_HOST='db-master', 
  SOURCE_USER='repl', 
  SOURCE_PASSWORD='repl_password', 
  SOURCE_LOG_FILE='mysql-bin.000003', 
  SOURCE_LOG_POS=859,
  GET_SOURCE_PUBLIC_KEY=1;

START REPLICA;
```
*(Nota: `GET_SOURCE_PUBLIC_KEY=1` es necesario si no se usan certificados SSL, dado que MySQL 8 utiliza `caching_sha2_password` por defecto).*

## Paso 4: Verificar el estado de la replicación
En el mismo contenedor `db-slave`, revisa el estado para confirmar que los hilos de I/O y SQL están corriendo:

```sql
SHOW REPLICA STATUS\G
```

Busca las siguientes dos líneas en la salida, ambas deben decir **Yes**:
* `Replica_IO_Running: Yes`
* `Replica_SQL_Running: Yes`

## Prueba de Escritura/Lectura
Se ha insertado el siguiente registro en el Master para comprobar la replicación:
```sql
INSERT INTO app_db.students (username, password_hash) VALUES ('test_replica@epn.edu.ec', 'hash_falso');
```

Y se verificó que se replicó exitosamente en el Slave ejecutando:
```sql
SELECT * FROM app_db.students WHERE username='test_replica@epn.edu.ec';
```
