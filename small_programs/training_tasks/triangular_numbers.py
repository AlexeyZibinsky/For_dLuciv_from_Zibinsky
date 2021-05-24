import tkinter
from tkinter.ttk import Combobox

class triangular_number_small:
    """
    По объектам этого класса можно итерироваться и получать треугольные числа.
    arg --- аргумент. Определяет, сколько треугольных чисел генерить.
    Данный класс реализован через непосредственно список треугольных чисел,
    поэтому для больших значений не годится, зато может сгенерить список.
    """ 
    def __init__(self, arg):
        self.content = [ i*(i + 1) // 2 for i in range(arg + 1) ]

    def __list__(self):
       return self.content

    def __len__(self):
        return len(self.content)

    def __getitem__(self, key):
        """
        Здесь я немножко ломаю нумерацию списков, но в этом и есть всё удовольствие:
        я пишу класс специально для того, чтобы было удобно :)
        """
        if key < 0:
            raise ValueError('sequence is a function from NATURAL numbers, and negative are not NATURAL')
        return self.content[key]

    def __setitem__(self, key, value):
        raise ValueError('If u wanna change me, just list me and do whatever u want')

    def __delitem__(self, key):
        raise ValueError('If u wanna change me, just list me and do whatever u want')

    def __reversed__(self):
        raise ValueError('If u wanna change me, just list me and do whatever u want')

    class _iterator_for_triangular_number_small:
        """ Подкласс --- реализация итератора """
        def __init__(self, arg):
            self.current_index = 0
            self.content = [ i*(i + 1) // 2 for i in range(arg) ]

        def __next__(self):
            if self.current_index >= len(self.content):
                raise StopIteration('As science develops, it constantly denies itself.')
            else:
                temp_index = self.current_index
                self.current_index += 1
                return self.content[temp_index]

    def __iter__(self):
        return triangular_number_small._iterator_for_triangular_number_small(len(self))



class triangular_number_large:
    """
    По объектам этого класса можно итерироваться и получать треугольные числа.
    arg --- аргумент. Определяет, сколько треугольных чисел "генерить".
    Данный класс реализован аккуратно, специально так, чтобы без проблем
    работать с длинными последовательностями треугольных чисел, не генерируя
    никаких списков.
    """
    def __init__(self, arg = 0):
        self.dlina = arg

    def __list__(self):
        raise ValueError('This method is not available in the class "triangular_number_large" ')

    def __len__(self):
        return self.dlina

    def __getitem__(self, key):
        """
        Этот метод не зависит от того, каким аргументом мы порождали объект класса: приятно
        знать, что можно получить любое треугольное число независимо от каких-то такм аргументов.
        """
        if key < 0:
            raise ValueError('sequence is a function from NATURAL numbers, and negative are not NATURAL')
        return key * (key + 1) // 2

    class _iterator_for_triangular_number_large:
        """ Подкласс --- реализация итератора """
        def __init__(self, arg):
            self.current_index = 0
            self.dlina = arg + 1
 
        def __next__(self):
            if self.current_index >= self.dlina:
                raise StopIteration('As science develops, it constantly denies itself.')
            else:
                temp_index = self.current_index
                self.current_index += 1
                return temp_index * (temp_index + 1) // 2

    def __iter__(self):
        return triangular_number_large._iterator_for_triangular_number_large(self.dlina)
    

# Какую-то скучную последовательность я выбрал...

window = tkinter.Tk()
window.title('Nils plays football')
window['bg'] = 'pink'
a = 800
b = a * 1.6180339887
window.geometry(str(int(b)) + 'x' + str(a))

lbl1 = tkinter.Label( window, text = 'Hello!', font = ( 'Arial Bold', 30 ), width = 20, bg = 'pink', fg = 'green4' )
lbl1.grid( column = 0 , row = 0 )

lbl2 = tkinter.Label( window, text = '1) Выберите, какой класс использовать:', font = ( 'Arial Bold', 30 ), bg = 'pink', fg = 'purple' )
lbl2.grid( column = 0 , row = 2 )
cmb1 = Combobox(window, width = 50)
cmb1 ['values'] = [ 'Мне не нужны большие числа.', 'Я беру от вычислительных мощностей максимум!' ]
cmb1.current(0)
cmb1.grid( column = 0 , row = 3 )

lbl3 = tkinter.Label( window, text = '2)До какого треугольного числа вы хотите вести работу?', font = ( 'Arial Bold', 30 ), bg = 'pink', fg = 'blue4' )
lbl3.grid( column = 0 , row = 5 )
txt1 = tkinter.Entry(window, width = 10, bg = 'grey65', fg = 'brown4')
txt1.grid( column = 0 , row = 6 )

def clicked():  
    window['bg'] = 'green1'
    lbl1.configure( bg = 'green1', fg = 'red4' )
    lbl2.configure( bg = 'green1' )
    lbl3.configure( bg = 'green1' )
    btn1.configure( text = 'а всё.' , state = 'disabled' , bg = 'white' )
    txt1.configure( state = 'disabled' )
    cmb1.configure( state = 'disabled' )
    inserted_value = int(txt1.get())
    if inserted_value == '':
        raise ValueError('Вы ничего не ввели :(')
    print('developer_info: ввод inserted_value ==', inserted_value)
    if cmb1.get() == 'Мне не нужны большие числа.':
        result = 0
        for i in triangular_number_small(inserted_value):
            result += i
        some_text1 = 'Сумма первых ' + str(inserted_value) + ' (не считая нуля) треугольных чисел равна ' + str(result)
        some_text2 = 'Мы пользовались классом triangular_number_small'
    else:
        result = 0
        for i in triangular_number_small(inserted_value):
            result += i
        some_text1 = 'Сумма первых ' + str(inserted_value) + ' (не считая нуля) треугольных чисел равна ' + str(result)
        some_text2 = 'Мы пользовались классом triangular_number_large'
    lbl4 = tkinter.Label( window, text = some_text1 + '\n' + some_text2, bg= 'green1', fg = 'purple1', font = ( 'Arial Bold' , 15 ) )
    lbl4.grid( column = 0 , row = 8 )
            
    print(b)
    
btn1 = tkinter.Button( window, text = 'тык' , command = clicked, bg = 'yellow1', fg = 'red4' )
btn1.grid( column = 0 , row = 7)

def update():
    btn1.configure( text = 'тык' , state = 'normal' , bg = 'yellow1' )
    window['bg'] = 'pink'
    lbl1.configure( bg = 'pink', fg = 'green4' )
    lbl2.configure( bg = 'pink' )
    lbl3.configure( bg = 'pink' )
    txt1.configure( state = 'normal' )
    cmb1.configure( state = 'normal' )

btn2 = tkinter.Button( window, text = 'update' , command = update, bg = 'black', fg = 'white' )
btn2.grid( column = 1 , row = 8 )

# Бессмысленно, но зато весело

if __name__ == '__main__':
    a = triangular_number_small(5)
    print(list(a))
    print(len(a))
    print(a[3])
    
    for i in a:
        print(i)
        
    print('')
    
    print('А ТЕПЕРЬ ТЕСТИРУЕМ ВТОРОЙ КЛАСС:')
    a = triangular_number_large(5)
    print(a)
    print(len(a))
    print(a[3])

    for i in a:
        print(i)

    print(a[6])
    print(a[60])

