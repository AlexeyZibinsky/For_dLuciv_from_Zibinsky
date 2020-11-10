def find_all_rabin_karp(text: str, pattern: str):
    """ Алгоритм Рабина-Карпа. """
    result = []
    pattern_sum = sum(ord(s) for s in pattern)
    current_sum = sum(ord(text[i]) for i in range(len(pattern)))
    index = 0 #счётчик текущего индекса, с которого сравниваем паттерн
    while True: #проходимся по тексту
        if current_sum == pattern_sum:
            proverka = True
            #проверяем поэлементно
            for i in range(len(pattern)-1): # -1 для маленькой оптимизации
                if pattern[i] != text[i + index]:
                    proverka = False
            if proverka: #сохраняем индекс, если поэлементно сошлось
                result.append(index)
        if len(pattern) + index >= len(text):
            break
        current_sum -= ord(text[index])
        current_sum += ord(text[len(pattern) + index])
        index += 1
    return result

t = """Вместе шли они в сраженья через минные поля,
на узлах сопротивленья славу поровну деля.
Не страшили дождь и ночь их, и немало огневых
подавили они точек, не считая запятых.
Воевала дело зная та четверка храбрецов -
Иваненко, Иванбаев, Иванидзе, Иванов."""
p = "Иван"
print(find_all_rabin_karp(t, p))
                
            
