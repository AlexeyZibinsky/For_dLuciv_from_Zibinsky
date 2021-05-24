import random

f = open('PRIMES.txt', encoding='utf-8')

rg = random.Random()

my_mega_spisok = list(map(int, f.read().split()))


def optimized_method(n1, some_spisok):
    """
    работает на числах меньших 1689243484682
    """

    def fermat_prime_or_pseudoprime(n, iter=5):
        for _ in range(iter):
            a = rg.randint(2, n-1)
            if pow(a, n-1, n) != 1:
                return False
        return True

    def MEGA_PROVERKA(n, some_spisok):
        """
        Сейчас 4:46 и нейминг функций уже не важен...
        Важно то, что я смог добыть мега-список! Это
        было весело. Пришлось облазить интернеты, а потом
        найденные данные переделать в подходящий вид.
        """
        sqrt_n = n**0.5  # Чтобы на каждой итерации не вычислять
        for ch in some_spisok:
            if ch > sqrt_n:
                return True
            if n % ch == 0:
                return False

    if fermat_prime_or_pseudoprime(n1):
        if MEGA_PROVERKA(n1, some_spisok):
            return True
    return False


if __name__ == '__main__':
    n = int(input('Какое число проверяем? '))
    print(optimized_method(n, my_mega_spisok))
