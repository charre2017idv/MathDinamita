import math
print ""

print "Bienvenido a tu Libreria Matematica"
print "-"*50

print "Si necesitas ayuda presiona la letra 'h'"
print "-"*50

print "Las funciones que puede realizar la libreria son las siguientes:"
print ""

print "- (1) Suma "
print "- (2) Multiplicacion "
print "- (3) Division"
print "- (4) Modulo"
print "- (5) Exponente"
print "- (6) Raiz"

print ""

print "Las funciones que puede traducir son las siguientes (Son conmutativas):"
print ""
print "- (7) Binario a Hexadecimal"
print "- (8) Decimal a Hexadecimal"
print "- (9) Decimal a Binario"

print ""

print "Las funciones que puede realizar en su persona son las siguientes: "
print ""
print "- (10) Indice de Masa Corporal (IMC)"
print "-"*50

n=int (raw_input("Que es lo que quieres realizar: "))
print "-"*50



def suma (a):
    return a
def multiplicacion (a):
    return a
def division (a,b):
   return float(a/b)
def modulo (a,b,):
    return a%b 
def exponente (a,b):  #Falta que se pueda ingresar decimal
    return float(a**b)
def raiz (a,b):
    return math.sqrt(a,b)


if (n==1) : #Suma
    print "Suma"
    print ""
    a=int(raw_input("Escriba cantidad de numeros a a sumar: "))
    i=0
    r=0
    while(i<a):
        b=int(raw_input("Numero: "))
        r=r+b
        i=i+1
#Hola
    print "El resultado de la suma es: " +str(suma(r))
elif (n==2): #Multiplicacion
    print "Multiplicacion"
    print ""
    a=int(raw_input("Escriba cantidad de numeros a a multiplicar: "))
    i=0
    r=1
    while(i<a):
        b=int(raw_input("Numero: "))
        r=r*b
        i=i+1
    print "El resultado de la multiplicacion es: " +str(multiplicacion(r))
elif (n==3): #Division
    print "Division"
    print ""
    a=float(raw_input("Escriba el dividendo: "))
    b=float(raw_input("Escriba el divisor: "))
    print "Su resultado es: " +str(division(a,b))
elif (n==4): #Modulo
    print "Modulo"
    print ""
    a=int(raw_input("Escriba el dividendo : "))
    b=int(raw_input("Escriba el divisor: "))
    print "Su resultado es: " +str(modulo(a,b))
elif (n==5): #Exponente
    print "Exponente"
    print ""
    a=float(raw_input("Escriba el primer numero: "))
    b=float(raw_input("Escriba el segundo numero: "))
    print "Su resultado es: " +str(exponente(a,b))
elif (n==6): #Raiz
    print "Raiz"
    print ""
    a=2
    b=int(raw_input("Escriba numero del radicando: "))
    a=int(raw_input("Escriba a que numero de indice: "))
    if (a<=2):
        print"Si el valor es menor que 2, el indice se toma al cuadrado por defecto"
        a=2
    print "Su resultado es: " +str(math.sqrt(b))

else:
    print "No existe ese valor"