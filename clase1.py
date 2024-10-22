# -*- coding: utf-8 -*-
#%%INICIO
"""
Created on Fri Oct  4 21:08:46 2024

@author: DAM
"""
# import numpy as np
# from sys import exit
# import funciones as f

# print("Hola Mundo")

# nombre = input("¿Cual es tu nombre?: ")
# edad = int(input("¿Cual es tu edad?: "))
# if edad > 25: 
#     print("Eres",nombre,"y tienes",edad,"lo que significa que eres un poco mayor")
# else:
#     print("Eres",nombre,"y tienes",edad)      

#%% Chequeo de errores
# nombre = input("¿Cual es tu nombre?: ")
# if nombre.isdigit():
#     print("Error mete un string")
#     exit()

# try:
#     edad = int(input("Edad: "))
# except ValueError:
#     print("mete un numero")
#     exit()
'''
int,string,tuplas,float,bool.
'''
# int
# a = 10
# b = 10
# print(id(a),id(b))

# a = 5
# b = a
# # b = 10
# print(id(a),id(b))

# string

# tuplas
'''

'''
# tupla = (1,2,3)
# print(tupla)
# # Crea una nueva tupla, no la modifica
# tupla = tupla + (4,)
# print(tupla)
# #obtener valor deseado
# print(tupla[1])
# #primera funcion
# def calcSuma(a,b):
#     suma = a + b
#     resta = a - b
#     return suma,resta

# resultado = calcSuma(10, 5)
# print(resultado) #es una tupla

# #listas
# lista = [1,2,3,4]
# print(lista)
# print(lista[3])
# print(type(lista))
# #añade el valor establecido al final de la lista
# lista.append(5)
# print(lista)
# #listas anidadas
# lista_anidada = [1, 2, 3, [4, 5, [6, 7]]]

# print(lista_anidada[3])


# n_filas1, n_columnas1 = 4, 2
# n_filas2, n_columnas2 = 4, 2
# n_filas3, n_columnas3 = 4, 3
# matriz = []
# contador = 1
# for i in range(n_filas1):
#     filai1 = []
#     for j in range(n_columnas1):
#         filai1.append(i)
#         contador += 1
#     matriz.append(filai1)
        
# print(matriz)

# M = [[0 for _ in range(n_columnas1)]
#      for _ in range(n_filas1)]
# for i in range(n_filas1):
#     for j in range(n_columnas1):
#         M[i][j] = [[0 for _ in range(n_columnas2)]
#              for _ in range(n_filas2)]
#         for ii in range(n_filas2):
#             for jj in range(n_columnas2):
#                    M[i][j][ii][jj] = [[0 for _ in range(n_columnas3)]
#                    c = 1 
#                         for _ in range(n_filas3)]
#                    for iii in range(n_columnas3):
#                        M[i][j][ii][jj][iii][jjj] = c
#                        c += 1
# Matriz_numpy = np.arange(1,n_filas1 * n_columnas1 * n_filas2 * n_columnas2 * n_filas3 * n_columnas3 + 1)
# Matriz_numpy = np.reshape(Matriz_numpy, (n_filas1 , n_columnas1,n_filas2 , n_columnas2,n_filas3 , n_columnas3))

#Diccionarios
# diccionario = {"nombre": "Sebas","edad":19,"Estudios": ["ESO","SMR"]}
# # diccionario["gusto"] = "jugar a videojuegos"
# # print(diccionario["Estudios"][0])
# Claves = diccionario.keys()

# empleados = {
#     "empleado 1":{"nombre": "Sebastian","Nota": -2} ,
#     "empleado 2":{"nombre": "Javi","Nota": 1.5}}

# # print(empleados["empleado 1"]["Nota"])
# print(diccionario.get("Estudios")[1])

# conjunto1 = {1, 2, 3}
# conjunto2 = {3, 4, 5}
# inter = conjunto1.intersection(conjunto2)
# print(inter)
# union = conjunto1.union((conjunto2))
# print(union)
#condicionales
# x = 20
# if x > 10:
#     # print("x es mayor que 10")
#     print(f"{x} es mayor que 10") #imprime "20 es mayor a 10"
# elif x == 10:
#     print(f"{x} es igual a 10")
# else:
#     print(f"{x} es menor que 10")

# y = 5
# print(f"{y} es mayor que 5" if y > 5 else f"{y} es menor o igual que 5")

# condicionales y listas
# colores = ["rojo", "azul", "verde", "amarillo", "violeta", "rojo", "rosa", "blanco", "negro", "rojo", "gris"]
# color = "rojo"
# if color in colores:
#     print(f"El color {color} está {colores.count(color)} dentro de la lista {colores}")
# else: 
#     print(f"El color {color} no está dentro de la lista {colores}")

#switch-case -> match-case
# animal = "perro"
# match animal:
#     case "gato":
        
# condicionales con diccionarios
# diccionario = {"Sebas": 19,
#                 "Daniel": 21,
#                 "Javier": 19,
#                 "Manu": 26,
#                 "Ana": 9}
# for persona in diccionario:
#     if diccionario[persona] >= 18:
#         print(f"{persona} es mayor de edad")
#     else:
#         print(f"{persona} es menor de edad")
   
# all(y) y any(cualquiera)        
# x, y, z = 5, 10, 15
# if all ([x > 0, y > 0, z > 0 ]):
#     print("todos son mayores a 0")
# else:
#     print("no todos son mayores")

#Bucles
#for
# frutas = ["manzana", "cereza", "plátano"]
# for fruta in frutas:
#     print(f"fruta: {fruta}")
# diccionario = {"d": 1, "a": 3,"Sebas": 4}
# # for clave in diccionario:
# #     print(f"Clave: {clave}")
# # for valores in diccionario.values():
# #     print(f"Valores: {valores}")
    
# diccionario2 = {"Sebas": {"Coche": {"Marca": "Ferrari", "kms": 10000}},
#                 "Javier": {"Coche": {"Marca": "Mercedes", "kms": 10000}},
#                 "Manu": {"Coche": {"Marca": "Honda", "kms": 10000}}
#                 }
# for clave in diccionario2:
#     print(f"los {clave} son: {diccionario2[clave]['Coche']['kms']})

#Instrucciones especiales -> Break, continue
# n = [1, 2, 3, 4, 5]
# for numero in n:
#     if(numero == 4):
#         break
#     print(numero)
# for numero in n:
#     if(numero == 4):
#         continue
#     print(numero)

# lista = [x**2 for x in range(1,6)] 
# print(lista)  

# diccionario = {x: x**2 for x in range(1,6)}
# print(diccionario) 
 
# nombres = ["Sebas", "Javier", "Manu"]
# edades = [19, 19, 26]
# for n, e in zip(nombres, edades):
#     print(f"La edad de {n} es {e}")

# for i in range(11, 1, -2):
#     print(i)
    
# for i in range(1, 11, 4):
#     print(i)
    
# for clave, valor in diccionario.items():
#     print(f"La clave es {clave} y el valor es {valor}")
# for clave in diccionario:
#     print(f"la clave es {diccionario[clave]}")
   
#%% funciones

# def nombre(parametros):
    '''
    Descripcion...
    
    Entradas:
        
    Salidas:
    '''
    #Chequeo de errores
    
# def saludar(nombre = None):
#     if nombre is None:
#         nombre = 'amigo'
#         print(f"hola {nombre} no has introducido nada")
#     else:
#         print(f"Hola {nombre}")
    
# saludar()   

# a = 1
# b = 16
# print(f.suma(a, b))
    
#%% POO
# class Coche:
    
#     def __init__(self,marca, modelo, color, cv):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.cv = cv
    
#     def describir_coche(self):
       
#         print(f"Mi coche es un {self.marca} {self.modelo} de color {self.color} con {self.cv} caballos")
    
#     def caballos(self):
#         return f"El coche tiene {self.cv} caballos"
    
#     def cambiar_color(self,n_color):
#         self.color = n_color
    
# mi_coche = Coche("Honda", "Civic", "Azul", 140) 
# mi_coche.cambiar_color("verde")
# mi_coche.describir_coche()
# print(mi_coche.caballos())
 
#%% HERENCIA & POLIMORFISMO
#clase padre
# class Animal:
    
#     def __init__(self,nombre):
#         self.nombre = nombre
    
#     def hablar(self):
#         return f"{self.nombre} hace x sonido" 
    
# class Perro(Animal):
    
#     def hablar(self):
#         return f"{self.nombre} hace Guau"

    
# mi_perro = Animal("Indio")
# print(mi_perro.hablar()) 
# mi_perro2 = Perro("Indio")
# print(mi_perro2.hablar())

#Composicion
# class Tipo_Motor:
    
#     def __init__(self, CV):
#         self.CV = CV
        
# class Coche:
    
#     def __init__(self,marca, modelo, CV):
#         self.marca = marca
#         self.modelo = modelo
#         self.CV = Tipo_Motor(CV)
        
#     def detalles(self):
#         return f"Es un {self.marca} {self.modelo} con {self.CV.CV} CV"
    
# coche1 = Coche("Seat","Ibiza",120)
# print(coche1.detalles())

#Agregacion
# class Profesor:
    
#     def __init__(self, nombre):
#         self.nombre = nombre
        
# class Instituto:
    
#     def __init(self, nombre):
#         self.nombre = nombre
#         self.profesores = []
  
#     def añadir_Profesores(self, profesor):
#         self.profesores.append(profesor)
        
#     def mostrar(self):
#         for profesor in self.profesores:
#             print(profesor.nombre)

# Instituto = Instituto("Las Salinas")
# profe1 = Profesor("Dani") 
# profe2 = Profesor("Vicente") 
# profe3 = Profesor("Manu") 
# Instituto.añadir_Profesores(profe1)
# Instituto.añadir_Profesores(profe2)
# Instituto.añadir_Profesores(profe3)
# Instituto.mostrar()

#Clases Abstractas
# from abc import ABC, abstractmethod
# #padre
# class Animal(ABC):
    
#     @abstractmethod #metodo abstracto
#     def sonido(self):
#         pass #pasa al metodo de cada clase hija
    
#     def come(self):
#         return f"El animal está comiendo"
# #hijas
# class Perro(Animal):
    
#     def info(self, Nombre):
#         self.nombre = Nombre
#         return f"EL animal se llama {self.nombre}"
    
#     def sonido(self):
#         return f"Guau"
    
# class Gato(Animal):
    
#     def sonido(self):
#         return f"El gato hace miau"
    
# perro = Perro()
# print(perro.sonido())

# gato = Gato()
# print(gato.sonido())

#Acceder a datos
# import pandas as pd
# leer csv
# archivo = pd.read_csv("empleados.csv")
# print(archivo)
# #extrer info y acceder a columnas
# print("\n",archivo['nombre'])
# #acceder a filas
# primer_empleado = archivo.loc[0]
# print("\n",primer_empleado)
# #acceder a un valor concreto
# print("\nSalario: ",archivo.loc[2 , 'salario_mensual'])
# #crear un csv
# nueva_fila = {
#     'nombre' : 'Javi',
#     'edad' : 19,
#     'id_empleado' : 105,
#     'horas_trabajadas': 20,
#     'tarifa_hora': 20,
#     'salario_mensual': None
#     }
# #añadir la fila al csv
# new_df = pd.DataFrame([nueva_fila])
# archivo = pd.concat([archivo,new_df])
# print(archivo)
#cargar informacion


# from tkinter import Tk
# from tkinter.filedialog import askopenfilename

# Tk().withdraw() 

# file_path = askopenfilename(
#     title = "Selecciona un archivo .csv",
#     filetypes = [("CSV files", "*.csv"), ("All files","*.*")])

# if file_path:
#     #leer
#     df = pd.read_csv(file_path)
    
# else:
#     print("No has seleccionado ningun archivo")   
# from tkinter import Tk
# from tkinter.filedialog import askdirectory
# import os
# nombre_archivo = "ejemEmpleados.csv"
# data = {
#         'nombre': ["Sebas","Javier","Manu","Ivan"],
#         'edad': [19 ,19 ,26 ,20 ],
#         'salario': [1800 ,1650 , 1799, 4000]}

# df = pd.DataFrame(data)

# carpeta_select = askdirectory(title="Selecciona directorio")

# if carpeta_select:
#     file_path = os.path.join(carpeta_select,nombre_archivo)
#     df.to_csv(file_path, index = False)
# else:
#     print("No has introducido nada")


#%% BASE DE DATOS
# import mysql.connector
# from mysql.connector import Error
# #host, database, usuario, password,puerto-conexion

# #funcion para conectarse
# def connect_BD(host,database,user,password,port):
#     try:
#         connection = mysql.connector.connect(
#             host = host,
#             database = database,
#             user = user,
#             password = password,
#             port = port
#             )
#         if connection.is_connected():
#             print(f"La conexion ha sido exitosa")
#             return connection
#     except Error as e:
#         print(f"Error al conectarse: {e}")
#         return None

# #funcion para leer
# def read_BD(connection, tabla, columnas, limite_filas):
#     try:
#         cursor = connection.cursor()
#         #convertir lista de columnas en un string
#         columnas_string = ",".join(columnas)
#         query = f"SELECT {columnas_string} FROM {tabla} LIMIT {limite_filas};"
#         #Ejecutar peticion
#         cursor.execute(query)
#         resultados = cursor.fetchall()
#         #obtener
#         columnas_resultados = [i[0] for i in cursor.description]
#         #nos creamos el df
#         df = pd.DataFrame(resultados, columns = columnas_resultados)
#         return df
#     except Error as e:
#         print(f"Error al leer la BD: {e}")
#         return None
    
# # Ejecutar
# if __name__ == '__main__':
#     host = 'mysql-rfam-public.ebi.ac.uk'
#     database = 'Rfam'
#     user = 'rfamro'
#     password = ''
#     port = 4497
#     tabla = 'family'
#     columnas = ['rfam_acc', 'rfam_id','description']
#     limite_filas = 5
#     conexion = connect_BD(host, database, user, password, port)
#     if conexion :
#         df_BD = read_BD(conexion, tabla, columnas, limite_filas)
#         if df_BD is not None:
#             print(df_BD)
#         conexion.close()


#Consumo de apis
# import requests

# url = 'https://pokeapi.co/api/v2/pokemon?limit=150'

# respuesta = requests.get(url)

# lista_pkmn = respuesta.json()["results"]

# for pokemon in lista_pkmn:
#     print(pokemon["name"])



#Conexion a MongoDB
# import pymongo
# import pandas as pd
# #Creamos conexion
# try:
#     cliente = pymongo.MongoClient("mongodb+srv://albertomariann15:0dRsYdOPu2BIFWky@albertocluster0.4zgi4.mongodb.net/?retryWrites=true&w=majority&appName=AlbertoCluster0")
#     print("Conexion exitosa")
# except Exception as e:
#     print(f"Error en la conexion {e}")
#     exit()
# #Extraer info
# db = cliente["sample_mflix"]
# coleccion = db["movies"]    
# #Consulta
# try:
#     resultados = coleccion.find().limit(10)
#     lista_resultados = list(resultados)
#     #verificar si se han extraido los resultados
#     if not lista_resultados:
#         print("No se han encontrado datos")
#     else:
#         print(f"Se han encontrado {len(lista_resultados)} documentos")
#         #Lista --> df
#         df = pd.DataFrame(lista_resultados)
# except Exception as e:
#     print(f"Error al realizar la consulta {e}")
   

#Creacion de apis
# import requests
# import json

# url = f"https://re.jrc.ec.europa.eu/api/v5_2/PVcalc"

# params = {
#     "lat" : 38.6759,
#     "lon" : -4.159,
#     "peakpower" : 1,
#     "pvtechchoice" : "crystSi",
#     "loss" : 14,
#     "outputformat" : "json"}

# #Realizar consulta
# respuesta = requests.get(url,params = params)

# data = json.loads(respuesta.text)

# print(f"La energia diaria estimada: {data['outputs']['totals']['fixed']['E_d']} KWh ")

#Creacion de Apis
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/lista1",methods = ["GET"])
def obtener_lista1():
    datos = {
        "nombre" : "Sebas",
        "edad": 19,
        "Residencia": "Seseña"}
    return jsonify(datos)

@app.route("/api/lista2", methods = ["GET"])
def obtener_lista2():
    lista_datos = [
        {"nombre" : "Sebas","edad": 19,"Residencia": "Seseña"},
        {"nombre" : "Javi","edad": 19,"Residencia": "Seseña"},
        {"nombre" : "Manu","edad": 19,"Residencia": "Cuidad Real"},
        {"nombre" : "Tymur","edad": 20,"Residencia": "Seseña"}]            
    return jsonify(lista_datos)

if __name__ == '__main__':
    app.run(debug = True)
    
    
    
    
    
    