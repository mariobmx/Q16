import math

def myfactorial(x):
  cont = 1
  prod = 1

  while cont <= x:

    prod = prod*cont

    cont = cont + 1

  return prod

x =  float(input('Dame un entero: '))

print('El factorial de ', x, 'es ', myfactorial(x))



def soluciones(a,b,c):

  if a != 0:

    return (-b + math.sqrt(b**2 - 4*a*c))/(2*a), (-b - math.sqrt(b**2 - 4*a*c))/(2*a)




a =  float(input('Dame el coeficiente cuadratico: '))
b =  float(input('Dame el coeficiente lineal: '))
c =  float(input('Dame el coeficiente del termino indep: '))

print('Las soluciones son ', soluciones(a,b,c))