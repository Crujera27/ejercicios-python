numero = int(input("- Indica el numero: "))

if numero <= 1:
    primo = False
else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(f"--> El número {numero} es PRIMO")
else:
    print(f"--> El número {numero} NO es PRIMO")