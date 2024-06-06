import random

nombres = []
for i in range(5):
    nombre = input("Introduce un nombre: ")
    nombres.append(nombre)

indice_elegido = random.randint(0, 4)
nombre_elegido = nombres[indice_elegido]

print("La persona elegida es:", nombre_elegido)

