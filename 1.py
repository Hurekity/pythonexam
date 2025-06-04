#from itertools import *
#print('1 2 3 4 5 6 7 8') # кол-во вершин
#a = '478 38 256 15 34 37 168 127'.split() # соседство пунктов по горизонтали
#s = 'DE DG GC GA BC FB FE FH BH AH'.split() # дороги

#for p in permutations('ABCDEFGH'): # все возможные перестановки
#    if all([str(p.index(x) + 1) in a[p.index(y)] for x,y in s]):
#        print(*p)
# ---------------------------------------------------------------
#from itertools import *
#print('1 2 3 4 5 6 7 8')
#a = '23 168 158 578 347 27 456 234'.split()
#s = 'HG HE HB GB GC CF FD FA DB DE AE'.split()

#for p in permutations('ABCDEFGH'):
#    if all([str(p.index(x) + 1) in a[p.index(y)] for x,y in s]):
#        print(*p)
# ---------------------------------------------------------------
#from itertools import *
#print ('1 2 3 4 5 6 7')
#a = '234 136 12 157 467 25 45'.split()
#s = 'BD BD FG FD GE GC CE EA AD'.split()

#for p in permutations('ABCDEFG'):
#    if all([str(p.index(x) + 1) in a[p.index(y)] for x,y in s]):
#        print(*p)
# ЗВЕЗДОЧКИ