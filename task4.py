#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл (или вывести в терминал) многочлен степени k.

#Пример:
#- k = 2  => 2*x² + 4*x + 5
#- k = 3  => 41*x^3 + 6*x² + 2*x + 98


import random

degree = int(input('Enter the degree of the polynomial k: '))
coefficients = [random.randint(-100, 100) for i in range(0, degree + 1)]

polynomial = ''
for i in range(0, degree + 1):
    if degree - i > 1 and coefficients[1] != 0:
        polynomial += f'{coefficients[i]} + x^{degree - i} + '
    elif degree - i == 1 and coefficients[i] != 0:
        polynomial += f'{coefficients[i]}+x +'
    elif coefficients[i] == 0:
        polynomial += ''
    else:
        polynomial += f'{coefficients[i]} = 0'
polynomial = polynomial.replace('+ -', '- ')
print(polynomial)
with open('file4.txt', 'w') as data:
    data.write(polynomial)