from itertools import *
#k = 0
#for p in product('АБДЕОП', repeat=6):
#    k+=1
#    x = ''.join(p)
#    if x[0]=='О':
#        np = [f for f in x if x.count(f)==1]
#        if len(np)==6:
#            print(k)
# --------------------------------------------------------------
# k = 0
# for p in product('0123456789AB', repeat=5):
#   x=''.join(p)
#   if x.count('7') == 1 and and x[0] != 0:
#       np = [f for f in x if int(f,12)>8]
#       if len(np) <= 3:
#       k += 1
# print(k)
# --------------------------------------------------------------
#words = list(product('ШКОЛА', repeat=3)) # всевозможные трехбуквенные слова из букв
#k = 0
#for x in words:
#    if x.count('К') == 1:
#        k += 1
#print(k)
# составление слов из букв
# --------------------------------------------------------------
#words = list(product('ГАФНИЙ', repeat=4))
#k = 0
#for w in words:
#    if w[0] != 'Й' and (w.count('А') + w.count('И')) >= 1: # условие хотя-бы на одну гласную
#        k+=1
#print(k)
# --------------------------------------------------------------
#k = 0
#d = list(product('0123456789AB', repeat = 5))
#for x in d:
#    if x.count('7') == 1:
#         if (x.count('9') + x.count('A') + x.count('B')) <= 3:
#             if x[0] != '0':
#              k+=1
#print(k)
# --------------------------------------------------------------
#k = 0
#d = list(product('0123456789AB', repeat = 5))
#for x in d:
#    if x.count('7') == 1:
#         if sum([x.count(c) for c in '9AB']) <= 3: # кол-во цифр в записи более двух
#             if x[0] != '0':
#              k+=1
#print(k)
# --------------------------------------------------------------
#n = list(permutations('0123456789ABCDEF',r=3))
#bad = list(permutations('02468ACE', r=2)) + list(permutations('13579BDF', r=2)) # условие
#k = 0
#for x in n:
#    if all([''.join(badn) not in ''.join(x) for badn in bad]): # join чтобы убрать скобочки и генератор списка
#        if x[0] != '0':
#            k+=1
#print(k)
# --------------------------------------------------------------
#n = list(product('012345', repeat=6))
#k=0
#bad = ['12', '21', '23', '32', '25', '52']
#for x in n:
#    x = ''.join(x)
#    if x.count('2') == 1:
#        if all(b not in x for b in bad):
#            if x[0] != '0':
#                k+=1
#print(k)
# --------------------------------------------------------------
#k = 0
#for x in product('АВНРЬЯ', repeat=5):
#    s = ''.join(x)
#    k+=1
#    if s[0] != 'Я' and s.count('Ь') <= 1 and 'ЯЯ' not in s:
#        print(k,s)
