# Ejercicio 3.3
year = int(input("Introduce el año: "))

if year < 1900 or year > 2100:
    print("Esta fórmula solo es válida para años entre 1900 y 2100.")
else:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    pascua_marzo = 22 + d + e
    if d + e <= 9:
        print(f"El domingo de Pascua en {year} es el {pascua_marzo} de marzo.")
    else:
        print(f"El domingo de Pascua en {year} es el {d + e - 9} de abril.")
