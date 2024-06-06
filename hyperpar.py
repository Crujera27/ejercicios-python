num = input("Introduce un número: ")

if all(int(digito) % 2 == 0 for digito in num):
    print("SÍ")
else:
    print("NO")
