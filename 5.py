# Генератор списков
# a = [2,4,6,11,7,8]
# Что генерируем, из чего генерируем, условие генерации
# [x for x in a if x % 2 == 0]
# [2,4,6,8]
# [x*2 for x in a if x % 2 == 0]
# [4, 8, 12, 24]

# v1
#for n in range(1,200):
#    b = bin(n)[2:] # перевод в двоинчую степень
#    b += str(b.count('1') % 2) # поиск кол-ва единиц в двоичном числе и прибавка в существующему числу, перевод в строку
#    b += str(b.count('1') % 2) # another step
#    r = int(b, 2) # перевод в десятичную систему
#    if r > 77:
#        print(n)
#        break
# -------------------------------------------
# v2

#def f(n):
#    b = bin(n)[2:]
#    b += str(b.count('1') % 2)
#    b += str(b.count('1') % 2)
#    return int(b,2)

#print(min([n for n in range(1,200) if f(n)>77]))
# Same question with different answer
# -------------------------------------------
#def f(n):
#    b = bin(n)[2:]
#    if n % 2 == 0:
#        b = '10' + b
#    if n % 2 != 0: #else
#        b = '1' + b + '01'
#    return int(b,2)

#print(max([f(n) for n in range (1,13)]))
# f(n) = R: результат функции
# -------------------------------------------
# Троичная запись числа
#def c(x):
#   b = ''
#    while x > 0:
#        b = str(x % 3) + b # именно такой порядок, чтобы все в нужном порядке записалось
#        x //= 3
# -------------------------------------------
#def c(n):
#    b = ''
#    while n > 0:
#        b = str(n % 3) + b
#        n //= 3
#    return b

#def f(n):
#    b = c(n)
#    if n % 3 == 0:
#        b = '1' + b + '02'
#    else:
#        b += c(n % 3 * 4)
#    return int(b,3)

#print (max([n for n in range (1,10000) if f(n)<199]))
# Задача с троичной системой
# -------------------------------------------
#def sum_of_digits(num):
#    sum = 0
#    while num > 0:
#        sum += num % 10
#        num //= 10
#    return sum
# Сумма чисел в числе
#print(sum_of_digits(1557)) # 18
# -------------------------------------------
#num_str = "1234567890"
#old_digit = "3"
#new_digit = "*"
#new_num_str = num_str.replace(old_digit, new_digit)
#print(new_num_str)  # Output: 12*4567890
# Замена чисел в строке
# s = s[:-1] - удаление последнего разряда из числа
# x = x + x[:-2] - прибавка двух последних разрядов