# -*- coding: utf-8 -*-

import turtle # Modulo de Phyton para generar programas graficos


def main ():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave)

    turtle.mainloop()

def make_square(dave):
    length = int(input('Tamaño de cuadrado: '))

    for i in range(4):
        make_line_and_turn(dave, length)

def make_line_and_turn(dave, length):
    dave.forward(length)# Tamaño de linea
    dave.left(90) #Grados de la linea


if __name__== '__main__':
    main()