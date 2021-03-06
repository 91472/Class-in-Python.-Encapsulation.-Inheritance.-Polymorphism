from Ultra_lite_parental_class import Formulas_2D # импортируем класс Formulas_2D
from Ultra_lite_parental_class import Prime_numbers # импортируем класс Prime_numbers

# Применив принцип полиморфизма, создадим два других класса из класса Formulas_2D - расчет периметра и расчет площади фигуры
# Применив принцип наследования, создадим новый класс, который проверяет является ли какое-либо расположение цифр в
# заданном числе простым числом.

from math import pi  # импорт модуля pi для работы с числом pi

class Perimeter_2D(Formulas_2D): # создание класса Perimeter_2D (принцип полиморфизма)
    '''
    Домументрирование класса.
    Класс Perimeter_2D расчитывает периметр плоской геометрической фигуры, объект класса - это фигура.
    Для создания объекта класса Perimeter_2D и вычисления его периметра необходимо указать два аргумента:
    тип фигуры и длины ее сторон. Метод для расчета периметра: .perimeter()
    Тип фигуры (первый аргумент, type_figure) может быть один из: quadrat (квадрат), rectangle (прямоугольник),
    parallelogram (параллелограмм), rhombus (ромб), trapezoid (трапеция), triangle (треугольник), circle (окружность).
    Длины сторон (второй аргумент, *args): для квадрата - длина одной стороны, для прямоуголника - длины двух
    различных сторон, для параллелограмма - длины двух различных сторон, для ромба - длина одной стороны,
    для трапеции - длины всех четырех сторон, для треугольника - длины всех трех сторон, для окружности - радиус.
    '''
    def __init__(self, type_figure, *args): # встроенный метод класса, инициализация
        super().__init__(type_figure) # наследуем из класса Formulas_2D
        self.__side = args # аргумент, кортеж неименованных параметров с длинами сторон фигур
        if (self.figure, len(self.__side)) not in [('circle', 1), ('quadrat', 1), ('rectangle', 2), ('parallelogram', 2),  ('triangle', 3), ('trapezoid', 4), ('rhombus', 1)]:
            raise Exception ('Ошибка ввода аргументов') # если уловие True, то принудительно запустить исключение

    def __str__(self): # встроенные метод класса, что выводить на экран когда для вывода подается сам объект
        return f'Фигура {self.figure} с радиусом {self.__side}' if self.figure == 'circle' else f'Фигура {self.figure} со сторонами {self.__side}'

    def perimeter(self): #метод класса, вычисление периметра заданной фигуры
        dict_formul = {'quadrat': 4*self.__side[0], 'rectangle': 2*sum(self.__side), 'parallelogram': 2*sum(self.__side), 'rhombus': 4*self.__side[0], 'trapezoid': sum(self.__side), 'triangle': sum(self.__side), 'circle': 2*pi*self.__side[0]}
        return dict_formul[self.figure]


if __name__ == '__main__':
       try:
        # help(Perimeter_2D) # вызов справки по созданному классу с его документацией
        figure = Perimeter_2D('rectangle', 1,2) #определяем объект класса
        #figure.__side = (1,) # после применения инкапсуляции доступ к эти аргументам извне будет недоступен
        # figure.side = (1,) #если не применить инкапсуляцию к этим аргументам, то их можно изменить после определения объекта
        print('\n', figure, ', периметр = ', figure.perimeter(), '\n', type(figure), sep='') #и тогда результат будет неверным, относительно исхоных входных параметров при определении объекта
       except: # если поймано исключение, то выдать следующее сообщение:
           print('\nОшибка количества значений аргумента args и(или) несоответсвующий тип фигуры, см help(Perimeter_2D)')



class Area_2D(Formulas_2D): # создание класса Area_2D (принцип полиморфизма)
    '''
    Домументрирование класса.
    Класс Area_2D расчитывает площадь плоской геометрической фигуры, объект класса - это фигура.
    Для создания объекта класса Area_2D и вычисления его площади необходимо указать два аргумента:
    тип фигуры и длины ее сторон (+высота где это необходимо). Метод для расчета площади: .area()
    Тип фигуры (первый аргумент, type_figure) может быть один из: quadrat (квадрат), rectangle (прямоугольник),
    parallelogram (параллелограмм), rhombus (ромб), trapezoid (трапеция), triangle (треугольник), circle (окружность).
    Длины сторон (второй аргумент, **kwargs - именованные параметры): для квадрата - длина одной стороны (a),
    для прямоуголника - длины двух различных сторон (a и b),
    для параллелограмма - длина стороны (a) и длина высоты опущенной на эту сторону (h),
    для ромба - длина стороны (a) и длина высоты опущенной на эту сторону (h),
    для трапеции - длины оснований (а и b) и длина высоты (h),
    для треугольника - длина какой-либо стороны (a) и длина высоты опущенной на эту сторону (h),
    для окружности - радиус (r).
    '''
    def __init__(self, type_figure, **kwargs): # встроенный метод класса, инициализация
        super().__init__(type_figure) # наследуем из класса Formulas_2D
        self.__side = kwargs # аргумент, словарь именованных параметров с длинами сторон фигур (+высота если требуется)
        if (self.figure, self.__side.keys()) not in [('circle', {'r'}), ('quadrat', {'a'}), ('rectangle', {'a', 'b'}), ('parallelogram', {'a', 'h'}),  ('triangle', {'a', 'h'}), ('trapezoid', {'a', 'b', 'h'}), ('rhombus', {'a', 'h'})]:
            raise Exception ('Ошибка ввода аргументов') # если уловие True, то принудительно запустить исключение

    def __str__(self): # встроенный метод класса, что выводить на экран когда для вывода подается сам объект
        return f'Фигура {self.figure} с радиусом r {self.__side}' if self.figure == 'circle' else f'Фигура {self.figure} со сторонами {self.__side}' if self.figure == 'quadrat' or self.figure == 'rectangle' else f'Фигура {self.figure} с основаниями a,b и высотой h {self.__side}' if self.figure == 'trapezoid' else f'Фигура {self.figure} со стороной a и высотой к ней h {self.__side}'

    def area(self): #метод класса, вычисление площади заданной фигуры
        if self.figure == 'quadrat':
             area_fig = self.__side['a']**2
        elif self.figure == 'rectangle':
             area_fig = self.__side['a'] * self.__side['b']
        elif self.figure == 'parallelogram':
             area_fig = self.__side['a'] * self.__side['h']
        elif self.figure == 'rhombus':
             area_fig = self.__side['a'] * self.__side['h']
        elif self.figure == 'trapezoid':
             area_fig = (self.__side['a'] + self.__side['b'])*self.__side['h']/2
        elif self.figure == 'triangle':
             area_fig = self.__side['a'] * self.__side['h']
        elif self.figure == 'circle':
             area_fig = pi*self.__side['r']**2
        return area_fig


if __name__ == '__main__':
    # help(Area_2D) # вызов справки по созданному классу с его документацией
    try:
        figure1 = Area_2D('circle', r = 10) #определяем объект класса
        #figure.__side = (1,) # после применения инкапсуляции доступ к эти аргументам извне будет недоступен
        # figure.side = (1,) #если не применить инкапсуляцию к этим аргументам, то их можно изменить после определения объекта
        print('\n', figure1, ', площадь = ', figure1.area(), '\n', type(figure1), sep='') #и тогда результат будет неверным, относительно исхоных входных параметров при определении объекта
    except: # если поймано исключение, то выдать следующее сообщение:
        print('\nОшибка количества значений аргумента kwargs, неверное имя параметра или несоответсвующий тип фигуры, см help(Area_2D)')



class Prime_num_dif(Prime_numbers): # Prime_num_dif (принцип наследования)
    '''
    Домументрирование класса.
    Класс Prime_num_dif проверяет является ли если какое-либо расположение поданного на вход числа простым числом,
    если да, то метод класса .prime_num_check() возвращает True, иначе False. Объект класса - это число.
    Например: если проверяемое число равно 910, на выходе должно быть True, потому что 910 может быть организовано
    в 109 или 019, оба из которых являются простыми числами.
    Для создания объекта класса Prime_num_dif необходимо указать один аргумент: натуральное (целое положительное) число.
    Справка:
    Простое число — натуральное (целое положительное) число, имеющее ровно два различных натуральных делителя — единицу
    и самого себя. Другими словами, число x является простым, если оно больше 1 и при этом делится без остатка только на 1 и на x.
    '''

    def __init__(self, n):  # встроенный метод класса, инициализация
        super().__init__(n)  # наследуем из класса Prime_numbers

    def prime_num_check(self): #создаем метод класса для проверки наличия простого числа среди всевозможных чисел из комбинаций цифр исходного числа
        import itertools  # импорт библиотеки для работы с итераторами
        val = [i for i in str(self._Prime_numbers__number)] #аргумент был инкапсулирован в родительском классе
        perm_set = itertools.permutations(val) #объект итератора, содержащий все возможные перестановки val
        for i in perm_set: #проходи по всем элементам (кортежи цифр в формате str) итератора perm_set
            num_i = int(''.join(list(i))) #конкатенируем и переводим в int (на выходе получаем число)
            if num_i != self._Prime_numbers__number:  # исключаем исходное расположение числа num из анализа (двоякое толкование задания)
                try:
                    if Prime_numbers(num_i).prime_number() == True:
                        return True
                except:
                    continue # если поймали исключение, то продолжить цикл (для исключения вылета при расположении цифр таких, что число < 2, напр., 100: 10, 1)
        return False

if __name__ == '__main__':
      # help(Prime_num_dif) # вызов справки по созданному классу с его документацией
       try: # далее код программы, который может вызвать исключение:
          num = Prime_num_dif(910) # определяем объект класса
          print('\n', num, ' является простым? - ', num.prime_number(), sep='')  # пример использования метода из наследуемого класса
          print('Является ли какое-либо расположение данного числа простым числом? - ', num.prime_num_check())
          print(type(num))
       except: # если поймано исключение, то выдать следующее сообщение:
           print('\nОшибка, введеное число не натуральное или меньше 2, см help(Prime_num_dif)')
