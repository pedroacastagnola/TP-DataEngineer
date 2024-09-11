
Para correr el código:
1. Pararse en branch "main"
2. Asegurarse de haber creado la tabla en la base usando el archivo sql_creation.sql que se encuentra en la carpeta sql
3. Completar valores faltantes en .env
4. Correr comando "docker-compose up airflow-init"
5. Correr comando "docker-compose up"
6. Loguearse en airflow con user= airflow, pass=airflow
7. Triggerear el dag


-------------------------------------------------------

Aclaraciones pre-entrega 2:

1. Con respecto al requisito de PK, se agregó una validación en el código para que el proceso ETL no permita la inserción de duplicados ya que leí que Redshift lo permite aunque se defina la constraint. De todas formas, se agregó la definición de PK compuesta en el .sql.
2. El valor cantPaginas=11 está seteado por default en el archivo config2.json para que la API traiga las primeras 11 páginas. Este valor puede ser modificado por un número mayor para insertar más registros en la tabla.


