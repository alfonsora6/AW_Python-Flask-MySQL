import pymysql
import sys
import getpass

def Conectar_BD(maquina,usuario,contraseña,nombrebd):
    try:
        db=pymysql.connect(host=maquina,user=usuario,password=contraseña,database=nombrebd)
        print("\nHas accedido a la base de datos.")
        return db       
    except:
        print("Error, no se puede conectar con la base de datos")
        sys.exit(1)

def Desconectar_BD(db):
    db.close()

def Mostrar_profesores_y_asignaturas(db):
    sql= "SELECT CONCAT(p.Nombre,' ',p.Apellido) AS 'Nombre y apellido', a.Nombre  FROM Profesor p, Asignatura a  WHERE p.DNI=a.DNI_Profesor"
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("\nLos profesores y asignaturas registrados son:\n")
        for nombre, asignatura in registros:
            print(nombre,"-",asignatura)
    except:
        print("Se ha producido un error en la consulta")
