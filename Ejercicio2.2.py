from cmath import sqrt


a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))

print((-b+sqrt(b**2-4*a*c))/(2*a))
print((-b-sqrt(b**2-4*a*c))/(2*a))