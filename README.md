Dudas y aclaraciones pre-entrega 3:

1. Además de "main", tengo una segunda branch "pre-entrega-3_v1" en la que trabajé para esta entrega. En ambas branches el código corre bien aunque mi entrega final se encuentra en "main".
    1a. En "pre-entrega-3_v1" quise que la función asociada a mi tarea 3 "subir_peli_nueva" reciba por parámetro lo que las otras dos tareas devolvían. Es decir, "leer_BD" en esta branch devuelve las películas ya subidas en la base, y "leer_API" todas las películas de la API en base a la cant de páginas seteadas en la config. "subir_peli_nueva" mira ambos conjuntos de datos y elimina los duplicados. Lo que quise hacer fue persistir lo que devolvían la task 1 y la task 2 para usarlas en la task 3, pero no logré hacerlo, entonces en la task 3 tuve que volver a llamar a las otras 2 funciones que ya habían corrido antes. ¿Puede ser que una solución sea utilizar un tema que vamos a ver la semana que viene que se llama XCOM?
    1b. En "main" modifiqué el código para que "leer_BD" y "leer_API" no devuelvan el resultado, sino que lo escriban en su archivo correspondiente dentro de la carpeta "data". De esta forma, "subir_peli_nueva" ahora lee la data de estos archivos para hacer su proceso de limpieza de duplicados antes de subirla a la base.

    ¿Qué approach sería mejor en este caso? ¿Que las tasks pasen su info a la task madre por parámetro o que las tasks hijas guarden su data en archivos?

2. Me tiraba un error de module not found en airflow cuando quería leer la línea "import toml" en una de las clases. Es por eso que cambié el toml por un json "config2.json" para leer esos datos. ¿Cómo podría hacer para que me tome correctamente el import toml?

Para correr el código:
a) Pararse en "main"
b) Correr comando "docker-compose up airflow-init"
c) Correr comando "docker-compose up"
d) Loguearse en airflow con user= airflow, pass=airflow
e) Triggerear el dag


-------------------------------------------------------

Aclaraciones pre-entrega 2:

1. Con respecto al requisito de PK, se agregó una validación en el código para que el proceso ETL no permita la inserción de duplicados ya que leí que Redshift lo permite aunque se defina la constraint. De todas formas, se agregó la definición de PK compuesta en el .sql.
2. El valor cantPaginas=10 está seteado por default en el archivo config.toml para que la API traiga las primeras 10 páginas. Este valor puede ser modificado por un número mayor para insertar más registros en la tabla.


