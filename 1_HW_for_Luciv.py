#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math # Импортируем модуль math чтобы была матеша
import numpy # Импортируем модуль numpy чтобы была матеша посерьёзнее
import matplotlib.pyplot as mpp # Импортируем matplotlib.pyplot чтобы были графики

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': # "Что-то вроде Begin End в Pascal" (c). 
    arguments = numpy.r_[0:6*math.pi:0.01] # Что-то вроде "списка" аргументов
    mpp.title("График") # Заголовок
    mpp.xlabel("x") # Обозначим ось абсцисс
    mpp.ylabel("y") # Обозначим ось ординат
    mpp.grid() # Путь будет сетка (так красивее)
    mpp.plot(
        arguments,
        [math.cos(x)+3 for x in arguments],
        color="grey"
    ) # Какой-то косинус зелёного цвета
    mpp.plot(
        arguments,
        [math.cos(x)+5 for x in arguments],
        color="grey" 
    ) # Ещё один косинус зелёного цвета
    mpp.plot(
        arguments,
        [math.cos(x) + 3*(math.cos(10*x)/3 + 8/6) for x in arguments],
        color="black"
    ) # Задаём прикольный косинус чёрного цвета между двумя зелёными косинусами
    mpp.show() # Наконец рисуем!
