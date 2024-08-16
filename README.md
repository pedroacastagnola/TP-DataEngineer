Aclaraciones:

1. Con respecto al requisito de PK, se agregó una validación en el código para que el proceso ETL no permita la inserción de duplicados ya que leí que Redshift lo permite aunque se defina la constraint. De todas formas, se agregó la definición de PK compuesta en el .sql.
2. El valor cantPaginas=10 está seteado por default en el archivo config.toml para que la API traiga las primeras 10 páginas. Este valor puede ser modificado por uno mayor para insertar más registros en la tabla.
