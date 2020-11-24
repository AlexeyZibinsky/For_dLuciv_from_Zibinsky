import turtle

cabbage_rule = {'l': 'l',
                'r': 'r',
                'F': 'FlFrrFlF',
                'angle': 60}
cabbage_base_string = 'FlFlFlFlFlFl'

serpinskiy_rule = {'l': 'l',
                   'r': 'r',
                   'F': 'FlGrFrGlF',
                   'G': 'GG',
                   'angle': 120}
serpinskiy_base_string = 'FlGlG'

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
    turtle.setx(-200)
    turtle.sety(-350)
    turtle.pendown()
    for ch in base_string:
        if ch == 'l':
            turtle.left(rule['angle'])
        elif ch == 'r':
            turtle.right(rule['angle'])
        else: # F or G or some another symbol =)
            turtle.forward(step)
    turtle.update()
    turtle.done()

iterations = 7
cabbage_step = 300 / 3**iterations
serpinskiy_step = 300 / iterations**2

if __name__ == '__main__':
    #printing(iterations, cabbage_step, transformation, cabbage_base_string, **cabbage_rule)
    printing(iterations, serpinskiy_step, transformation, serpinskiy_base_string, **serpinskiy_rule)
