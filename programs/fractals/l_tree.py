import turtle
import random

"""
Сразу стоит оговориться, что эта программа не является полностью плодом моего воображения.
Летом я видел какой-то видеоролик, в котором объяснялась вообще вся эта приколюха со строкой
и словарём, и там в качестве примера как раз и были подобные деревья. Я лишь перевоспроизвёл
их в вольной интерпретации и с добавлением рандома.
"""

tree_rule = { '0': '1[-0]+0',
              '1': '21',
              '2': '2',
              '[': '[',
              ']': ']',
              '-': '-',
              '+': '+',
              'angle': 25}

tree_base_string = '0'

def transformation(base_string, **rule):
    temp = ''
    for symbol in base_string:
        temp += rule[symbol]
    return temp

def printing(ITERATIONS, step, TRANSFORMATION, base_string, **rule):
    for i in range(ITERATIONS):
            base_string = TRANSFORMATION(base_string, **rule)
    turtle.tracer(0, 0)
    turtle.penup()
    turtle.setx(0)
    turtle.sety(-350)
    turtle.setheading(90)
    turtle.pensize(12)
    turtle.pendown()
    stack = []
    for ch in base_string:
        if ch == '1':
            turtle.forward(step)
        elif ch == '2': # эта двойка - вообще колдовство чтобы было красиво
            if random.randint(1,3) == 1: # поэтому рандом объяснить никак, так просто красивее :)
                turtle.forward(step)
        elif ch == '0': # 0 рисует последние отрезки, т.е. "листики"
            stack.append(turtle.pensize())
            turtle.pensize(turtle.pensize() + 2) # "листики" должны быть потолще
            # Установим случайным образом какой-нибудь зелёный на листики
            if random.randint(1, 9) <= 3:
                turtle.pencolor(0, 1, 0)
            elif 4 <= random.randint(1, 9) <= 6:
                turtle.pencolor(0, 0.7, 0)
            else:
                turtle.pencolor(0, 0.5, 0)
            turtle.forward(step)
            turtle.pensize(stack.pop())
            turtle.pencolor(0,0,0)
        elif ch == '-':
            turtle.left(rule['angle'] - random.randint(0, 10))
        elif ch == '+':
            turtle.right(rule['angle'] - random.randint(0, 10))
        elif ch == '[':
            stack.append(turtle.ycor())
            stack.append(turtle.xcor())
            stack.append(turtle.heading())
            turtle.pensize(0.825 * turtle.pensize()) # "веточки" становятся всё тоньше
            stack.append(turtle.pensize())     
        elif ch == ']':
            turtle.penup()
            turtle.pensize(stack.pop())
            turtle.setheading(stack.pop())
            turtle.setx(stack.pop())
            turtle.sety(stack.pop())
            turtle.pendown()
    turtle.update()
    turtle.done()

iterations = 10
tree_step = 15

if __name__ == '__main__':
    printing(iterations, tree_step, transformation, tree_base_string, **tree_rule)           
