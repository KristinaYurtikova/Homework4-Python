#Вычислить число Pi c заданной точностью d, не используя ф. round()
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

user_input = int(input('Enter the number rounding precision of Pi: '))
k = 1
pi = 0
for k in range(1, 1000000):
    pi = pi+4*((-1)**(k+1))/(2*k-1)
x = str(pi)
print(f'Number Pi = {pi} rounded to {user_input} characters after comma = {x[0:user_input+2:1]}')