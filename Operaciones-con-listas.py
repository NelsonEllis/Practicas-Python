>>> mi_lista = []
>>> type(mi_lista)
<class 'list'>
>>> mi_lista.append(1)
>>> mi_lista
[1]
>>> mi_lista_2 = [2, 3, 4]
>>> mi_lista_2
[2, 3, 4]
>>> mi_lista_3 = mi_lista + mi_lista_2
>>> mi_lista_3
[1, 2, 3, 4]
>>> mi_lista_4 = mi_lista_2 + mi_lista
>>> mi_lista_4
[2, 3, 4, 1]
>>> mi_lista_5 = ['a']
>>> mi_lista_6 = mi_lista_5 * 10
>>> mi_lista_6
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
>>> utiles = ['lapiz', 'calculadora', 'cuaderno']
>>> del utiles[0]
>>> utiles
['calculadora', 'cuaderno']
>>> del utiles[1]
>>> utiles
['calculadora']
>>> casa = 'casa'
>>> casa
'casa'
>>> type(casa)
<class 'str'>
>>> lista_casa = list(casa)
>>> lista_casa
['c', 'a', 's', 'a']
>>> str_casa = ''.join(lista_casa)
>>> str_casa
'casa'
