#def f(x,end):
#    if x>end: return 0
#    if x == end: return 1
#    return f(x+1,end) + f(x*2,end)
#print(f(1,10) * f(10,20)) # гарантия прохода алгоритма через 10

# ------------------------------------------------------------

#def f(x,end):
#   if x > end: return 0
#    if x == 12: return 0 # НЕ ПРОХОДИТ ЧЕРЕЗ 12, ПОЭТОМУ ПРОСТО ПРИ Х = 12 РВЕМ МАРШРУТ
#    if x == end: return 1
#    return f(x+1,end) + f(x+2,end) + f(x*3,end)
#print(f(2,19)*f(9,19))

# ------------------------------------------------------------

#def f(x,end):
#    if x > end: return 0
#    if x == end: return 1
#    return f(x+1,end) + f(x+2,end) + f(x+3,end)
#print(f(5,7)*f(7,11))

# ------------------------------------------------------------

#def f(x,end):
#    if x < end: return 0
#    if x == end: return 1
#    return f(x-2,end) + f(x//2, end)

#print(f(32,14) * f(14,1))

# ------------------------------------------------------------

#def f(x,end):
#    if x > end: return 0
#    if x == end: return 1
#    if x == 32: return 0
#    return f(x+3,end) + f(x+5,end) + f(x*2, end)

#print(f(4,16)*f(16,68))
# replace 16 and 32 по условию

# ------------------------------------------------------------

def f(x,end):
    if x < end: return 0
    if x == end: return 1
    turns = []
    turns.append(f(x-3,end))
    if x % 2 == 0:
        turns.append(f(x//3,end))
    if x >= 10:
        turns.append(f(x//10,end)) # - отбрасываем последнюю цифру
    return sum(turns)
print(f(1250,20))