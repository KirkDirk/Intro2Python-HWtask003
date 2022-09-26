# Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
# четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координаты x: '))
y = int(input('и координату y: '))
quarternumber = 1
if x<0 and y>0: quarternumber = 2
if x<0 and y<0: quarternumber = 3
if x>0 and y<0: quarternumber = 4
if x==0 and y==0: quarternumber = 0
if x==0 and y!=0: quarternumber = -1
if x!=0 and y==0: quarternumber = -2
if quarternumber>0: print('Точка с координатами (', x,',', y, ') находится в четверти ', quarternumber)
if quarternumber==-2: print('Точка лежит на оси абсцисс')
if quarternumber==-1: print('Точка лежит на оси ординат')
if quarternumber==0: print('Точка есть начало координат')