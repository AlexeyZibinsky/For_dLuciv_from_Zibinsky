def decorator(genuine_function): #Почему бы и нет
    def fake_function(*args):
        result = genuine_function(*args)
        print('gcd', args, '~', result)
        return result
    return fake_function

@decorator
def algoritm_Evklida(a, b):
    a, b = abs(a), abs(b)
    while True:
        if a > b:
            a -= b
        elif b > a:
            b -= a
        else:
            return a

if __name__ == '__main__':
    m = algoritm_Evklida(int(input('введите первое число: ')),
                         int(input('введите второе число: ')))
    # Для открытия мимо IDLE, мне ж этим ещё пользоваться:
    input('Закончить? ')
    
