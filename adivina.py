from random import randint
def main():
    rnum = randint(1, 100)
    intentos = 0
    
    print("ADIVINA, ADIVINANZA")
    
    while intentos < 8:
        intentos += 1
        print("- Indica un número (Intento {}):".format(intentos))
        try:
            numero_usuario = int(input())
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        if numero_usuario == rnum:
            print("- HAS ACERTADO en el Intento", intentos)
            return
        elif numero_usuario < rnum:
            print("- El número buscado es mayor.")
        else:
            print("- El número buscado es menor.")
    
    print("- ¡Lo siento! Has agotado tus intentos.")
    print("- El número oculto era:", rnum)

main()
