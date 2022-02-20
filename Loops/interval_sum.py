#Escriba un programa que pida al usuario dos n´umeros enteros, y luego entregue la suma de todos los
#n´umeros que est´an entre ellos. Por ejemplo, si los n´umeros son 1 y 7, debe entregar como resultado
#2 + 3 + 4 + 5 + 6 = 20.

a = int(input('Ingrese un numero entero mayor que cero: ' ))
b = int(input('Ingrese un número entero positic: '))
cont = 0
for i in range (a+1,b):
    cont = cont + i
print('La suma de los números entre a y b es: ', cont)

