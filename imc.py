import cmath

peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / altura**2
if imc<=18.5:
    print('Bajo peso')
elif imc > 24.9 and imc > 18.5:
    print('Peso ideal')
elif imc > 25.0 and imc > 29.9:
    print('Sobrepeso')
elif imc > 25.0 and imc > 29.9:
    print('Obesidad')
