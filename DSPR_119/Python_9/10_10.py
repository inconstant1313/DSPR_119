'''Напишите функцию get_loto(num), генерирующую трёхмерный массив случайных целых чисел от 1 до 100 (включительно). 
Это поля для игры в лото.
Трёхмерный массив должен состоять из таблиц чисел формы 5х5, то есть итоговая форма — (num, 5, 5).
Функция возвращает полученный массив.'''

import numpy as np

def get_loto(num):
    result = np.random.randint(1,101,size=(num,5,5))
    return result
    
    
print(get_loto(3))