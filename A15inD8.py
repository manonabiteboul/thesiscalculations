import math
from collections import Counter
import itertools
import re
from tensor_wedge import wedge2
from compare import checker
from compare import order
from compare import expand
from tensor_wedge import latex
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

#Finding all possible VD8(lambda1) \downarrow A1^5

#Function to find wedights of VD8(lambda1) \downarrow A1 for ith A1
def isZero(L,n):
    checker=True
    for i in range(0,len(L)):
        if L[i][n] !=0:
            checker=False
    return(checker)
L=[(0,2,0),(1,5,1)]
print(isZero(L,1))



#VD8(lambda1) has dim 12
d=16

L=[]

#List of all possible weights
for i in range(0,d-1):
    if i%2==0:
        L.append([(i,0,0,0,0)])
    else :
        temp=[(i,0,0,0,0),(i,0,0,0,0)]
        tempdim=dimChecker(temp)
        if tempdim<=d:
                L.append(temp)

o=order(5)
for i in range(0,len(L)):
    for j in range(0,len(o)): 
        temp=perm(o[j],L[i])
        if temp not in L:
            L.append(temp)
        
Ladd = [[(1,1,0,0,0)],[(2,2,0,0,0)],[(1,3,0,0,0)],[(1,1,2,0,0)]]
for i in range(0,len(Ladd)):
    for j in range(0,len(o)): 
        temp=perm(o[j],Ladd[i])
        if temp not in Ladd:
            Ladd.append(temp)

L= L+Ladd

print(L)




def assemble(L,n):
    print("newloop : " + str(n))
    sol=[]
    for i in range(0,len(L)):
         print("i="+str(i))
         a=dimChecker(L[i])
         print(a)
         if a>n:
             
             return []
         if a==n:
           return [L[i]]
         else:
             print("here")
             temp=assemble(L,n-a)

             print("temp=")
             print(temp)
             if len(temp)>=1:
                 
                 return L[i]+temp
             else :
                 return []
##L=[[(2,0,0)],[(1,1,0)],[(0,1,0),(0,1,0)],[(0,0,3),(0,0,3)]]
##print(assemble(L,6))
##
##p=itertools.combinations_with_replacement(L, 2)
##final=[]
##n=12
##L=[[(2,0,0)],[(1,1,0)],[(0,1,0),(0,1,0)],[(0,0,3),(0,0,3)]]
##a=itertools.combinations_with_replacement(L, 5)
##for x in a:
##    print("x:")
##    print(x)
##    V1=[x[0]]
##    for i in range(0,len(x)):
##        dim=dimChecker(V1)+dimChecker(x[i])
##        if dim==n:
##            #for j in range(0,len(x[i])):
##             #   V1.append(x[i][j])
##            V1.append(x[i])
##            final.append(V1)
##        


#FRANK
##
##def dim(x):
##    sol=1
##    for i in range(0,len(x)):
##      sol = sol*(x[i]+1)
##    return(sol)
##
##vs = [[(2,0,0)],[(1,1,0)],[(0,1,0),(0,1,0)],[(0,0,3),(0,0,3)]]
##solutions = set()
##count = 0
##
##for combination in itertools.combinations_with_replacement(L, 4):
##  # flatten combination
##  combination = itertools.chain.from_iterable(combination)
##  count += 1
##  print(count, len(vs))
##
##  solution = []
##
##  dim_sum = 0
##  for v in combination:
##    dim_sum += dim(v)
##    solution.append(v)
##    if dim_sum >= 12:
##      break
##
##  if dim_sum == 12:
##    zero=False
##    #print(solution)
##    for i in range(0,5):
##        if isZero(solution,i):
##            zero=True
##    if zero==False:
##        print(solution)
##        solutions.add(tuple(solution))
##
##for sol in solutions:
##  print(sol)
##print(len(solutions))
##                








        
