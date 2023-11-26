#Problema 4:
"""Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
} Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
Nota:
El uso de listas con diccionarios le será de utilidad."""

lista_alumnos = []

while True:
    nombre = input("Ingrese el nombre del alumno (o escriba 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    notas = [float(input(f"Ingrese la calificación {i+1} del alumno {nombre}: ")) for i in range(3)]
    lista_alumnos.append({"Alumno": nombre, "Notas": notas})

print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")


    