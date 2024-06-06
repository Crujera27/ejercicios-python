import random

tiradas = [random.randint(1, 6) for _ in range(30)]
frec = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for tirada in tiradas:
    frec[tirada] += 1
max_frec = max(frec.values())
numero_mas_frecuente = [numero for numero, frecuencia in frec.items() if frecuencia == max_frec]

print("Resultados de las tiradas:")
for numero, frecuencia in frec.items():
    print(f"Número {numero}: {frecuencia} veces")
print(f"\nEl número que ha salido más veces es: {numero_mas_frecuente}, con {max_frec} veces.")
