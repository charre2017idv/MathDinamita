import math
n=0
print "MATHLIB (TM)2017"
print "-"*50

print "Las funciones que puede realizar la libreria son las siguientes:"
print ""

print "-(1) Suma "
print "-(2) Multiplicacion "
print "-(3) Division"
print "-(4) Modulo"
print "-(5) Exponente"
print "-(6) Raiz"
print "-(7) Comprobacion de numeros primos"
print "-(8) Numeros primos por rango"

print ""

print "FUNCIONES DE CONVERSION:"
print ""
print "-(9) Binario -> Hexadecimal"
print "-(10) Binario -> Decimal"
print "-(11) Decimal -> Hexadecimal"
print "-(12) Decimal -> Binario"
print "-(13) Hexadecimal -> Binario"
print "-(14) Hexadecimal -> Decimal"

print ""

print "FUNCIONES ADICIONALES: "
print ""
print "-(15) Indice de Masa Corporal (IMC)"
print ""
print "En caso de necesitar ayuda, presiona 'h'"
print "-"*50

while (n<1 or n>15):
    n=int (raw_input("Escriba el numero de la funcion a realizar: "))
    if (n<1 or n>15):
        print "Ese numero es invalido. Por favor, ingrese una opcion permitida"
        print ""
print "-"*50

def suma (a):
    return a
def multiplicacion (a):
    return a
def division (a,b):
   return float(a/b)
def modulo (a,b):
    return a%b 
def exponente (a,b):  #Falta que se pueda ingresar decimal
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


if (n==1) : #Suma
    print "SUMA"
    print ""
    a=int(raw_input("Escriba cantidad de numeros a sumar: "))
    i=0
    r=0
    while(i<a):
        b=int(raw_input("Numero: "))
        r=r+b
        i=i+1
    print "El resultado de la suma es: " +str(suma(r))

elif (n==2): #Multiplicacion
    print "MULTIPLICACION"
    print ""
    a=int(raw_input("Escriba cantidad de numeros a multiplicar: "))
    i=0
    r=1
    while(i<a):
        b=int(raw_input("Numero: "))
        r=r*b
        i=i+1
    print "El resultado de la multiplicacion es: " +str(multiplicacion(r))

elif (n==3): #Division
    print "DIVISION"
    print ""
    a=float(raw_input("Escriba el dividendo: "))
    b=float(raw_input("Escriba el divisor: "))
    print "Su resultado es: " +str(division(a,b))

elif (n==4): #Modulo
    print "MODULO"
    print ""
    a=int(raw_input("Escriba el dividendo : "))
    b=int(raw_input("Escriba el divisor: "))
    print "Su resultado es: " +str(modulo(a,b))

elif (n==5): #Exponente
    print "EXPONENTE"
    print ""
    a=float(raw_input("Escriba el primer numero: "))
    b=float(raw_input("Escriba el segundo numero: "))
    print "Su resultado es: " +str(exponente(a,b))

elif (n==6): #Raiz
    print "RAIZ"
    print ""
    a=2
    b=int(raw_input("Escriba numero del radicando: "))
    a=int(raw_input("Escriba a que numero de indice: "))
    if (a<=2):
        print"Si el valor es menor que 2, el indice se toma al cuadrado por defecto"
        a=2
    print "Su resultado es: " +str(math.sqrt(b))

elif (n==7): #Binario a Hexadecimal -- Falta completar
    print "BINARIO -> HEXADECIMAL" 
    print "" 

elif (n==8): #Binario a Decimal -- Falta completar
    print "DECIMAL -> HEXADECIMAL"
    print ""

elif (n==9): #Decimal a Hexadecimal -- Falta completar
    print "DECIMAL -> HEXADECIMAL"
    print ""
    print ("Decimal a Hexadecimal")
        print ("")
        print ("Que numero decimal quiere convertir: ")
        a=int(input())
        print ("Su resultado es: " + format(a, '02x'))

elif (n==10): #Decimal a Binario
    print "DECIMAL -> BINARIO"
    print ""
    numero=int(raw_input("Ingrese un numero: "))
    a=[]
    while(numero>0):
        if(numero%2==0):
            a.append(0)
        else:
            a.append(1)
        numero=numero/2
    a.reverse()
    print "Su resultado es: " +  str(DaB(a))

elif (n==13): #Numero Primo por Ingreso
    print "NUMEROS PRIMOS POR INGRESO"
    a=0
    n=int(raw_input("Ingrese numero para verificar si es primo: "))
    for i in range(1,n+1):
        if(n % i==0):
            a=a+1
    if(a!=2):
        print "El numero "+(str(n)+" no es primo")
        print ""
    else:
        print "El numero "+(str(n)+" si es primo")
        print ""

elif (n==15): #Calculadora de IMC
    print "CALCULADORA DE INDICE DE MASA CORPORAL"
    pes=int(raw_input("Ingrese su peso en Kg (Kilogramos): "))
    alt=float(raw_input("Ingrese un altura en Mt (Metros): "))
    imc=(pes/(alt**2))
    print "Su IMC es de: "+str(imc)
    print ""

elif (n=="h" or n=="H"): #Menu de Ayuda
    print "MENU DE AYUDA"
    print ""

else:
    print "No existe ese valor"
