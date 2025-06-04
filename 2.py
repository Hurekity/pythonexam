# Up arrow = and, down arrow = or
#print("x", "y", "z", "w")
#for x in range(2):
#   for y in range(2):
#        for z in range(2):
#            for w in range(2):
#                f = z or (z == w) or (not(y <= x))
#                if f == 0:
#                    print(x, y, z, w)
# IF F EQUALS ONLY 0 OR 1 IN THE END
# -------------------------------------------------------
#print("x y z w f")
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            for w in range(2):
#                f = ((y <= x) == (w <= (not z))) and (w or x)
#                print(x, y, z, w, int(f))
# IF F EQUALS BOTH 0 AND 1 IN THE END
# -------------------------------------------------------
#from itertools import *
#def f(x,y,z,w):
#   return ((x <= y) or (z == x)) and (w <= z)

#t = [(0,0,1,1), (0,0,1,0),(0,1,1,1)]
#for p in permutations('xyzw'):
#   if[f(**dict(zip(p,r))) for r in t] == [1,0,0]:
#       print(*p, sep='')
# IF F EQUALS BOTH 0 AND 1 IN THE END
# -------------------------------------------------------
