# -*- coding: utf-8 -*-

import turtle # Modulo de Phyton para generar programas graficos


def run (edad, genero):
    if genero == 'M':
        if edad > 18:
            print('Hola, señor')
        else:
            print('Hola, niño')
    else:
        if edad > 18:
            print('Hola, señora')
        else:
            print('Hola, niña')



if __name__== '__main__':
    print('***VERIFICA SI ERES UNA MUJER O NIÑA, HOMBRE O NIÑO***')
    edad = int(input('Ingresa tu edad: '))
    genero = str(input('Ingresa tu sexo (M / F): '))
    run(edad, genero)