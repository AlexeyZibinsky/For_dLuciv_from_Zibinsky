def decorator(genuine_function): #Почему бы и нет
    def fake_function(*args):
        result = genuine_function(*args)
        print('gcd', args, '~', result)
        return result
    return fake_function

@decorator
def algoritm_Evklida(a, b):
    a, b = abs(a), abs(b)
    if a == b:
        return a
    while True:
        if a > b and (a - b) > 0:
            a -= b
        elif b > a and (b - a) > 0:
            b -=a
        elif a != b:
            raise ValueError('Что-то явно пошло не так o_0')
        else:
            return a

if __name__ == '__main__':
    m = algoritm_Evklida(int(input('введите первое число: ')),
                         int(input('введите второе число: ')))
    # Для открытия мимо IDLE, мне ж этим ещё пользоваться:
    input('Закончить? ')
    
