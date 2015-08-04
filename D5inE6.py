#D5 in E6

import math
import pickle

from collections import Counter
import itertools
import re
from tensor_wedge import wedge2
from tensor_wedge import wedge3
from compare import checker
from compare import order
from compare import expand
from tensor_wedge import latex
from tensor_wedge import latexWithoutDollar
from compare import dimChecker
from compare import classifyIncomplete
#from compare import classifyIncomplete2
from compare import classify
from compare import perm
from tensor_wedge import concat
from remove_tensor_A1 import removeFirstA1
from remove_tensor_A1 import removeA1
from remove_tensor_A1 import diagA1
from tensor_wedge import printLE8
from tensor_wedge import tensor


print("A_1^4 in D5")
a=[(1,1,0,0),(0,0,1,1),(0,0,0,0),(0,0,0,0)]
b=[(1,1,0,0),(0,0,2,0),(0,0,0,2),(0,0,0,0)]
print(latex(wedge2(a)))
print(latex(wedge2(b)))



print("A_1^3 in D5")
lam=[0]
lam.append(expand("[(1,1,0)/(0,1,1)/(0,0,0)^2]"))
lam.append(expand("[(1,1,0)/(0,0,1)^2/(0,0,0)^2]"))
lam.append(expand("[(1,1,0)/(0,0,2)/(0,0,0)^3]"))
lam.append(expand("[(1,1,0)/(0,0,2)^2]"))
lam.append(expand("[(1,1,0)/(2,0,0)/(0,0,2)]"))
lam.append(expand("[(1,1,0)/(0,0,4)/(0,0,0)]"))
lam.append(expand("[(1,0,0)^2/(0,2,0)/(0,0,2)]"))
lam.append(expand("[(2,0,0)/(0,2,0)/(0,0,2)/(0,0,0)]"))
print(len(lam))
for i in range(1,len(lam)):
    print(dimChecker(lam[i]))




basisA13=[0]


basisA13.append(expand("[(1,4,1)/(1,2,1)/(1,0,3)/(2,0,0)/(0,4,2)/(0,4,0)/ (0,2,2)/(0,2,0)/(0,0,2)]"))
                       
basisA13.append(expand("[(1,2,2)^2/(1,0,0)^2/(2,0,0)/(0,4,0)/(0,0,4)/(0,2,0)/(0,0,2)/(0,2,2)^2/ (0,0,0)]"))

basisA13.append(expand("[(1,2,1)^2/(1,2,0)^2/(1,0,0)^2/(2,0,0)/(0,4,0)/(0,2,1)^2/(0,2,0)^3/(0,0,2)/(0,0,1)^2/(0,0,0)^2]"))

basisA13.append(expand("[(1,1,1)^2/(1,3,0)/(1,1,0)/(1,1,2)/(2,0,0)/(0,2,2)/ (0,2,0)^2/(0,0,2)/(0,2,1)^2/(0,0,1)^2/(0,0,0)]"))

                
basisA13.append(expand("[(1,1,1)^2/(1,2,0)^2/(1,0,2)^2/(2,0,0)/(0,2,0)/(0,0,2)/ (0,2,2)/(0,1,1)^4/(0,0,0)^4]"))
                

basisA13.append(expand("[(1,1,2)/(2,0,0)/(0,2,0)/(0,0,2)^4/(1,1,0)^3/(1,0,1)^4/(0,1,1)^4/(0,0,0)^4]"))

                
basisA13.append(expand("[(2,0,0)/(0,2,0)/(0,0,2)/(1,1,1)^2/(1,1,0)^2/(1,0,1)^2/(0,1,1)^2/(1,0,0)^4/ (0,1,0)^4/(0,0,1)^4/(0,0,0)^5]"))

                
basisA13.append(expand("[(0,6,0)/(1,4,1)/(0,4,0)/(1,3,0)^2/(0,3,1)^2/(2,0,0)/(0,2,0)/(0,0,2)/ (1,0,1)/(0,0,0)]"))

                
basisA13.append(expand("[(1,1,1)^4/(2,2,0)/(2,0,2)/(0,2,2)/(0,2,0)^2/(0,0,2)^2/(2,0,0)^2/(0,0,0)]"))

basisA13.append(expand("[(2,2,2)^2/(4,0,0)/(0,4,0)/(0,0,4)/(2,0,0)/(0,2,0)/(0,0,2)]"))


for i in range(1,len(basisA13)):
    print(dimChecker(basisA13[i]))

order3=order(3)
for i in range(1,len(lam)):
    x=wedge2(lam[i])
    n=classifyIncomplete(x,basisA13,order3)
    p=str(i) + " &  " +latex(lam[i])+" & "+ latex(x)+ " & "+str(n[1])+"\\\\ \\hline"
    print(p)
    


print("//////////////////////////////")
print("A12")
print("/////////////////////////////")

lam2 = [0]
lam2.append([(1, 1), (1, 1), (0, 0), (0, 0)])
lam2.append([(1, 1), (1, 0), (1, 0), (0, 0), (0, 0)])
lam2.append([(1, 1), (2, 0), (2, 0)])
lam2.append([(1, 1), (2, 0), (0, 2)])
lam2.append([(1, 1), (2, 0), (0, 0), (0, 0), (0, 0)])
lam2.append([(1, 1), (4, 0), (0, 0)])
lam2.append([(1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)])
lam2.append([(2, 2), (0, 0)])
lam2.append([(3, 1), (0, 0), (0, 0)])
lam2.append([(1, 0), (1, 0), (0, 1), (0, 1), (0, 0), (0, 0)])
lam2.append([(1, 0), (1, 0), (0, 2), (0, 2)])
lam2.append([(1, 0), (1, 0), (0, 2), (0, 0), (0, 0), (0, 0)])
lam2.append([(1, 0), (1, 0), (0, 4), (0, 0)])
lam2.append([(2, 0), (2, 0), (0, 2), (0, 0)])
lam2.append([(2, 0), (0, 2), (0, 0), (0, 0), (0, 0), (0, 0)])
lam2.append([(2, 0), (0, 4), (0, 0), (0, 0)])
lam2.append([(2, 0), (0, 6)])
lam2.append([(4, 0), (0, 4)])










basisA12=[0]
basisA12.append(expand("[(1,9)/(1,5)/(1,3)/(2,0)/(0,10)/(0,8)/(0,6)/(0,4)/(0,2) ]"))

basisA12.append(expand("[(0,8)/(1,6)^2/(0,6)/(0,4)^3/(1,2)^2/(2,0)/(0,2)/(0,0) ]"))

basisA12.append(expand("[(0,6)/(1,5)/(0,4)^3/(1,3)^3/(2,0)/(0,2)^4/(1,1)/(0,0) ]"))

basisA12.append(expand("[(0,6)/(1,4)^2/(0,4)/(1,3)^2/(0,3)^4/(2,0)/(0,2)/ (1,0)^2/(0,0)^4]"))
basisA12.append(expand("[(1,4)^2/(0,4)^4/(1,2)^2/(2,0)/(0,2)^4/(1,0)^4/(0,0)^3 ]"))

basisA12.append(expand("[(0,4)/(1,3)^2/(0,3)^2/(1,2)^2/(2,0)/(0,2)^4/(1,1)^2/(1,0)^2/ (0,1)^4/(0,0)^2]"))

basisA12.append(expand("[(1,3)/(2,0)/(0,2)^9/(1,1)^8/(0,0)^8 ]"))

basisA12.append(expand("[(1,2)^2/(2,0)/(0,2)^4/(1,1)^4/(1,0)^6/(0,1)^8/(0,0)^7 ]"))

basisA12.append(expand("[(2,0)/(0,2)/(1,1)^6/(1,0)^8/(0,1)^8/(0,0)^8/(0,0)^8 ]"))

basisA12.append(expand("[(0,4)/(1,2)^6/(2,0)/(0,2)^7/(1,0)^2/(0,0)^9 ]"))

basisA12.append(expand("[(4,1)^2/(4,2)/(4,0)/(0,3)^2/(2,1)^2/(2,2)/(2,0)/(0,2)/(0,0)^3 ]"))
basisA12.append(expand("[ (4,0)/(0,4)/(2,2)^6/(2,0)/(0,2)/(0,0)^8 ]"))

basisA12.append(expand("[ (3,0)^2/(2,2)/(2,1)^2/(1,2)^2/(2,0)^2/(0,2)/(1,1)^4/ (1,0)^2/(0,1)^2/(0,0)^4]"))
basisA12.append(expand("[(2,2)/(2,0)^5/(0,2)^5/(1,1)^8/(0,0)^7]"))



basisA12.append(expand("[(5,1)/(3,1)^2/(1,1)/(1,3)/(2,0)^2/(4,2)/(4,0)/(2,2)/(0,2)]"))
                       
basisA12.append(expand("[(2,4)/(0,4)/(2,2)^2/(0,2)^2/(4,0)/(2,0)^3/(2,4)/(0,4)]"))

basisA12.append(expand("[(3,2)^2/(1,2)^2/(1,0)^2/(2,0)^2/(4,0)/(0,4)/(0,2)/(2,2)^2/ (0,0)]"))


basisA12.append(expand("[(2,2)^2/(0,2)^5/(1,2)^2/(1,0)^2/(2,0)^2/(0,4)/(1,2)^2/(1,0)^2/(0,0)^2]"))

basisA12.append(expand("[(2,1)^2/(0,1)^2/(1,3)/(1,1)^2/(3,1)/(2,0)^2/(2,2)/(0,2)^2/ (1,2)^2/(1,0)^2/(0,0)]"))

 
basisA12.append(expand("[(0,6)/(2,4)/(0,4)/(0,4)/(1,3)^2/(1,3)^2/(2,0)^2/(0,2)/ (2,0)/(0,0)^2]"))


basisA12.append(expand("[ (6,0)/(0,6)/(4,4)/(3,3)^2/(2,0)/(0,2)/(0,0) ]"))

basisA12.append(expand("[(0,10)/(4,6)/(2,6)/(4,0)/(2,0)/(0,2)]"))
basisA12.append(expand("[(2,6)/(1,6)^2/(0,6)/(2,0)/(1,0)^2/(0,0)/(0,10)/(0,2)]"))


basisA12.append(expand("[(4,2)/(2,4)/(0,2)/(2,0)/(2,2)/(3,1)^2/(1,3)^2/(0,0)]"))












print(len(basisA12))
for i in range(1,len(lam2)):
    print(dimChecker(lam2[i]))

order2=order(2)
for i in range(1,len(lam2)):
    x=wedge2(lam2[i])
    n=classifyIncomplete(x,basisA12,order2)
    p=str(i) + " &  " +latex(lam2[i])+" & "+ latex(x)+ " & "+str(n)+"\\\\ \\hline"
    print(p)
       


