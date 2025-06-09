#def f(x):
#    divs = set() # - set() является множеством. ЭТО СПИСОК БЕЗ ПОВТОРЕНИЙ
#    for d in range(1,int(x ** 0.5) + 1):
#        if x%d == 0:
#            divs.add(d)
#            divs.add(x//d)
#    return divs
#print(f(14))
# в делители добавлять условия спокойно можно

# ------------------------------------------------------------

#def f(x):
#    divs = set()
#    for d in range(1,int(x**0.5) + 1):
#        if x % d == 0:
#            if d != x and d != 9 and d % 10 == 9:
#                divs.add(d)
#            if (x//d) != x and (x//d) != 9 and (x//d) % 10 == 9:
#                divs.add(x//d)
#    return divs

#for x in range(800000,801000):
#    divs = f(x)
#    if len(divs) > 0:
#        print(x, min(divs))

# ------------------------------------------------------------

# Задача на простоту числа или его делителя

#def p(x):
#    return x > 1 and all(x % d != 0 for d in range(2,int(x**0.5)+1))
    # Простое число больше единицы, d не является делителем, перебор от 2 (обязательно) до квадратного корня + 1 всевозможных делителей.
    # Если при проверке делителей их просто нет, то число является простым.

# ------------------------------------------------------------

#def p(x):
#    return x > 1 and all (x % d != 0 for d in range(2, int(x**0.5)+1))
#def f(x):
#    divs = set()
#    for d in range(1,int(x**0.5)+1):
#        if x % d == 0:
#            if p(d):
#                divs.add(d)
#            if p(x//d):
#                divs.add(x//d)
#    return divs
#for x in range(1000001, 1000500):
#    divs = f(x)
#    if len(divs) == 3:
#        print(x, max(divs))

# ------------------------------------------------------------

# Маски
#from fnmatch import fnmatch

#for x in range(1917, 10**10 + 1, 1917): # идем с шагом в 1917, тк НУЖНЫ КРАТНЫЕ 1917
#    if fnmatch(str(x), '3?12?14*5'):
#        if x % 1917 == 0:
#            print(x, x // 1917)

# ------------------------------------------------------------
#from fnmatch import fnmatch

#def f_all(x):
#    divs = set()
#    for d in range(2, int(x**0.5) + 1): # берем с 2, тк по условию не нужно само число в делителях
#        if x % d == 0:
#                divs.add(d)
#                divs.add(x//d)
#    return divs

#def f_m(x):
#    divs = set()
#    for d in range(1, int(x**0.5) + 1):
#        if x % d == 0:
#            if fnmatch(str(d), '*1?3'):
#                divs.add(d)
#            if fnmatch(str(x//d), '*1?3'):
#                divs.add(x//d)
#    return divs

#for x in range(500000,600000):
#    divs = f_all(x)
#    divs_mask = f_m(x)
#    if len(divs_mask) == 3:
#        print(x, max(divs))

# ------------------------------------------------------------




