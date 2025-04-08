import mysql.connector

# Conectar a la base de datos
mydb = mysql.connector.connect(
  host="db",
  user="root",
  password="1234",
  database="recauderia_db"
)

# Crear un cursor
mycursor = mydb.cursor()

# SQL para insertar un registro
sql = "INSERT INTO frutas (nombre, descripcion) VALUES (%s, %s)"
val = ("Rosa", "Rojo")

# Ejecutar el comando SQL
mycursor.execute(sql, val)

# Confirmar los cambios en la base de datos
mydb.commit()

print(mycursor.rowcount, "registro insertado.")
