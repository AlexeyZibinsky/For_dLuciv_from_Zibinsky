"""
Here I try to implement Gaussian integer
"""
from numbers import Number
import random


class Gaussian_integer:
    """Целое Гауссово Число"""

    def __init__(self, arg):
        """
        coefficients -- коэффицинты
        т.е. действительная и мнимые части
        """
        if type(arg) == complex:
            # Своеобразная проверка, целые ли?
            if arg.real == int(arg.real) / 1 and arg.imag == int(arg.imag) / 1:
                self.coefficients = [int(arg.real), int(arg.imag)]
            else:
                raise ValueError('Real or Imaginary part not int')
        elif type(arg) == int:
            self.coefficients = [arg, 0]
        elif type(arg) == tuple:
            if len(arg) == 1 and type(arg[0]) == int:
                self.coefficients = [arg[0], 0]
            if len(arg) == 2 and type(arg[0]) == int and type(arg[1]) == int:
                self.coefficients = [arg[0], arg[1]]
        else:
            raise ValueError('I condemn this mistake...')

    def __str__(self):
        if self.coefficients[1] >= 0:
            return str(self.coefficients[0]) + '+' + str(self.coefficients[1]) + 'i'
        else:
            return str(self.coefficients[0]) + str(self.coefficients[1]) + 'i'

    def __eq__(self, other):
        """
        Laureat Nobelevskoy premii po logike.
        Согласен, стрёмный код, но всё же хочется
        реализацию и для целого числа, и для
        комплексного, и для пары (кортежа).
        """
        # Тривиальное сравнение
        if isinstance(other, Gaussian_integer):
            return self.coefficients == other.coefficients
        # Сравнение с Целым
        elif type(other) == int:
            if self.coefficients[1] == 0:
                return self.coefficients[0] == other
            else:
                return False
        # Если пользователь - любитель кортежей (всё же Целое Гауссово - суть пара целых, так что фича необходима)
        elif type(other) == tuple:
            if len(other) == 1 and type(other[0]) == int and self.coefficients[1] == 0:
                return self.coefficients[0] == other[0]
            elif len(other) == 2 and type(other[0]) == int and type(other[1]) == int:
                if self.coefficients[0] == other[0]:
                    return self.coefficients[1] == other[1]
                else:
                    return False
            else:
                return False
        # Сравнение с комплексным
        elif type(other) == complex:
            if other.real == int(other.real) / 1 and other.imag == int(other.imag) / 1:
                if self.coefficients[0] == int(other.real):
                    return self.coefficients[1] == int(other.imag)
                else:
                    return False
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __pos__(self):
        return self

    def __neg__(self):
        return Gaussian_integer((-self.coefficients[0], -self.coefficients[1]))

    def __abs__(self):
        return (self.coefficients[0] ** 2 + self.coefficients[1] ** 2)**2

    def __round__(self):
        """ Почему бы и нет :) """
        return self

    def __add__(self, other):
        if not isinstance(other, Gaussian_integer):
            other = Gaussian_integer(other)
        return Gaussian_integer((self.coefficients[0] + other.coefficients[0], self.coefficients[1] + other.coefficients[1]))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Gaussian_integer):
            other = Gaussian_integer(other)
        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        if not isinstance(other, Gaussian_integer):
            temp = complex(self.coefficients[0], self.coefficients[1])
            try:
                result = Gaussian_integer(temp * other)
                return result
            except:
                return temp * other
        else:
            return Gaussian_integer(complex(self.coefficients[0], self.coefficients[1]) * complex(other.coefficients[0], other.coefficients[1]))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        """
        Определим возведение в степень натуральную, целую, вещественную и комплексную.
        """
        if type(other) == int:
            if other > 0:  # Натуральная степень
                result = 1
                for i in range(other):
                    result = result * self
                return result
            elif other == 0:  # Нулевая степень
                return 1
            else:  # Отрицательная степень
                # Выходим в поле комплексных
                return complex(self.coefficients[0], self.coefficients[1]) ** other
        elif type(other) == float:
            # Выходим в поле комплексных
            return complex(self.coefficients[0], self.coefficients[1]) ** other
        elif type(other) == complex:
            # Выходим в поле комплексных
            return complex(self.coefficients[0], self.coefficients[1]) ** other
        elif isinstance(other, Gaussian_integer):
            # Выходим в поле комплексных
            return complex(self.coefficients[0], self.coefficients[1]) ** complex(other.coefficients[0], other.coefficients[1])
        else:
            raise ValueError('I condemn this mistake...')

    # Перед работой с делимостью необходимо определить Евклидову Нормму

    def norm(self):
        return self.coefficients[0] ** 2 + self.coefficients[1] ** 2

    def __truediv__(self, other):
        """
        Просто деление комплексных чисел. Возвращает объект типа complex.
        Вдохновлялся делением целых чисел и получением числа типа float.
        """
        if type(other) == complex:
            return complex(self.coefficients[0], self.coefficients[1]) / other
        elif type(other) == int:
            return complex(self.coefficients[0], self.coefficients[1]) / complex(other, 0)
        elif type(other) == float:
            return complex(self.coefficients[0], self.coefficients[1]) / complex(other, 0)
        elif type(other) == tuple:
            if len(other) == 1 and isinstance(other[0], Number):
                return complex(self.coefficients[0], self.coefficients[1]) / complex(other[0], 0)
            elif len(other) == 2 and isinstance(other[0], Number) and isinstance(other[1], Number):
                return complex(self.coefficients[0], self.coefficients[1]) / complex(other[0], other[1])
            else:
                return ValueError('Do u like quaternions?')
        elif isinstance(other, Gaussian_integer):
            return complex(self.coefficients[0], self.coefficients[1]) / complex(other.coefficients[0], other.coefficients[1])
        else:
            return ValueError('Division is not available for this.')

    def __rtruediv__(self, other):
        if type(other) == complex:
            return other / complex(self.coefficients[0], self.coefficients[1])
        elif type(other) == int:
            return complex(other, 0) / complex(self.coefficients[0], self.coefficients[1])
        elif type(other) == float:
            return complex(other, 0) / complex(self.coefficients[0], self.coefficients[1])
        elif type(other) == tuple:
            if len(other) == 1 and isinstance(other[0], Number):
                return complex(other[0], 0) / complex(self.coefficients[0], self.coefficients[1])
            elif len(other) == 2 and isinstance(other[0], Number) and isinstance(other[1], Number):
                return complex(other[0], other[1]) / complex(self.coefficients[0], self.coefficients[1])
            else:
                return ValueError('Do u like quaternions?')
        elif isinstance(other, Gaussian_integer):
            return complex(other.coefficients[0], other.coefficients[1]) / complex(self.coefficients[0], self.coefficients[1])
        else:
            return ValueError('Division is not available for this.')

    # Так как представление числа в виде неполного частного и остатка при делении с остатком
    # в Целых Гауссовых не единственно, то __floordiv__ и __mod__ будут возвращать лишь
    # одно решение (зачастую кол-во решений доходит до четырёх).

    def __divmod__(self, other):
        if not isinstance(other, Gaussian_integer):
            try:
                other = Gaussian_integer(other)
            except:
                raise ValueError('Smth wrong with division')
        temp = complex(self.coefficients[0], self.coefficients[1]) / complex(other.coefficients[0], other.coefficients[1])
        quotient = Gaussian_integer((round(temp.real),round(temp.imag)))
        remainder = self.__sub__(other.__mul__(quotient))
        if remainder.norm() >= other.norm():
            raise ValueError('Данную функцию следует отправить в утиль')
        return (quotient, remainder)

    def __floordiv__(self, other):
        return divmod(self, other)[0]

    def __rfloordivmod__(self, other):
        if not isinstance(other, Gaussian_integer):
            try:
                other = Gaussian_integer(other)
            except:
                raise ValueError('Smth wrong with division')
        return divmod(other, self)[0]

    def __mod__(self, other):
        return divmod(self, other)[1]

    def __rmod__(self, other):
        if not isinstance(other, Gaussian_integer):
            try:
                other = Gaussian_integer(other)
            except:
                raise ValueError('Smth wrong with division')
        return divmod(other, self)[1]

    def associate(self):
        """
        Возвращает список из 4-х ассоциированных
        """
        return [self,
                self.__mul__(complex(0, 1)),
                self.__mul__(complex(-1, 0)),
                self.__mul__(complex(0, -1))]

    def is_prime(self):
        """
        Данный метод укажет нам, является ли данное
        целое Гауссово число неприводимым. Для проверки
        буду пользоваться критерием Гаусса
        """

        def primitive_prime_test(n):
            """
            Проверка целого числа на простоту (примитивная).
            """
            n = abs(n)
            for i in range(2, round(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        if self.coefficients[0] != 0 and self.coefficients[1] != 0:
            return primitive_prime_test(self.norm())
        elif self.coefficients[0] == 0:
            if primitive_prime_test(self.coefficients[1]):
                return abs(self.coefficients[1]) % 4 == 3
            else:
                return False
        else:  # self.coefficients[1] == 0
            if primitive_prime_test(self.coefficients[0]):
                return abs(self.coefficients[0]) % 4 == 3
            else:
                return False

    def gcd(self, other):
        """
        Использует алгоритм Евклида для Нахождения наибольшего общего делителя
        и его линейного представления
        """
        if not isinstance(other, Gaussian_integer):
            try:
                other = Gaussian_integer(other)
            except:
                raise ValueError('Smth wrong with division')
        def extended_algoritm_evklida(a, b):
            if a == 0 and b == 0:  # Тривиальный случай
                return (0, 0, 0)  # Одно из представлений :)
            if a == 0:
                return (1, 0, b)
            if b == 0:  # (b == 0, a != 0) => (a ~ gcd)
                return (1, 0, a)  # a == 1*a + 0*b
            x, y, greatest_common_divisor = extended_algoritm_evklida(b, a % b)
            return (y, x - (a // b) * y, greatest_common_divisor)
        return extended_algoritm_evklida(self, other)


if __name__ == '__main__':
    # a place to experiment!
    a = Gaussian_integer((random.randint(1, 1000), random.randint(1, 1000)))
    b = Gaussian_integer((random.randint(1, 10), random.randint(1, 10)))
    print( 'a =', a, '   ', 'b =', b)
    print( a.gcd(b) )
    print( Gaussian_integer.gcd(a,b)[2] )
    print( Gaussian_integer.gcd(a,b)[2], ' = (', Gaussian_integer.gcd(a,b)[0], ') * (', a, ') + (', Gaussian_integer.gcd(a,b)[1], ') * (', b, ')' ) # Алгоритм Евклида работает
    pass
