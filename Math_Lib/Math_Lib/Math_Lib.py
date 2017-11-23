import math
import os
n=0
print ("MATHLIB (TM)2017")
print ("-"*50)

print ("Las funciones que puede realizar la libreria son las siguientes:")
print ("")

print ("FUNCIONES BASICAS:")
print ("")
print ("-(1) Suma ")
print ("-(2) Multiplicacion ")
print ("-(3) Division")
print ("-(4) Modulo")
print ("-(5) Potencia")
print ("-(6) Raiz")
print ("-(7) Verificacion de numeros primos")
print ("-(8) Rango de numeros primos")

print ("")

print ("FUNCIONES DE CONVERSION:")
print ("")
print ("-(9) Binario -> Hexadecimal")
print ("-(10) Binario -> Decimal")
print ("-(11) Decimal -> Hexadecimal")
print ("-(12) Decimal -> Binario")
print ("-(13) Hexadecimal -> Binario")
print ("-(14) Hexadecimal -> Decimal")
print ("-(15) Metros -> Yardas")
print ("-(16) Yardas -> Metros")

print ("")

print ("FUNCIONES ADICIONALES: ")
print ("")
print ("-(19) Indice de Masa Corporal [IMC]")
print ("")
print ("-"*50)

while (n<1 or n>19):
    n=int(input("Escriba el numero de la funcion a realizar: "))
    if (n<1 or n>19):
        print ("Ese numero es invalido. Por favor, ingrese una opcion permitida")
        print ("")
print ("-"*50)
os.system("cls")

def suma (a):
    return a
def multiplicacion (a):
    return a
def division (a,b):
   return float(a/b)
def modulo (a,b):
    return a%b 
def potencia (a,b):  #Falta que se pueda ingresar decimal
    return float(a**b)
def raiz (a,b):
    return math.sqrt(a,b)
def BaH (a):
    return a 
def DaH (a):
    return a
def DaB (a):
    return a 
def HaB (a):
    return a 
def HaD (a):
    return a
def BaD (a):
    return a 
def primos (a,b):
    return (a,b)
def primosrang (a,b):
    return (a,b)

'''SUMA 
En esta funcion se puede sumar dos variables que el usuario decida y obtener valores numericos nuevos.
'''

if (n==1) : #Suma
    print ("---SUMA---")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Suma---")
        print ("(1) Ingresar la cantidad de numeros a sumar")
        print ("(2) Ingresar las cifras individualmente y presionar 'Enter' para registrarlas")
        print ("(3) Una vez ingresados todos los datos su respuesta se imprimira presionando 'Enter'")
        print ("")
    a=int(input("Escriba cantidad de numeros a sumar: "))
    i=0
    r=0
    while(i<a):
        b=int(input("Numero: "))
        r=r+b
        i=i+1
    print ("El resultado de la suma es: " +str(suma(r)))
    print ("")

    """MULTIPLICACION
    En esta funcion se pueden multiplicar dos variables dadas por el usuario y asi obtener un nuevo valor numerico """
elif (n==2): #Multiplicacion
    print ("---MULTIPLICACION---")
    print ("")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Multiplicacion---")
        print ("(1) Ingresar la cantidad de numeros a multiplicar")
        print ("(2) Ingresar las cifras individualmente y presionar 'Enter' para registrarlas")
        print ("(3) Una vez ingresados todos los datos su respuesta se imprimira presionando 'Enter'")
        print ("")
    a=int(input("Escriba cantidad de numeros a multiplicar: "))
    i=0
    r=1
    while(i<a):
        b=int(input("Numero: "))
        r=r*b
        i=i+1
    print ("El resultado de la multiplicacion es: " +str(multiplicacion(r)))

    """DIVISION
   En esta funcion se va a poder dividir dos valores para asi poder obtener un resultado numerico nuevo
   Se utiliza la funcion de numero flotante para que de decimales"""
elif (n==3): #Division
    print ("---DIVISION---")
    print ("")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Division---")
        print ("* El programa solo imprime el resultado de la division")
        print ("(1) Ingresar el dividendo [El numero a dividir]")
        print ("(2) Ingresar el divisor [El numero que dividirá al dividendo]")
        print ("(3) Una vez ingresados todos los datos su respuesta se imprimira presionando 'Enter'")
        print ("")
    a=float(input("Escriba el dividendo: "))
    b=float(input("Escriba el divisor: "))
    print ("Su resultado es: " +str(division(a,b)))

elif (n==4): #Modulo
    print ("---MODULO---")
    print ("")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Modulo---")
        print ("* El programa solo imprime el residuo de la division")
        print ("(1) Ingresar el dividendo [El numero a dividir]")
        print ("(2) Ingresar el divisor [El numero que dividirá al dividendo]")
        print ("(3) Una vez ingresados todos los datos su respuesta se imprimira presionando 'Enter'")
        print ("")
    a=int(input("Escriba el dividendo : "))
    b=int(input("Escriba el divisor: "))
    print ("Su resultado es: " +str(modulo(a,b)))

    """POTENCIA
    La función calculara un numero elevado a cierta potencia.
    El usuario puede ingresar el numero base y el exponente que guste para hacer la funcion"""

elif (n==5): #Potencia
    print ("---POTENCIA---")
    print ("")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("") 
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Potencia---")
        print ("(1) Ingresar el numero base [El numero a potenciar]")
        print ("(2) Ingresar el exponente [El numero de veces que la base se multiplicara a si misma]")
        print ("(3) Una vez ingresados todos los datos su respuesta se imprimira presionando 'Enter'")
        print ("")
    a=float(input("Escriba el numero base: "))
    b=float(input("Escriba el exponente: "))
    print ("Su resultado es: " +str(potencia(a,b)))

    """RAIZ
    La función calculara la raiz de un numero cualquiera ingresado por el usuario.
    El usuario puede poner como parametro el indice y numero que gusten"""

elif (n==6): #Raiz
    print ("---RAIZ---")
    print ("")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Raiz---")
        print ("(1) Ingresar el radicando [El numero del cual se obtendrá la raiz]")
        print ("(2) Ingresar el indice [La raiz de la cual se obtendrá el resultado]")
        print ("(3) Una vez ingresados todos los datos su respuesta se imprimira presionando 'Enter'")
        print ("")
    a=2
    b=int(input("Escriba numero del radicando: "))
    a=int(input("Escriba a que numero de indice: "))
    if (a<=2):
        print ("Si el valor es menor que 2, el indice se toma al cuadrado por defecto")
        a=2
    print ("Su resultado es: " +str(math.sqrt(b)))

    """VERIFICACION DE NUMEROS PRIMOS
    La función demostrara si el numero que ha ingresado el usuario es numero primo o no.
    El programa verificara si el numero ingresado el multiplo de sus anteriores.
    Caso 1: En caso de que encuentre un multiplo, la función imprimira que no es primo
    Caso 2: Si el numero demuestra que no es multiplo de nunguno, la función imprimira que si es primo"""

elif (n==7): #Verificacion de numeros primos
    print ("---VERIFICACION DE NUMEROS PRIMOS---")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Numeros Primos por Verificacion---")
        print ("(1) Ingrese una cifra o numero entero cualquiera")
        print ("(2) Una vez ingresado el numero el programa evaluara el numero")
        print ("(3) Como resultado, el programa le dira si su numero es primo o no")
        print ("")
    a=0
    n=int(input("Ingrese numero para verificar si es primo: "))
    for i in range(1,n+1):
        if(n % i==0):
            a=a+1
    if(a!=2):
        print ("El numero "+(str(n)+" no es primo"))
        print ("")
    else:
        print ("El numero "+(str(n)+" si es primo"))
        print ("")

    """NUMERO PRIMO POR RANGO
    La función demostrara la lista de numeros primos, tomando como limite el numero ingresado por el usuario
    El programa verificara si cada numero dentro del rango es multiplo de sus anteriores.
    Caso 1: En caso de que encuentre un multiplo, el numero sera desechado por la funcion.
    Caso 2: Si el numero demuestra que no es multiplo de nunguno, sera imprimido en pantalla"""

elif (n==8): #Numero Primo por Rango
    a=0
    print ("---NUMEROS PRIMOS POR RANGO---")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Numeros Primos por Rango---")
        print ("(1) Ingresar una cifra para ponerlo como limite de la lista")
        print ("(2) Una vez ingresado el numero el programa evaluara los numeros primos dentro del rango")
        print ("(3) Como resultado, se generara una lista de numeros primos hasta el numero limite")
        print ("")

    lim=(input("Ingrese el limite de la lista de numeros primos: "))
    while (not lim.isdigit()):
        print ("Solo se aceptan numeros.")
        print ("")
        lim=(input("Ingrese el limite de la lista de numeros primos: "))
    lim=int(lim)
    print ("")
    print ("La lista de numeros primos hasta el numero "+str(lim)+" es:")
    print ("")
    for x in range (2,lim):
        prnt=False
        verf=0
        for i in range(1,x+1):
            if(x % i==0):
                verf=verf+1
        if (prnt==False and verf<3):
            print (str(x))
            prnt=True
    print ("")

elif (n==9): #Binario a Hexadecimal -- Falta completar
    print ("BINARIO -> HEXADECIMAL") 
    print ("") 

elif (n==10): #Binario a Decimal -- Falta completar
    print ("BINARIO -> DECIMAL")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Binario a Decimal---")
        print ("(1) Ingresar un numero en binario (Recuerde que estos solo llevan 0 y 1) y luego presionar 'Enter'")
        print ("(2) Al recibir su numero en forma decimal aparecera una pregunta")
        print ("(3) Presione '1' seguido de un 'Enter' para poder introducir otro numero o presione '0' seguido de un 'Enter' para terminar el programa")
        print ("")
    respuesta=1

    while(respuesta==1):
#Primero le pedimos al usuario su numero en binario
        binario=input("Introduzca un numero en binario: ")
        if(binario is not int):
            try:
#Convertimos la variable a entero para que pueda hacer las siguientes
#Comparaciones
                binario=int(binario)
                if(binario>2):
                    decimal=int(str(binario), 2)
                    print ("\nSu numero en decimal es: ")+str(decimal)
#La ultima opcion restante es que sean numeros que no sean 0 o 1
                else:
                    print ("Los numeros binarios solo llevan 0 y 1")
#Pero si no son numeros pasara lo siguiente
            except:
                print ("Las letras no se pueden convertir a decimal")
        respuesta=int(input("Va a introducir otro numero:<Si[1] No[0]>"))

    '''Esta funcion de DaH empieza pideiendole al usuario una cifra de entero,
    si el valor que se le pone no es un numero, este marcara un error.

    .isdigit() cumple la funcion de revisar si existen puros numeros y de este modo
    no acepte caracteres de letra.'''

elif (n==11): #Decimal a Hexadecimal
    print ("DECIMAL -> HEXADECIMAL")
    print ("")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Decimal -> Hexadecimal---")
        print ("(1) Ingresar una cifra para converir el numero a hexadecimal")
        print ("(2) Una vez ingresado el numero, se trasladara a decimal pero contando A, B, C, D, E y F como numeros también.")
        print ("(3) Como resultado, el programa le dira el numero que ingreso, pero usando los dieciseis numeros")
        print ("")

    a=(input("Ingrese una cifra en decimal: "))
    while (not a.isdigit()):
        print ("Solo se aceptan numeros.")
        a=(input("Ingrese una cifra en decimal: "))
    a=int(a)
    print ("Su resultado es: " + format(a, '02x'))
    print ("")
            

elif (n==12): #Decimal a Binario
    print ("---DECIMAL -> BINARIO---")
    print ("")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Decimal -> Binario---")
        print ("(1) Ingresar una cifra para converir el numero en binario")
        print ("(2) Una vez ingresado el numero, se trasladara a 1s y 0s")
        print ("(3) Como resultado, el programa le dira el numero que ingreso, pero en binario")
        print ("")
    respuesta=1

    while(respuesta==1):
        numero=input("Ingrese un numero: ")
        r=[]
    #Las letras y los decimales no se pueden pasar a binario
        if(numero is not int):
            try:
                numero = int(numero)
                if(numero==0):
                    print("0 no se puede convertir a binario")
                    input()
                elif(numero<0):
                    print("Los numeros menores a 0 no se pueden convertir a binario")
                    input()
        
                elif(numero>0):
                    while(numero>0):
                #Si el residuo de dividir el elemento[n] del numero entre 2 da 0
                #Agregamos 0 a la lista, de lo contratrio agregamos 1
                        if(numero%2==0):
                            r.append(0)
                        else:
                            r.append(1)
                        numero=numero/2
    #Al tener la lista la invertimos para tener el numero binario verdadero
                r.reverse()
                print (r)
            except:
                print("Las letras y los numeros decimales no se pueden convertir a binario")
#El numero tiene que ser mayor que 0 porque los numeros
#menores o iguales no se puede convertir a binario
        respuesta=int(input("¿Quieres ingresar otro numero? (Si[1]  No[0])"))

    print ("")

elif (n==13): #Hexadecimal a Binario
    print ("HEXADECIMAL -> BINARIO")

    """ En esta funcion se puede calcular un numero de hexadecimal a un numero decimal
    comenzando por iniciar un ciclo que niegue letras fuera del patron del hexadecima
    en este caso solo se permiten de la A a la F."""

elif (n==14): #Hexadecimal a Decimal
    print ("HEXADECIMAL -> DECIMAL")
    print ("")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("---Ayuda de Hexadecimal -> Decimal---")
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("(3) Como resultado, se mostrara el numero en sistema decimal")
        print ("(2) Presione 'Enter' para que el programa lo convierta a decimal")
        print ("(1) Escriba una cifra en sistema hexadecimal [Numeros y A,B,C,D,E,F son admitidos]")
        print ("")
    # Se hizo la modificacion para que la funcion hexdec funcionara

    print ("Que numero hexadecimal quiere convertir: ")
    hexdec=(input("Ingresa el numero en hexadecimal: ")) 
    while (hexdec >= 'g'):
        print ("No es una letra valida")
        hexdec=(input("Ingresa el numero en hexadecimal: "))

    dec = int(hexdec, 16) 
    print (hexdec + " en Decimal es: " + str(dec) +"\n")


    """METROS A YARDAS
    Con esta conversion podras facilmente convertir la medida de metro a yardas 
    Se solicita la cantidad de metros que el usuario quiere transformar luego 
    multiplica esa cantidad por metro(1)/yarda(.914) y muestra el resultado """
elif (n==15): #Metros a Yardas
    print ("METROS -> YARDAS")
    print ("")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("---Metros -> Yardas---")
    print ("")  
    if (hlp=="h" or hlp=="H"):
        print ("(3) Como resultado, se mostrara la conversi[on de metros(m) a yardas(yd)")
        print ("(2) Presione 'Enter' para que el programa lo convierta a Yardas")
        print ("(1) Escriba la cantidad de metros que desea convertir")
        print ("")
    metros=input("¿Cuantos metros quieres convertir a yardas? ")
    while (metros==""):
        print ("")
        print ("Porfavor escoja no deje ese espacio vacio ")
        metros=input("¿Cuantos metros quieres convertir a yardas? ")
    conversion= int(metros)*(int(1)/float(.914))
    print ("Sus metros en yardas son: "+ str(conversion)+"yd")

    """YARDAS A METROS
  Con esta funcion podras transformar Yardas(yd) a Metros(m) en base a una operacion 
  basada en regla de 3; multiplicando el numero de yardas por el el equivalente de 
  un metro pero en medias de yardas y dividiendoloe entre 1 para asi mostrar la conversion"""
elif (n==16): #yardas a metros
    yardas=input("Ingrese el numero de Yardas que quiere transformar a metros: ")
    while (yardas==""):
        print("Porfavor no deje ese espacio en blanco")
        yardas=input("Podria ingresar otra vez el numero?: ")
    Conversion= int(yardas)*float(.9144)/int(1)
    print ("Sus yardas transformadas a metros son: "+str(Conversion)+"m")


    """CALCULADORA DE IMC
    El proposito de esta funcion es el de calcular el indice de masa corporal del usuario.
    Los datos del usuario (Peso y Altura) se utilizan como variables para obtener el dato.
    El peso se divide entre la altura en metros al cuadrado."""

elif (n==19): #Calculadora de IMC
    print ("CALCULADORA DE INDICE DE MASA CORPORAL")
    print ("")
    hlp=str(input("Para iniciar la funcion presione 'Enter', pero si no sabe como funciona o necesita ayuda, presione 'h': "))
    print ("")     
    if (hlp=="h" or hlp=="H"):
        print ("---Ayuda de Calculadora de IMC---")
        print ("(1) Ingrese su peso en kg. [Kilogramo: 1kg = 1000gr.]")
        print ("(2) Ingrese su altura en mt. [Metro: 1mt. = 100cm.]")
        print ("(3) Como resultado, el programa le dira su indice de masa corporal.")
        print ("")

    pes=(input("Ingrese su peso en Kg (Kilogramos): "))
    while (not pes.isdigit()):
        print ("Solo se aceptan numeros.")
        print ("")
        pes=(input("Ingrese su peso en Kg (Kilogramos): "))
    pes=int(pes)

    alt=(input("Ingrese su altura en Cm (Centimetros): "))
    while (not alt.isdigit()):
        print ("Solo se aceptan numeros.")
        print ("")
        alt=(input("Ingrese un altura en Mt (Metros): "))
    alt=float(alt)
    imc=(pes/((alt/100)**2))
    print ("Su IMC es de: "+str(imc))
    print ("")
   
else:
    print ("No existe ese valor")

#Ejemplo de commit