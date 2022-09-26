#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

#Пример:

#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

import numbers
numbers = [1, 2, 3, 5, 1, 5, 3, 10]

resnum = list(filter(lambda x: numbers.count(x)==1, numbers))

print(resnum)


