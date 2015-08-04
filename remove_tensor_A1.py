import math
from tensor_wedge import concat
from tensor_wedge import latex
from tensor_wedge import tensor

def removeFirstA1(L):
    finalSol=[]
    n=len(L[0])
    for j in range(0,len(L)):
        sol=()
        x=L[j]
        deg=x[0]
        for i in range(1,n):
            sol=sol+(x[i],)
        for i in range(0,deg+1):
            finalSol.append(sol)
        
    return(finalSol)

def removeA1(L,k):
    finalSol=[]
    n=len(L[0])
    for j in range(0,len(L)):
        sol=()
        x=L[j]
        deg=x[k-1]
        for i in range(0,n):
            if i!=k-1:
                sol=sol+(x[i],)
        for i in range(0,deg+1):
            finalSol.append(sol)
        
    return(finalSol)


def diagA1(L,index1,index2):
    n=len(L[0])
    sol=[]
    ind1=index1-1
    ind2=index2-1
    for i in range(0,len(L)):
        #print("i= "+str(i))
        x=tensor([(L[i][ind1],)],[(L[i][ind2],)])
        #print("this is x:")
        #print(x)
        temp2=[]
        for t in range(0,len(x)):
            temp2.append((x[t],))
        #for t in range(0,len(x)):
        #    x=[(x[0],)]
        #print("This is temp2:")
        #print(temp2)
        
        s=()
        for j in range(0,n):
            if j!=ind1 and j!=ind2:
                s=s+(L[i][j],)
        #print("this is s:")
        #print(s)
        temp=[]
        temp.append(s)
        a=concat(temp2,temp)
        #print(a)
        for t in range(0,len(a)):
            sol.append(a[t])
        #sol.append(a)
    return(sol)


