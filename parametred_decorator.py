def repeat(n):
"""
"декоратор с параметром"
"""
    def logging_decorator(genuine_function):
        def fake_function(arg):
            if n == 0:
                return arg
            if n == 1:
                value = genuine_function(arg)
                return value
            if n > 1:
                value = genuine_function(arg)
            for i in range(n-1):
                value = genuine_function(value)
            return value   
        return fake_function 
    return logging_decorator

@repeat(2)
def plus_1(x):
    return x + 1

@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3))  # должно выдать 5
print(mul_2(4))  # должно выдать 4
