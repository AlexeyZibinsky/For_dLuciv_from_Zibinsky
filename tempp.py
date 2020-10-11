""" Вычисляем квадрат по модулю """
m=int(input('vvedite modul: '))
for i in range(0, m):
    j=i*i
    while j >= m:
        j -= m
    if j == 1:
        print(i,'*', i, '=',j)
