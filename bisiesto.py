year = int(input("Introduce el año para verificar si es bisiesto: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"El año {year} es bisiesto.")
        else:
            print(f"El año {year} no es bisiesto.")
    else:
        print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")
