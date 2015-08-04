import math
from collections import Counter
import itertools
import re


def expand(in_str):
	regex = r"(\([^\)]+\))(?:\^(\d+))?"
	groups = re.findall(regex, in_str)
	out_list = []
	for group, mult in groups:
		if not mult:
			mult = 1
		for i in range(int(mult)):
			out_list.append(eval(group))

	return out_list
def dimChecker(x):
    sol=0
    for i in range(0,len(x)):
        temp=1
        for j in range(0,len(x[i])):
            temp = temp*(x[i][j]+1)
        sol = sol+temp
    return(sol)

#This fction checks if x and y are equal when you do not consider order
def eq(x,y):
    yy=y
    if len(x)!=len(yy):
        #print("Not the same length")
        return False
    for i in range(0,len(x)):
        if x[i] in yy:
           # print "i=", i," and x[i] = ",x[i]," and is in y" )
            yy.remove(x[i])
        else:
            return False
    return True


def classify(tester, basis,orderList ):
    sol = -1
    for i in range(0,len(basis)):
       
        #print("i="+str(i))
        #print("basis[i]=")
        #print(basis[i])
        if len(tester) != len( basis[i]):
           # print("not same length so I skip:")
            #print(basis[i])
            continue
    
        for j in range(0,len(orderList)):

            vector = perm(orderList[j], basis[i])
            tt=list(tester)
            if eq(vector, tt):
              #  print("WE HAVE FOUND A MATCH using orderList[j] =")
                #print(orderList[j])
                sol = i;
                
          
            else:
                manon=1
              #  print("It is not a match, we have have used orderList[j] =")
                #print(orderList[j])
            
    return(sol)




def classifyIncomplete(tester, basis,orderList ):
    sol = [-1]
    for i in range(1,len(basis)):
    
         for j in range(0,len(orderList)):
        
            vector = perm(orderList[j], basis[i])

            tt=list(tester)
            if eqIncomplete(tester,vector):
               # print("WE HAVE FOUND A MATCH using at element "+str(i))
                #print(orderList[j])
                sol.append(i);
                
          
            else:
                manon=1
              #  print("It is not a match, we have have used orderList[j] =")
                #print(orderList[j])
            
    return(sol)



def checker(tester, basis,orderList ):
    incomplete=[]
    #incomplete=[23,24]
    #print("Which complete option is it equal to?")
    #print(classify(tester, basis,orderList ))
    temp5 = classify(tester, basis,orderList )
    at=expand("[(0,6,0,0)/(0,4,2,0)/(0,3,2,1)/(0,3,0,1)/(2,0,0,0)/(0,2,0,0)/(0,0,2,0)^2/(0,0,0,2)/ (1,4,1,0)/(1,3,1,1)/(1,0,3,0)/(1,0,1,0)]")
    options=[at]
    at=expand("[(0,1,2,1)/(0,0,1,2)^2/(2,0,0,0)/(0,2,0,0)/(0,0,2,0)^2/(0,0,0,2)^2/(0,1,1,1)^2/(0,1,0,1)/(0,0,1,0)^2/(0,0,0,0)^3/(1,1,1,1)/(1,0,2,0)^2/(1,0,1,2)/(1,1,0,1)^2/(1,0,1,0)/(1,0,0,0)^2 ]")
    options.append(at)
    at=expand("[(0,1,2,0)^2/(2,0,0,0)/(0,2,0,0)/(0,0,2,0)^2/(0,0,0,2)/(0,0,1,1)^4/(0,1,1,1)^2/(0,1,0,0)^2/(0,0,0,0)^6/(1,0,2,1)/(1,1,1,0)^2/(1,1,0,1)^2/(1,0,0,1)/(1,0,1,0)^4 ]")
    options.append(at)
    at=expand("[  (2,0,0,0)/(0,2,0,0)/(0,0,2,0)/(0,0,0,2)/(0,1,1,0)^4/(0,1,0,1)^4/(0,0,1,1)^4/(0,0,0,0)^9/(1,1,1,0)^2/(1,1,0,1)^2/ (1,0,0,0)^8/(1,0,1,1)^2/]")
    options.append(at) 

    bIncomplete=list(basis)
    bIncomplete.append(tester)
    for i in range(0,len(options)):
        if i==0  :
                if eq( tester,options[0]):
                        print("This is conjugate to the second option of case 3")
        if i==1 and eq(tester,options[1]):
                print("This is conjugate to the second option of 18")
        if i==2 and eq(tester,options[2]):
                print("This is conjugate to the second option of 19")
        if i==3 and eq(tester,options[3]):
                print("This is conjugate to the second option of 20")

    #print("Now check the incomplete")
    for i in incomplete:
        print("Is it potentially conjugate to "+str(i))

        if len(classifyIncomplete(basis[i], bIncomplete,orderList ))>2:
                print("yes, this was the classification:")
        else:
                print("no, this was the classification:")
        print(classifyIncomplete(basis[i], bIncomplete,orderList ))
    return temp5

def order(n):
    o=[]
    stuff = [0]
    for i in range(1,n):
        stuff.append(i)
    for subset in itertools.permutations(stuff, n):
            o.append(subset)
    return(o)



def perm(order, xx):
    
    res=[]

    for t in range(0,len(xx)):
        y=(xx[t][order[0]],)
        for j in range(1,len(xx[t])):
            y = y+(xx[t][order[j]],)
        res.append(y)
    return res


def eqIncomplete(x,y):
    for i in range(0,len(x)):
        if x[i] in y:
           # print "i=", i," and x[i] = ",x[i]," and is in y" )
            y.remove(x[i])
        else:
            return False
        #print(y)
    return True



