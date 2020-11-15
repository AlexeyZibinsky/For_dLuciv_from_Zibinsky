def prime_test(n):
    """
    Проверка числа на простоту. В случае не простого
    числа возвращает кортеж (False, divisor)
    """
    for i in range(2, round(n**0.5) + 1):
        if n % i ==0:
            return (False, i)
    return True

if __name__ == '__main__':
    m = int(input('проверяем на прстоту: '))
    print(prime_test(m))
    # Для открытия мимо IDLE, мне ж этим ещё пользоваться:
    input('Закончить? ')
