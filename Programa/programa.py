from funciones import *
print("¡Bienvendido!\nPara acceder a la información de la base de datos, introduce los parámetros de conexión.\n")

maquina=input("Introduce la ip del servidor: ")
nombrebd=input("Introduce el nombre de la base de datos: ")
usuario=input("Introduce el usuario: ")
contraseña=getpass.getpass("Introduce contraseña: ")

db=Conectar_BD(maquina,usuario,contraseña,nombrebd)
Mostrar_profesores_y_asignaturas(db)
Desconectar_BD(db)

print("\nFin del programa")
