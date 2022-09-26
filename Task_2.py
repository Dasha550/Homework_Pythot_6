#Напишите программу вычисления арифметического выражения заданного строкой. Используйте 
#операции +,-,/,*. приоритет операций стандартный.



equation = '10/5+2-10*4'
ListOperation = ['-', '+', '*', '/']


def split_into_arfim(some_sting, list_of_operators):
    operator = []
    numbers = []
    positionBetween = ''
    for char in some_sting:
        if not char in list_of_operators:
            positionBetween += char
        else:
            operator.append(char)
            try:
                numbers.append(int(positionBetween))
            except:
                print('Strange symbol')
                exit()
            positionBetween = ''
    numbers.append(int(positionBetween))
    # создание 2-х списков(числа и знаки отдельные списки)

    while len(numbers) > 1:

        if '*' in operator:
            index = operator.index('*')
            positionBetween = performingAnOperation(numbers[index], numbers[index + 1], '*')
            numbers[index] = positionBetween
        elif '/' in operator:
            index = operator.index('/')
            positionBetween = performingAnOperation(numbers[index], numbers[index + 1], '/')
            numbers[index] = positionBetween
        elif '+' in operator:
            index = operator.index('+')
            positionBetween = performingAnOperation(numbers[index], numbers[index + 1], '+')
            numbers[index] = positionBetween
        elif '-' in operator:
            index = operator.index('-')
            positionBetween = performingAnOperation(numbers[index], numbers[index + 1], '-')
            numbers[index] = positionBetween

        del (numbers[index + 1])
        del (operator[index])
    return numbers[0]
#фунция выстраивает приоритеты выполнения операций
def performingAnOperation(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        if operator == '-':
            return num1 - num2
        if operator == '*':
            return num1 * num2
        if operator == '/':
            try:
                return num1 / num2
            except:
                print('Не делится на ноль')
                exit()
    except:
        print('Неизвестное значение')
        exit()
#Выполнение операций

print(equation)#выводит изначальное выражение
print(split_into_arfim(equation, ListOperation))#Результат вычеслений