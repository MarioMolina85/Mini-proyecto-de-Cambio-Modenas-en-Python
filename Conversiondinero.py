
import datetime#importacion de las librerias
from  os import  system
import time

class Conversiones:#creacion de la clase conversion parala cual permite calcular de una cantidad de dolares a siguientes modenas
    def __init__(self, codigo, cantidad_dolares, fecha):
        self.codigo=codigo
        self.cantidad_dolares=cantidad_dolares
        self.fecha=fecha
#creacion de los metodo getters y seters
    def gettcodigo(self):
        return self.codigo#
    def gettcantidad(self):
        return self.cantidad_dolares
    def getfecha(self):
        return self.fecha
#funciones la cual permite la conversion de modenas
    def conversion_euros(self):
        return self.gettcantidad()*0.84
    def conversion_bolivianos(self):
        return self.gettcantidad()*6.90
    def conversion_pesos(self):
        return self.gettcantidad() * 21.90
    def conversion_soles(self):
        return self.gettcantidad() * 3.53
    #tenemos una str que nos devuelve los datos imprimidos de la clase
    def __str__(self):
        return "Codigo '{}' Cantidad Dolares {} Euros {} Bolivianos {}  Pesos {} Soles {} Fecha Coversion {}".format(
            self.gettcodigo(), self.gettcantidad(), self.conversion_euros(), self.conversion_bolivianos(),
            self.conversion_pesos(), self.conversion_soles(), self.getfecha()
        )


def total_conversiones_inte(listdataconersiones):#funcion para obtener el total de cada conversion  de moneda
    listaconversiones=["euro","soles","bolivianos","pesos"]#declaramos una lista nombrando cada conversion
    dic_conversion={}#creamos un diccionario para almacenar los totales de cada modena
    totaleuros=totalsoles=totalbolivianos=totalpesos=0#inicializamos las variables de los totales de cada moneda

    for moneda in range(len(listaconversiones)):#recorremos un bucle para sacar los totales de cada moneda
        for c in listdataconersiones:
            if isinstance(c, Conversiones):
                if listaconversiones[moneda]=="euro":
                    totaleuros+=c.conversion_euros()
                if listaconversiones[moneda]=="soles":
                    totalsoles+=c.conversion_soles()
                if listaconversiones[moneda]=="bolivianos":
                    totalbolivianos+=c.conversion_bolivianos()
                if listaconversiones[moneda]=="pesos":
                    totalpesos+=c.conversion_pesos()
    #almacenamos los totales de modenas en un diccionario
    dic_conversion[listaconversiones[0]]=totaleuros
    dic_conversion[listaconversiones[1]] = totalsoles
    dic_conversion[listaconversiones[2]] = totalbolivianos
    dic_conversion[listaconversiones[3]] = totalpesos
    return dic_conversion#retornamos los totales

def obtener_totalcantidad(listdataconersiones):#funcion para obtener los totales de dolares de cada ingreso de conversiones
    total_dolares=0
    for c in listdataconersiones:
        if isinstance(c, Conversiones):
            total_dolares+=c.gettcantidad()
    return total_dolares

def list_conversiones(listdataconersiones):#funcion para imprimir  cada conversion
    for c in listdataconersiones:
        if isinstance(c, Conversiones):
            print(c)
            time.sleep(0.3)

def runmain():#creamos una funcion principal que nos permite ejecurtar cada funcion
    print('__________________________SISTEMA DE CONVERSION DE MODENAS INTERBNACIONALES______________')
    listahistrialconversion=[]#creamos una lista vacia donde se va almacenar cada conversiones de monedas
    banexit=True
    while banexit:#reccorremos un bucle
        try:
            numconersiones=int(input("Ingrese el numero de Converiones 0 Cancel:::"))#ingresamos el numero de conversiones que se va a realizar
            if numconersiones>0:
                for index in range(numconersiones):#creamos un bucle para el numero de conversiones
                    #obtenemos todos los datos para la conversion
                    fecha_obtencion=datetime.datetime.today()
                    print("-------------------Numero {} de Conversion--------------".format(index+1))
                    codigo="000"+str(index)
                    cantidad=int(input("Ingrese la Cantidad::::"))
                    objconversion=Conversiones(codigo, cantidad, fecha_obtencion)#creamos un objeto conversion para calcular caa conversion
                    if isinstance(objconversion, Conversiones):#verificamos si consta el objetos con la clase
                        print("___________Data Conversion_____________")
                        print(objconversion)#imprimimos los datos de la conversion de modenas
                        listahistrialconversion.append(objconversion)#almacenamos en la lista
                    else:
                        raise Exception['Error en la Agregacion de la Conversion ']
               #imprimimos los totales de las conservaciones
                print("__________________Totales de Conversiones_________")
                dic_coversiones=total_conversiones_inte(listahistrialconversion)#llamamos a una funcion donde nos devuelve los totales de cada modena
                total_cantidad=obtener_totalcantidad(listahistrialconversion)#call a una funcion donde me devuelve el total de antidad de dolares ingresados en cada conversion
                list_conversiones(listahistrialconversion)#call a la funcion para imprimir el historial de conversiones
                #impimimos en un bucle los totales de cada monedas
                print('__________________Moneda de Conversiones___________')
                for moneda, total in dic_coversiones.items():
                    print("Moneda '{}' total {}".format(moneda, round(total, 2)))
                print("\n Total Cantidad en Dolares {}".format(total_cantidad))

            elif numconersiones==0:
                banexit=False
            else:
                print("Opcion Incorrecta vuelva a ingresar")
        except ValueError as er:
            print("Error en Manipulacion de Datos ->{}".format(er))
runmain()#funcion para ejecutar la aplicacion