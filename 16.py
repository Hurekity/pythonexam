#from functools import *

#@lru_cache(None)

#def f(n):
#    if n == 1:
#        return 1
#    if n > 1:
#        return n * f(n - 1)

#for n in range(1,2024):
#    f(n)
#print((2*f(2024)+f(2023)) / f(2022))

# ---------------------------------------------------

#from functools import lru_cache

#@lru_cache(None)

#def f(n):
#    if n < 7: return 7
#   if n >= 7 and n%3 != 0: return 5-f(n-1)
#    if n >= 7 and n%3 == 0: return 3+f(n-1)

#for n in range(8,3015):f(n)

#print(f(3015))

# ---------------------------------------------------

#from functools import lru_cache

#@lru_cache(None)
#def f(n):
# lalalala
#def g(n):
# lalalala

#for n in range(10,3000): g(n)
#for n in range(3215,10,-1): f(n) - -1 для разворота range в обратную сторону

#print(f(15)-g(3000)) = 2462

# ---------------------------------------------------
#from functools import lru_cache
#@lru_cache(None)
#def f(n):
#    if n < 3: return n + 1
#    if n >= 3 and n%2 == 0: return f(n-2) + n-2
#    if n >= 3 and n%2 != 0: return f(n+2) + n-2
#
#k = 0
#for n in range(1, 10000):
#    try:
#         if 10000 <= abs(f(n)) <= 99999:
#             k += 1
#    except: pass
#print(k)
#Если в задании предусмотрена ошибка, то используем try and except

# ---------------------------------------------------

#from functools import lru_cache
#@lru_cache(None)
#def f(n,x):
#    if n >= 3000: return n
#    if n < 3000: return n + x + f(n+2,x)

#for x in range(-10000,10000):
#    if f(2984,x)-f(2988,x) == 5916:
#        print(x)

# ---------------------------------------------------