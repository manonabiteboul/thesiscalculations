import math
from collections import Counter
import itertools
import re
from tensor_wedge import wedge2
from tensor_wedge import S2
from tensor_wedge import wedge4
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






basisA12=[[(0)]]
basisA12Lambda1=[[(0)]]
lambda1=[(0)]
lambda2=[(0)]
lambda5=[(0)]
lambda4=[(0)]


#The first 30 cases are A1A1 in A1D6

lambda1.append([(10,), (0,)])
lambda5.append([(15,),(9,),(5,)])
lambda4.append([(15,),(9,),(5,)])

lambda1.append([(8,), (2,)])
lambda5.append(expand("[(11,)/(9,)/(5,)/(3,)]"))
lambda4.append(expand("[(11,)/(9,)/(5,)/(3,)]"))


lambda1.append([(6,), (4,)])
lambda5.append(expand("[(9,)/(7,)/(5,)/(3,)^2]"))
lambda4.append(expand("[(9,)/(7,)/(5,)/(3,)^2]"))

lambda1.append([(6,), (2,), (0,), (0,)])
lambda5.append(expand("[(7,)^2/(5,)^2/(1,)^2]"))
lambda4.append(expand("[(7,)^2/(5,)^2/(1,)^2]"))


lambda1.append([(6,), (0,), (0,), (0,), (0,), (0,)])
lambda5.append(expand("[(6,)^4/(0,)^4]"))
lambda4.append(expand("[(6,)^4/(0,)^4]"))

lambda1.append([(6,), (0,), (1,), (1,)])
lambda5.append(expand("[(7,)/(5,)/(6,)^2/(0,)^2/(1,)]"))
lambda4.append(expand("[(7,)/(5,)/(6,)^2/(0,)^2/(1,)]"))




lambda1.append([(4,), (2,), (2,), (0,)])
lambda5.append(expand("[(5,)^2/(3,)^4/(1,)^2]"))
lambda4.append(expand("[(5,)^2/(3,)^4/(1,)^2]"))

lambda1.append([(4,), (2,), (0,), (0,), (0,), (0,)])
lambda5.append(expand("[(4,)^4/(2,)^4]"))
lambda4.append(expand("[(4,)^4/(2,)^4]"))

lambda1.append([(4,), (2,), (1,), (1,)])
lambda5.append(expand("[(5,)/(3,)^2/(1,)/(4,)^2/(2,)^2]"))
lambda4.append(expand("[(5,)/(3,)^2/(1,)/(4,)^2/(2,)^2]"))

lambda1.append([(4,), (0,), (0,), (0,), (0,), (0,), (0,), (0,)])
lambda5.append(expand("[(3,)^8]"))
lambda4.append(expand("[(3,)^8]"))

lambda1.append([(4,), (0,), (0,), (0,), (1,), (1,)])
lambda5.append(expand("[(4,)^2/(2,)^2/(3,)^4]"))
lambda4.append(expand("[(4,)^2/(2,)^2/(3,)^4]"))

lambda1.append([(2,), (2,), (2,), (2,)])
lambda5.append(expand("[(4,)^2/(2,)^6/(0,)^4]"))
lambda4.append(expand("[(4,)^2/(2,)^6/(0,)^4]"))

lambda1.append([(2,), (2,), (2,), (0,), (0,), (0,)])
lambda5.append(expand("[(3,)^4/(1,)^8]"))
lambda4.append(expand("[(3,)^4/(1,)^8]"))

lambda1.append([(2,), (2,), (0,), (0,), (0,), (0,), (0,), (0,)])
lambda5.append(expand("[(2,)^8/(0,)^8]"))
lambda4.append(expand("[(2,)^8/(0,)^8]"))

lambda1.append([(2,), (2,), (0,), (0,), (1,), (1,)])
lambda5.append(expand("[(3,)^2/(1,)^4/(2,)^4/(0,)^4]"))
lambda4.append(expand("[(3,)^2/(1,)^4/(2,)^4/(0,)^4]"))

lambda1.append([(2,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,)])
lambda5.append(expand("[(1,)^8/(1,)^8]"))
lambda4.append(expand("[(1,)^8/(1,)^8]"))

lambda1.append([(2,), (0,), (0,), (0,), (0,), (0,), (1,), (1,)])
lambda5.append(expand("[(2,)^4/(1,)^8/(0,)^4]"))
lambda4.append(expand("[(2,)^4/(1,)^8/(0,)^4]"))

lambda1.append([(2,), (0,), (3,), (3,)])
lambda5.append(expand("[(5,)/(4,)^2/(3,)/(2,)^2/(1,)^3]"))
lambda4.append(expand("[(5,)/(4,)^2/(3,)/(2,)^2/(1,)^3]"))

lambda1.append([(2,), (0,), (1,), (1,), (1,), (1,)])
lambda5.append(expand("[(3,)/(2,)^4/(1,)^6/(0,)^4]"))
lambda4.append(expand("[(3,)/(2,)^4/(1,)^6/(0,)^4]"))

lambda1.append([(0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (1,), (1,)])
lambda5.append(expand("[(1,)^8/(0,)^8/(0,)^8]"))
lambda4.append(expand("[(1,)^8/(0,)^8/(0,)^8]"))

lambda1.append([(0,), (0,), (0,), (0,), (3,), (3,)])
lambda5.append(expand("[(4,)^2/(3,)^4/(0,)^6]"))
lambda4.append(expand("[(4,)^2/(3,)^4/(0,)^6]"))

lambda1.append([(0,), (0,), (0,), (0,), (1,), (1,), (1,), (1,)])
lambda5.append(expand("[(2,)^2/(1,)^8/(0,)^5/(0,)^5]"))
lambda4.append(expand("[(2,)^2/(1,)^8/(0,)^5/(0,)^5]"))

#2 possible lambda5 in this case
lambda1.append([(3,), (3,), (1,), (1,)])
lambda5.append(expand("[(4,)^4/ (2,)^2/ (0,)^6]"))
lambda4.append(expand("[(5,)/(3,)^5/(1,)^3]"))

lambda1.append([(3,), (3,), (1,), (1,)])
lambda5.append(expand("[(5,)/(3,)^5/(1,)^3]"))
lambda4.append(expand("[(4,)^4/ (2,)^2/ (0,)^6]"))

#2 possible lambda5
lambda1.append([(1,), (1,), (1,), (1,), (1,), (1,)])
lambda5.append(expand("[(2,)^6/(0,)^9/(0,)^5]"))
lambda4.append(expand("[(3,)/(1,)^9/(1,)^5]"))

lambda1.append([(1,), (1,), (1,), (1,), (1,), (1,)])
lambda5.append(expand("[(3,)/(1,)^9/(1,)^5]"))
lambda4.append(expand("[(2,)^6/(0,)^9/(0,)^5]"))

#Check lambda5??
lambda1.append([(8,), (0,), (0,), (0,)])
lambda5.append(expand("[(10,)^2/(4,)^2]"))
lambda4.append(expand("[(10,)^2/(4,)^2]"))

#What is lambda5??
lambda1.append([(4,), (4,), (0,), (0,)])
lambda5.append(expand("[(6,)^2/(4,)^2/(2,)^2/(0,)^2]"))
lambda4.append(expand("[(6,)^2/(4,)^2/(2,)^2/(0,)^2]"))

#What is the spin here?
lambda1.append([(5,), (5,)])
lambda5.append(expand("[(8,)^2/(4,)^2/(0,)^4]"))
lambda4.append(expand("[(5,)^3/(9,)/(3,)]"))

#What is the spin here?
lambda1.append([(5,), (5,)])
lambda5.append(expand("[(5,)^3/(9,)/(3,)]"))
lambda4.append(expand("[(8,)^2/(4,)^2/(0,)^4]"))

for i in range(1,len(lambda1)):
    lambda2.append(wedge2(lambda1[i]))
    #print(dimChecker(lambda2[i]))



orderList3=order(3)
basisA13=[[0]]
basisA13Lambda1=[[0]]

for i in range(1,38):
    print("case i")
    LE8[i]=[]
    LE8[i]=concat([(1,1)],lambda1[i])
    LE8[i]=LE8[i]+concat([(1,0)],lambda4[i])
    LE8[i]=LE8[i]+[(2,0,0),(0,2,0)]
    LE8[i]=LE8[i]+concat([(0,0)],lambda2[i])
    LE8[i]=LE8[i]+concat([(0,1)],lambda5[i])
    if dimChecker(LE8[i])!=248:
        print("LE8 does not have dim 248 at i=")
        print(i)
        
    temp=checker(LE8[i],basisA13,orderList3)
    print(temp)
    if temp==-1:
        print("New element, added to basis")
        basisA13.append(LE8[i])
        basisA13Lambda1.append(lambda1[i])
    else:
        print("conjugate")



