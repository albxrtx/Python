# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:14:24 2024

@author: DAM
"""

class Empresa:
    
    def __init__(self,nombre,empleados):
        self.nombre = nombre
        self.empleados = []
        
        
    def añadir_empleado(self):
        id_empleado = input("Introduce el ID del empleado: ")
        nombre = input("Introduce el nombre del empleado: ")
        tipo = input("Introduce el tipo de empleado (asalariado/temporal): ")
        if tipo == "asalariado":
            sueldo = input("Introduce el saldo del empleado: ")
            empleado = Empleado(id_empleado ,nombre ,tipo ,sueldo )
            self.empleados.append(empleado)
        elif tipo == "temporal":
            horas = int(input("Introduce las horas que trabaja el empleado: "))
            pago = int(input("Introduce cuánto le pagas a la hora: "))
            sueldo = horas * pago
            empleado = Empleado(id_empleado ,nombre ,tipo ,sueldo )
            self.empleados.append(empleado)
        else:
            print("No has introducido una opcion válida")
        
    def mostrar_datos_empleados(self):
        print("\n-----Empleados-----")
        for empleado in self.empleados:
            print(f"\nID:{empleado.id_empleado}\nNombre:{empleado.nombre}\nTipo:{empleado.tipo}\nSueldo:{empleado.sueldo}€")
    
    def calcular_gastos(self):
        gastos_totales = 0
        for empleado in self.empleados:
            gastos_totales += int(empleado.sueldo)
        print(f"\nGastos totales en salarios: {gastos_totales}€")
        
class Empleado:
    
    def __init__(self,id_empleado ,nombre ,tipo ,sueldo ):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.tipo = tipo
        self.sueldo = sueldo

nombre_empresa = input("Introduce el nombre de la empresa: ")
empleados = []
print(f"---- {nombre_empresa} ----")
empresa = Empresa(nombre_empresa, empleados)
continuar = True
while continuar:
    opcion = input("\nEscoge una opcion: \n1.Introducir Empleado\n2.Ver Empleados\n3.Calcular Gastos\n4.Salir")
    if opcion == "1":
        empresa.añadir_empleado()
    elif opcion == "2":
        empresa.mostrar_datos_empleados()
    elif opcion == "3":
        empresa.calcular_gastos()
    elif opcion == "4":
        continuar = False
    
