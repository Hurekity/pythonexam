#a = [5,5,12,1,1,1]
#p3 = [x for x in a if a.count(x) == 3]
#count = 0
#for line in open('9.txt'):
#    a = [int(x) for x in line.split()] # список всех чисел из строки в файле
#    p2 = [x for x in a if a.count(x) == 2] # список повторяющихся дважды чисел
#    if max(a) < sum(a)-max(a): # сумма всех остальных чисел, кроме максимального
#        if len(p2) == 2:
#            count += 1
#print(count)

# ---------------------------------------------------------

#k = 0
#for line in open('9.txt'):
#    a = [int(x) for x in line.split()]
#    p = [x for x in a if a.count(x) > 1] #повторяющиеся числа
#    np = [x for x in a if a.count(x) == 1] #неповторяющиеся числа
#    if len(p) > 0 and len(np) > 0: # проверка на логику, что такие строки с числами вообще существуют
#        if a.count(max(a)) == 1: # в строке не повторяются максимальные числа
#            if sum(np) >= sum(p) * 3:
#                k+=1
#print(k)

# ---------------------------------------------------------

#k = 0
#for line in open('9.txt'):
#    a = [int(x) for x in line.split()]
#    p2 = [x for x in a if a.count(x) == 2]
#    np = [x for x in a if a.count(x) == 1]
#    ch = [x for x in a if x%2==0]
#    if len(ch) == 0:
#        each = 0
#    else:
#        each = sum(ch) / len(ch)
#    nch = [x for x in a if x%2!=0]
#    if len(nch) == 0:
#        avgnch = 0
#    else:
#        avgnch = sum(nch)/len(nch)
#    usl1 = len(p2) == 2 and len(np) == 4
#    usl2 = abs(each - avgnch) > 50
#    if usl1 + usl2 == 1: # ВЫПОЛНЯЕТСЯ ТОЛЬКО ОДНО ИЗ УСЛОВИЙ, БЕРЕМ ЗНАЧЕНИЕ ЗА BOOL
#        k += 1
#print(k)







