#Problema 8:
"""Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento."""

def factorial_numero(num):
    factorial = 1
    for i in range(num):
        factorial*=(i+1)
        return factorial
n = int(input('Ingrese el número: '))
resultado = factorial_numero(n)
print('El numero factorial es: ', resultado)

