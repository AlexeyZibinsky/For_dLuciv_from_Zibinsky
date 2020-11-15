def decorator(genuine_function):
    """
    Данный декоратор создан для того, чтобы
    расписать расширенный алгоритм евклида
    по шагам.
    """
    def fake_function(a, b):
        result = genuine_function(a, b)
        k_1, k_2, gcd = result
        print('gcd(', a, ',', b, ') =', gcd)
        print(gcd, '= (', k_1, '*', a, ') + (', k_2, '*', b, ')')
        print('')
        return result
    return fake_function

    
@decorator  
def extended_algoritm_Evklida(a, b):
    """
    Возвращает кортеж (k_1, k_2, gcd(a,b)), т.ч.:
    gcd(a, b) == k_1 * a + k_2 * b
    """
    if a == 0 and b == 0: # Тривиальный случай
        return (0, 0, 0) # Одно из представлений :)
    if a == 0:
        return (1, 0 ,b)
    if b == 0: # (b == 0, a != 0) => (a ~ gcd)
        return (1, 0, a) # a == 1*a + 0*b
    x, y, gcd = extended_algoritm_Evklida(b, a%b)
    return (y, x - (a // b) * y, gcd)



if __name__ == '__main__':
    extended_algoritm_Evklida(int(input('введите первое число ')),
                              int(input('введите второе число ')))
    # Для открытия мимо IDLE, мне ж этим ещё пользоваться:
    input('Закончить? ')
    
