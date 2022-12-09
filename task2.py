#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#24
#2 2 2 3

user_input = int(input("Enter a number: "))
i = 2
list = []
while i <= user_input:
    if user_input % i == 0:
        list.append(i)
        user_input //= i
    else:
        i += 1
print(f"Prime factors are: {list}")