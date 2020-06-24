>>> range(5)
range(0, 5)
>>> range(30)
range(0, 30)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(30))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> list(range(5, 40, 3))
[5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38]
>>> for i in list(range(30)):
...     if i % 3 !=0:
...         continue
...     else:
...         print(i**2)
... 
0
9
36
81
144
225
324
441
576
729
>>> 
for i in range(30):
    if i % 3 == 0:
        print(i**2)
    elif i == 22:
        break

0
9
36
81
144
225
324
441

for i in range(30):
    if i % 3 == 0:
        print(i)
    elif i == 22:
        break

    0
3
6
9
12
15
18
21

>>> r = 'ferrocarril'
>>> for letter in r:
...     print(letter)
... 
f
e
r
r
o
c
a
r
r
i
l

