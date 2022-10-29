from flask import Flask, render_template, abort, request, redirect, url_for
import pymysql
import os
import sys
import getpass

def Conectar_BD(maquina,usuario,contraseña,nombrebd):
    try:
        db=pymysql.connect(host=maquina,user=usuario,password=contraseña,database=nombrebd)
        return db
    except:
        db=None
        return db

def Desconectar_BD(db):
    db.close()

def Mostrar_profesores_y_asignaturas(db):
    sql= "SELECT CONCAT(p.Nombre,' ',p.Apellido) AS 'Nombre y apellido', a.Nombre  FROM Profesor p, Asignatura a  WHERE p.DNI=a.DNI_Profesor"
    cursor=db.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()
    return registros 