import math
import cmath
import numpy
import matplotlib.pyplot as mpp

ITERATIONS = 50

def factorial(a):
    """Лень копаться со встроенными факториалами, напишу свой """
    if a == 0:
        return 1
    return a*factorial(a-1)

def my_cos(x, factorial):
    """
    Вычисление косинуса при помощи частичного суммирования
    ряда Тейлора "в обратном порядке".
    """
    if type(x) != complex and x >= 10**8:
        print('Вы меня убить хотите?')
        return 'Не убивайте :(  введите лучше число поменьше, я всего лишь студенческая программа.'
    
    # Найдём аргумент из полуинтервала [0, 2*pi), эквивалентный введённому
    if type(x) != complex:
        x = abs(x)          # т.к. косинус - чётная функция
        while x > 2*math.pi:
            x -= 2*math.pi
        if x == 0:
            return 1.0
    
    # Найдём последний член, т.е. под номером ITERATIONS+1
    slagaemoe = (((-1)**ITERATIONS)*(x**(2*ITERATIONS))) / (factorial(2*ITERATIONS))
    partial_sum = 0 # Сюда будем запихивать сумму ряда
    if abs(x) >= 0.1: # Иначе аномалии близ нуля, т.к. в цикле я делю на аргумент.
        for n in range(ITERATIONS, 0, -1):
            slagaemoe /= x**2
            slagaemoe *= -1 * (2*n-1) * 2*n
            partial_sum += slagaemoe
        return partial_sum
    else:             # Близ нуля считаем ряд в "прямом порядке"
        x_pow = 1
        multiplier = 1
        partial_sum = 1
        for n in range(1, ITERATIONS):
            x_pow *= x**2  
            multiplier *= -1 / (2*n-1) / 2*n  
            partial_sum += x_pow * multiplier
        return partial_sum
        


while True:
    argument=float(input('введите значение аргумента: '))
    print('питоновский косинус:', math.cos(argument))
    print('мой косинус:       ', my_cos(argument, factorial))
    print('')
    if input('Введите bl, если хотите повторить. Иначе press Enter. ') != 'bl':
        break

print('бОльшая точность мне как-то не требуется.')
print('')
print('Теперь поработаем с комплексными аргументами.')
print('косинус комплексного аргумента получается точным лишь при малых Im и Real частях.')
print('')


while True:
    re_argument = float(input('введите действительную часть аргумента: '))
    im_argument = float(input('введите мнимую часть аргумента: '))
    argument = complex(re_argument, im_argument)
    print('наш аргумент:', argument)
    print('питоновский complex косинус:', cmath.cos(argument))
    print('мой comlex косинус:        ', my_cos(argument, factorial))
    print('')
    if input('Введите bl, если хотите повторить. Иначе press Enter. ') != 'bl':
        break

print('')
print('Рассмотрим аргумент:', cmath.acos(6))
print('Косинус из numpy: cos(-2.477888730288475j) =',numpy.cos(-2.477888730288475j))
print('Мой косинус: cos(-2.477888730288475j) =',my_cos(-2.477888730288475j, factorial))
print('Как мы видим, шести косинус достигает.')
print('')

#%matplotlib inline
#from IPython.display import set_matplotlib_formats
#set_matplotlib_formats('pdf', 'svg')

print('Взглянем на графики.')

arguments = numpy.r_[-6*math.pi: 6*math.pi: 0.01]
mpp.title('Косинусы')
mpp.grid()
mpp.xlabel('Аргумент')
mpp.ylabel('Значение')
mpp.plot(arguments, numpy.cos(arguments), color = "blue")
mpp.plot(arguments, [my_cos(x, factorial) for x in arguments], "r--")
mpp.show()
