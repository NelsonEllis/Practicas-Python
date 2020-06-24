'''>>> while i < 10:
...     print(i)
...     i += 1
... 
0
1
2
3
4
5
6
7
8
9'''

import random

def run():
    rango_menor = int(input('Ingresa el rango menor del numero aleatorio: '))
    rango_mayor = int(input('Ingresa el rango mayor del numero aleatorio: '))
    number_found = False
    random_number = random.randint(rango_menor, rango_mayor)

    while not number_found:
        number = int(input('Intenta un numero: '))

        if number == random_number:
            print('Felicidades. Encontraste el numero')
            number_found = True
        elif number > random_number:
            print('El numero es mas pequeño')
        else:
            print('El numero es mas grande')

if __name__ == '__main__':
    run()