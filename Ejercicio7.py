#Problema 7:
"""Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no."""

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True
numero_a_verificar = int(input("Ingrese un número para verificar si es primo: "))
if es_primo(numero_a_verificar):
    print(f"{numero_a_verificar} es un número primo.")
else:
    print(f"{numero_a_verificar} no es un número primo.")
