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





#######################################################
#######################################################
#A12inE7
#######################################################
#######################################################28
basisA12=[[(0)]]
basisA12Lambda1=[[(0)]]
lambda1=[(0)]
lambda2=[(0)]
lambda5=[(0)]

lambda1.append([(10,), (0,)])
lambda5.append([(15,),(9,),(5,)])

lambda1.append([(8,), (2,)])
lambda5.append(expand("[(11,)/(9,)/(5,)/(3,)]"))



lambda1.append([(6,), (4,)])
lambda5.append(expand("[(9,)/(7,)/(5,)/(3,)^2]"))

lambda1.append([(6,), (2,), (0,), (0,)])
lambda5.append(expand("[(7,)^2/(5,)^2/(1,)^2]"))

lambda1.append([(6,), (0,), (0,), (0,), (0,), (0,)])
lambda5.append(expand("[(6,)^4/(0,)^4]"))

lambda1.append([(6,), (0,), (1,), (1,)])
lambda5.append(expand("[(7,)/(5,)/(6,)^2/(0,)^2/(1,)]"))




lambda1.append([(4,), (2,), (2,), (0,)])
lambda5.append(expand("[(5,)^2/(3,)^4/(1,)^2]"))

lambda1.append([(4,), (2,), (0,), (0,), (0,), (0,)])
lambda5.append(expand("[(4,)^4/(2,)^4]"))

lambda1.append([(4,), (2,), (1,), (1,)])
lambda5.append(expand("[(5,)/(3,)^2/(1,)/(4,)^2/(2,)^2]"))

lambda1.append([(4,), (0,), (0,), (0,), (0,), (0,), (0,), (0,)])
lambda5.append(expand("[(3,)^8]"))

lambda1.append([(4,), (0,), (0,), (0,), (1,), (1,)])
lambda5.append(expand("[(4,)^2/(2,)^2/(3,)^4]"))

lambda1.append([(2,), (2,), (2,), (2,)])
lambda5.append(expand("[(4,)^2/(2,)^6/(0,)^4]"))

lambda1.append([(2,), (2,), (2,), (0,), (0,), (0,)])
lambda5.append(expand("[(3,)^4/(1,)^8]"))

lambda1.append([(2,), (2,), (0,), (0,), (0,), (0,), (0,), (0,)])
lambda5.append(expand("[(2,)^8/(0,)^8]"))

lambda1.append([(2,), (2,), (0,), (0,), (1,), (1,)])
lambda5.append(expand("[(3,)^2/(1,)^4/(2,)^4/(0,)^4]"))

lambda1.append([(2,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,)])
lambda5.append(expand("[(1,)^8/(1,)^8]"))

lambda1.append([(2,), (0,), (0,), (0,), (0,), (0,), (1,), (1,)])
lambda5.append(expand("[(2,)^4/(1,)^8/(0,)^4]"))

lambda1.append([(2,), (0,), (3,), (3,)])
lambda5.append(expand("[(5,)/(4,)^2/(3,)/(2,)^2/(1,)^3]"))

lambda1.append([(2,), (0,), (1,), (1,), (1,), (1,)])
lambda5.append(expand("[(3,)/(2,)^4/(1,)^6/(0,)^4]"))

lambda1.append([(0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (1,), (1,)])
lambda5.append(expand("[(1,)^8/(0,)^8/(0,)^8]"))

lambda1.append([(0,), (0,), (0,), (0,), (3,), (3,)])
lambda5.append(expand("[(4,)^2/(3,)^4/(0,)^6]"))

lambda1.append([(0,), (0,), (0,), (0,), (1,), (1,), (1,), (1,)])
lambda5.append(expand("[(2,)^2/(1,)^8/(0,)^5/(0,)^5]"))

#2 possible lambda5 in this case
lambda1.append([(3,), (3,), (1,), (1,)])
lambda5.append(expand("[(4,)^4/ (2,)^2/ (0,)^6]"))

lambda1.append([(3,), (3,), (1,), (1,)])
lambda5.append(expand("[(5,)/(3,)^5/(1,)^3]"))

#2 possible lambda5
lambda1.append([(1,), (1,), (1,), (1,), (1,), (1,)])
lambda5.append(expand("[(2,)^6/(0,)^9/(0,)^5]"))

lambda1.append([(1,), (1,), (1,), (1,), (1,), (1,)])
lambda5.append(expand("[(3,)/(1,)^9/(1,)^5]"))

#Check lambda5??
lambda1.append([(8,), (0,), (0,), (0,)])
lambda5.append(expand("[(10,)^2/(4,)^2]"))

#What is lambda5??
lambda1.append([(4,), (4,), (0,), (0,)])
lambda5.append(expand("[(6,)^2/(4,)^2/(2,)^2/(0,)^2]"))

#What is the spin here?
lambda1.append([(5,), (5,)])
lambda5.append(expand("[(8,)^2/(4,)^2/(0,)^4]"))


for i in range(1,len(lambda1)):
    lambda2.append(wedge2(lambda1[i]))
    #print(dimChecker(lambda2[i]))


orderList2=order(2)
L=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,len(lambda1)):
    L[i]=[]
    L[i]=L[i]+concat([(0,)],lambda2[i])
    L[i]=L[i]+[(2,0)]
    L[i]=L[i]+concat([(1,)],lambda5[i])
    x=checker(L[i],basisA12,orderList2)
 #   print("///////////////////////////////")
 #   print(i)
 #   print(x)
    basisA12.append(L[i])
    basisA12Lambda1.append(lambda1[i])
    checker(L[i],basisA12,orderList2)
 #   if dimChecker(L[i])!=133:
 #       print("////////////////////////////////////")
 #       print(latex(lambda1[i]))
 #       print(dimChecker(L[i]))
 #       print(latex(L[i]))

for i in range(1,1):
    p=""
    p=p+str(i)+"&"
    temp=latex(lambda1[i])
    for j in range(0,len(temp)):
        if temp[j]!='(' and temp[j]!=')' and temp[j]!=',':
            p=p+temp[j]

    p=p+"& "
    p=p+latex(L[i])
    p=p+"   \\\\ "
    print(p)
    print("&& $$ \\\\ \\hline")




def checkerA12inE8(l,basis,orderList):
    print("Checking if conjugate to any of the complete ones:")
    print(checker(l,basis,orderList))

    #These are two two cases where we do not know lambda5: cases 28 and 29
    l28=[(4,), (4,), (0,), (0,)]
    l29=[(5,), (5,)]
    L28=[]
    L28=L28+concat([(0,)],wedge2(l28))
    L28=L28+[(2,0)]
    
    L29=[]
    L29=L29+concat([(0,)],wedge2(l29))
    L29=L29+[(2,0)]

    basisTemp=[[(0)]]
    basisTemp.append(l)
    print("Conjugate to case 28?")
    print(classifyIncomplete(L28,basisTemp,orderList2))
    if len(classifyIncomplete(L28,basisTemp,orderList2))>1:
        print("YES")
    print("Conjugate to case 29?")
    print(classifyIncomplete(L29,basisTemp,orderList2))
    if len(classifyIncomplete(L29,basisTemp,orderList2))>1:
        print("YES")

    








#A12 in D6


lambda1=[[(0)]]
lambda2=[[(0)]]
lambda5=[[(0)]]
Lie=[[(0)]]
LieA13=[[(0)]]

for i in range(0,70):
    lambda1.append([(0)])
    lambda2.append([(0)])
    lambda5.append([(0)])
    Lie.append([(0)])
    LieA13.append([(0)])

        
lambda1[1]=expand("[ (2,2)/(2,0)]")
lambda5[1]=expand("[(4, 1)/(2,1)/(2, 3)/(0,3) ]")



lambda1[2]=expand("[(8,0)/(0,2)]")
lambda5[2]=expand("[ (10,1)/(4,1)]")



lambda1[3]=expand("[(3,1)/(1,1)]")
lambda5[3]=expand("[(5,0)/(3,0)/(1,2)/(3,2)/(3,0) ]")


lambda1[4]=expand("[(3,1)/(1,1)]")
lambda5[4]=expand("[(4,1)^2/(2,1)/(0,3)/(0,1) ]")


lambda1[5]=expand("[(3,1)/(1,0)^2]")
lambda5[5]=expand("[(4,1)/(2,1)/(4,0)^2/(0,2)^2]")


lambda1[6]=expand("[(3,1)/(1,0)^2]")
lambda5[6]=expand("[ (5,0)/(3,0)/(1,2)/(3,1)^2 ]")


lambda1[7]=expand("[ (3,1)/(0,1)^2]")
lambda5[7]=expand("[(4,1)/(0,3)/(0,1)/(3,1)^2 ]")


lambda1[8]=expand("[(3,1)/(0,1)^2]")
lambda5[8]=expand("[ (3,2)/(3,0)/(4,0)^2/(0,2)^2]")


lambda1[9]=expand("[(3,0)^2/(1,1)]")
lambda5[9]=expand("[  (5,0)/(1,0)^3/(3,1)^2/(3,0)]")



lambda1[10]=expand("[ (3,0)^2/(0,1)^2]")
lambda5[10]=expand("[(3,1)^2/(4,0)^2/(0,0)^6 ]")



lambda1[11]=expand("[ (3,1)/(2,0)/(0,0)]")
lambda5[11]=expand("[(5,0)/(3,0)/(1,2)/(4,1)/(2,1) ]")



lambda1[12]=expand("[ (3,1)/(0,2)/(0,0)]")
lambda5[12]=expand("[ (3,2)/(3,0)/(4,1)/(0,3)/(0,1)]")




lambda1[13]=expand("[ (3,0)^2/(0,2)/(0,0)]")
lambda5[13]=expand("[ (3,1)^2/(4,1)/(0,1)^3]")




lambda1[14]=expand("[ (3,1)/(0,0)^4]")
lambda5[14]=expand("[ (3,1)^2/(4,0)^2/(0,2)^2]")



lambda1[15]=expand("[ (6,0)/(0,4)]")
lambda5[15]=expand("[ (6,3)/(0,3)]")



lambda1[16]=expand("[  (6,0)/(1,1)/(0,0)]")
lambda5[16]=expand("[ (7,0)/(6,1)/(5,0)/(1,0)/(0,1)]")




lambda1[17]=expand("[ (6,0)/(0,1)^2/(0,0)]")
lambda5[17]=expand("[ (6,1)/(6,0)^2/(0,1)/(0,0)^2]")



lambda1[18]=expand("[ (6,0)/(0,2)/(0,0)^2]")
lambda5[18]=expand("[ (6,1)^2/(0,1)^2]")



lambda1[19]=expand("[ (4,0)/(0,4)/(0,0)^2]")
lambda5[19]=expand("[ (3,3)^2]")




lambda1[20]=expand("[ (4,0)/(1,1)/(2,0)]")
lambda5[20]=expand("[ (4,1)/(2,1)/(5,0)/(3,0)^2/(1,0)]")





lambda1[21]=expand("[ (4,0)/(1,1)/(0,2)]")
lambda5[21]=expand("[ (4,1)/(2,1)/(3,2)/(3,0)]")



lambda1[22]=expand("[ (4,0)/(0,1)^2/(2,0)]")
lambda5[22]=expand("[ (4,1)/(2,1)/(4,0)^2/(2,0)^2]")


lambda1[23]=expand("[  (4,0)/(0,1)^2/(0,2)]")
lambda5[23]=expand("[ (3,2)/(3,0)/(3,1)^2]")


lambda1[24]=expand("[  (4,0)/(1,0)^2/(0,2)]")
lambda5[24]=expand("[ (4,1)/(2,1)/(3,1)^2]")


lambda1[25]=expand("[ (4,0)/(1,1)/(0,0)^3]")
lambda5[25]=expand("[ (4,0)^2/(2,0)^2/(3,1)^2]")



lambda1[26]=expand("[  (4,0)/(0,1)^2/(0,0)^3]")
lambda5[26]=expand("[ (3,1)^2/(3,0)^4]")


lambda1[27]=expand("[ (4,0)/(0,2)^2/(0,0)]")
lambda5[27]=expand("[ (3,2)^2/(3,0)^2]")


lambda1[28]=expand("[ (4,0)/(0,2)/(2,0)/(0,0)]")
lambda5[28]=expand("[ (4,1)^2/(2,1)^2]")


lambda1[29]=expand("[ (4,0)/(0,2)/(0,0)^4]")
lambda5[29]=expand("[ (3,1)^4]")



lambda1[30]=expand("[ (1,1)^3]")
lambda5[30]=expand("[ (2,1)^3/(0,1)^5/(0,3)]")


lambda1[31]=expand("[  (1,1)^2/(0,1)^2]")
lambda5[31]=expand("[ (2,1)/(0,1)/(1,1)^4/(0,3)/(0,1)^2]")


lambda1[32]=expand("[ (1,1)^2/(0,1)^2]")
lambda5[32]=expand("[ (2,0)^2/(0,0)^4/(1,2)^2/(1,0)^2/(0,2)^2]")


lambda1[33]=expand("[ (1,1)/(0,1)^4]")
lambda5[33]=expand("[ (1,1)^4/(0,1)^4/(0,3)/(0,1)^2]")


lambda1[34]=expand("[ (1,1)/(0,1)^2/(1,0)^2]")
lambda5[34]=expand("[ (2,0)^2/(0,0)^2/(1,1)^2/(1,2)/(1,0)/(0,1)^4]")




lambda1[35]=expand("[ (1,0)^4/(0,1)^2]")
lambda5[35]=expand("[ (2,0)^2/(0,0)^2/(1,1)^4/(0,0)^8]")





lambda1[36]=expand("[ (1,1)^2/(0,0)^4]")
lambda5[36]=expand("[ (2,0)^2/(0,0)^4/(1,1)^4/(0,2)^2]")



lambda1[37]=expand("[ (1,1)/(1,0)^2/(0,0)^4]")
lambda5[37]=expand("[ (2,0)^2/(0,0)^2/(1,0)^4/(1,1)^2/(0,1)^4]")




lambda1[38]=expand("[ (1,0)^2/(0,1)^2/(0,0)^4]")
lambda5[38]=expand("[ (0,1)^4/(0,0)^8/(1,1)^2/(1,0)^4]")




lambda1[39]=expand("[  (1,1)/(0,0)^8]")
lambda5[39]=expand("[ (1,0)^8/(0,1)^8]")





lambda1[40]=expand("[ (1,1)/(0,2)^2/(0,0)^2]")
lambda5[40]=expand("[ (1,2)^2/(1,0)^2/(0,3)^2/(0,1)^4]")




lambda1[41]=expand("[(1,1)/(2,0)/(0,2)/(0,0)^2]")
lambda5[41]=expand("[ (2,1)^2/(0,1)^2/(1,2)^2/(1,0)^2)]")




lambda1[42]=expand("[ (1,0)^2/(2,0)/(0,2)/(0,0)^2]")
lambda5[42]=expand("[ (1,1)^4/(2,1)^2/(0,1)^2]")





lambda1[43]=expand("[(1,0)^2/(0,2)^2/(0,0)^2]")
lambda5[43]=expand("[ (1,2)^2/(1,0)^2/(0,2)^4/(0,0)^4]")




lambda1[44]=expand("[(1,1)/(2,0)/(0,0)^5]")
lambda5[44]=expand("[ (1,1)^4/(2,0)^4/(0,0)^4]")






 
lambda1[45]=expand("[(1,0)^2/(0,2)/(0,0)^5]")
lambda5[45]=expand("[ (1,1)^4/(0,1)^8]")







lambda1[46]=expand("[ (2,0)^3/(0,2)]")
lambda5[46]=expand("[ (3,1)^2/(1,1)^4]")



lambda1[47]=expand("[(2,0)^2/(0,2)^2]")
lambda5[47]=expand("[ (2,2)^2/(2,0)^2/(0,2)^2/(0,0)^2]")



lambda1[48]=expand("[(2,0)^2/(0,2)/(0,0)^3]")
lambda5[48]=expand("[ (2,1)^4/(0,1)^4]")




lambda1[49]=expand("[(2,0)/(0,2)/(0,0)^6]")
lambda5[49]=expand("[ (1,1)^8]")




lambda1[50]=expand("[(1,1)/(2,0)/(0,1)^2/(0,0)]")
lambda5[50]=expand("[ (1,1)^2/(1,2)/(1,0)/(2,1)/(0,1)/(2,0)^2/(0,0)^2]")




lambda1[51]=expand("[(0,2)/(1,0)^2/(0,1)^2/(0,0)]")
lambda5[51]=expand("[ (1,1)^2/(1,2)/(1,0)/(0,2)^2/(0,0)^2/(0,1)^4]")



lambda1[52]=expand("[(1,1)/(2,0)(1,0)^2/(0,0)]")
lambda5[52]=expand("[ (1,1)^2/(2,1)/(0,1)/(3,0)/(1,0)^2/(2,0)^2/(0,0)^2]")



lambda1[53]=expand("[(1,1)^2/(2,0)(0,0)]")
lambda5[53]=expand("[ (3,0)/(1,0)^2/(2,1)^2/(0,1)^2/(1,2)/(1,0)]")


lambda1[54]=expand("[(1,0)^4/(0,2)/(0,0)]")
lambda5[54]=expand("[ (2,1)/(0,1)/(1,1)^4/(0,1)^4]")


lambda1[55]=expand("[(2,1)^2]")
lambda5[55]=expand("[ (2,2)^2/(0,0)^4/(4,0)^2]")


lambda1[56]=expand("[(5,1)]")
lambda5[56]=expand("[ (8,1)/(4,1)/(0,3)]")


lambda1[57]=expand("[(2,2)/(0,0)^3]")
lambda5[57]=expand("[ (3,1)^2/(1,3)^2]")







###Additional
##
###this is case 9
##lambda1[58]=expand("[(3,0)^2/(1,1)]")
##lambda5[58]=expand("[ (4,0)^2/(2,0)^2/(4,1)/(0,1)^3]")
##
###case 10
##lambda1[59]=expand("[ (3,0)^2/(0,1)^2]")
##lambda5[59]=expand("[ (4,1)/(0,1)^3/(3,0)^4]")
##
###this is case 30
##lambda1[60]=expand("[ (1,1)^3]")
##lambda5[60]=expand("[(3,0)/(1,2)^3/(1,0)^5 ]")
##
###This is case 33
##lambda1[61]=expand("[ (1,1)/(0,1)^4]")
##lambda5[61]=expand("[(1,0)^4/(1,2)/(1,0)/(0,2)^4/(0,0)^4 ]")
##
###This is case 34
##lambda1[62]=expand("[ (1,1)/(0,1)^2/(1,0)^2]")
##lambda5[62]=expand("[(2,1)/(0,1)/(1,0)^4/(1,1)^2/(0,2)^2/(0,0)^2]")
##
##
###This is case 35
##lambda1[63]=expand("[ (1,0)^4/(0,1)^2]")
##lambda5[63]=expand("[(2,1)/(0,1)/(1,0)^8/(0,1)^4 ]")




for i in range(1,58):
    lambda2[i]=wedge2(lambda1[i])



for i in range(1,58):
    Lie[i]=[]
    Lie[i]=Lie[i]+lambda2[i]
    Lie[i]=Lie[i]+lambda5[i]
    Lie[i]=Lie[i]+lambda5[i]
    Lie[i]=Lie[i]+[(0,0),(0,0),(0,0)]
   #p=str(i)
   #p=p+" & "+latex(lambda1[i])+" & "+latex(Lie[i])+"   &   "+ str(checker(Lie[i],basisA12,orderList2))+" \\\\ "
    #print(p)
    #print("&&  $ $  &\\\\ \\hline")

for i in range(1,58):
#    print("//////////////////////")
#    print(i)
#    print(latex(lambda1[i]))
#    print(checker(Lie[i],basisA12,orderList2))
    if checker(Lie[i],basisA12,orderList2)==-1:
#        print("We add it to the list with index: ")
        basisA12.append(Lie[i])
        basisA12Lambda1.append(lambda1[i])
#        print(checker(Lie[i],basisA12,orderList2))



#Building the latex of table A12inE7
end=len(basisA12)
end=30
for i in range(30,end):
    p=str(i)+" & $A_1D_6$ & $(0,"+ latexWithoutDollar(basisA12Lambda1[i])+")$ & "+latex(basisA12[i])+" \\\\ "
    print(p)
    print("&&& $ $ \\\\ \\hline")




#A12 in A1D6 with diagonal

for i in range(1,58):
    LieA13[i]=[]
    LieA13[i]=LieA13[i]+concat([(0,)],lambda2[i])
    LieA13[i]=LieA13[i]+concat([(1,)],lambda5[i])
    LieA13[i]=LieA13[i]+[(2,0,0)]

for i in range(1,58):
    for j in range(2,4):
        temp=diagA1(LieA13[i],1,j)
        conjugate = checker(temp,basisA12,orderList2)
        #print("/////////////////////////////////////////////////////////")
        #print(str(i)+"   ----->   "+str(conjugate))
        #print(latex(lambda1[i]))
        if conjugate==-1:
        #    print("add new element tensor with "+str(j)+":")
        #    print(latex(lambda1[i]))
            basisA12.append(temp)
        #    print("new nb: "+str(checker(temp,basisA12,orderList2)))
#            print(str(checker(temp,basisA12,orderList2))+"&$A_1D_6$ & $(\\underline{1},"+latexWithoutDollar(lambda1[i])+" )$ & " +latex(temp)+" \\\\ ")
#            print("&&& $ $ \\\\ \\hline")







end=58
end=1
for i in range(1,end):
    for j in range(2,4):
        temp=diagA1(LieA13[i],1,j)
        #print("////////////////////")
        #print(latex(lambda1[i]))
        lat=latexWithoutDollar(lambda1[i])
        t=""
        index=0
        if j==2:
            line=str(i)+"&(i)&"
            while index<len(lat):
                if lat[index]!='(':
                    t=t+lat[index]
                    index = index+1
                else:
                    
                    t=t+"(\\underline{"
                    t=t+lat[index+1]
                    t=t+"}"
                    index=index+2
            t="( \\underline{1}, "+t +")"
        if j==3:
            line="&(ii)&"
            while index<len(lat):
                if lat[index]!=',':
                    t=t+lat[index]
                    index = index+1
                else:
                    t=t+",\\underline{"
                    t=t+lat[index+2]
                    t=t+"}"
                    index=index+3
            t="( \\underline{1}, "+t +")"
        conjugate = checker(temp,basisA12,orderList2)
        counter=0
        temp=latexWithoutDollar(temp)
        power=0
        temp2=""
        while power<len(temp):
            if temp[power]!="^":
                temp2=temp2+temp[power]
                power=power+1
            else:
                if temp[power+2]=="/":
                    temp2=temp2+temp[power]
                    power=power+1
                else:
                    temp2=temp2+"^{"+temp[power+1]+temp[power+2]+"}"
                    power=power+3
                

        temp=temp2
        temp1=""
        temp2=""
        for index in range(0,len(temp)):
            if counter<8:
                temp1=temp1+temp[index]
            else:
                temp2=temp2+temp[index]
            
            if temp[index]=="/":
                counter = counter+1
        
        

        t1=""
        t2=""
        counter=0
        for index in range(0,len(t)):
            if counter<2:
                t1=t1+t[index]
            else:
                t2=t2+t[index]
            
            if t[index]=="/":
                counter = counter+1
                
                
            
        
        if conjugate==-1:
            conjugate = "none"
        else:
            conjugate= str(conjugate)
        line = line+"$"+t1+"$ & $"+temp1+"$ & "+ conjugate +"\\\\ "
        print(line)
        print("&& $"+t2+"$ & $"+temp2+"$ & \\\\ \\hline ")
        
        
#print(len(basisA12))
























#A12 in A2A5
print("A12 in A2A5")


#In A5
print("A12 in A5")
lambda1=[[(0)]]
lambda2=[[(0)]]
l=[[(0)]]

lambda1.append([(2,1)])
lambda1.append([(1,1),(1,0)])
lambda1.append([(1,1),(0,0),(0,0)])
lambda1.append([(3,0),(0,1)])
lambda1.append([(2,0),(0,2)])
lambda1.append([(2,0),(0,1),(0,0)])
lambda1.append([(1,0),(1,0),(0,1)])
lambda1.append([(1,0),(0,1),(0,0),(0,0)])

for i in range(1,len(lambda1)):
    lambda2.append(wedge2(lambda1[i]))
    l.append(tensor(lambda1[i], lambda1[i]))
    l[i].remove((0,0))

for i in range(1,len(lambda1)):
    Lie[i]=l[i]
    for j in range(0,6):
        Lie[i]=Lie[i]+lambda2[i]
    for j in range(0,8):
        Lie[i]=Lie[i]+[(0,0)]

for i in range(1,len(lambda1)):
    conjugate = checker(Lie[i], basisA12,orderList2)
#    p=str(i)+" & "+latex(lambda1[i])+" & "+latex(Lie[i])+" & "+str(conjugate )+"\\\\ \\hline"
#    print(p)




print("A12 in A2A5 with diag:")

Lie1=[0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,0]
Lie2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,len(lambda1)):
    Lie1[i]=concat([(0,)],l[i])
    Lie2[i]=concat([(0,)],l[i])
    
    Lie1[i]=Lie1[i]+concat([(1,),(0,)],lambda2[i])
    Lie1[i]=Lie1[i]+concat([(1,),(0,)],lambda2[i])
    Lie1[i]=Lie1[i]+concat([(2,),(1,),(1,),(0,)],[(0,0)])

    Lie2[i]=Lie2[i]+concat([(2,)],lambda2[i])
    Lie2[i]=Lie2[i]+concat([(2,)],lambda2[i])
    Lie2[i]=Lie2[i]+concat([(4,),(2,)],[(0,0)])

L1diag1=[0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,0]
L1diag2=[0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,0]
L2diag1=[0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,0]
L2diag2=[0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,0]
for i in range(1,len(lambda1)):
    #print(latex(Lie1[i]))
    L1diag1[i]=diagA1(Lie1[i],1,2)
    L1diag2[i]=diagA1(Lie1[i],1,3)

    #p1diag1=str(i*4-3)+"& $(\\underline{1+0},"+latexWithoutDollar(lambda1[i])+")$&"+latex(L1diag1[i])+"&"+str(checker(L1diag1[i],basisA12,orderList2))+"\\\\ "
    p1diag2=str(i*4-2)+"&$(\\underline{1+0},"+latexWithoutDollar(lambda1[i])+")$&"+latex(L1diag2[i])+"&"+str(checker(L1diag2[i],basisA12,orderList2))+"\\\\ "

    p1diag1l1=str(i*4-3)+"& $(\\underline{1+0},"+latexWithoutDollar(lambda1[i])+")$& $"
    p1diag1l2="&& $"
    counter = 0
    index=0
    lat1=latexWithoutDollar(L1diag1[i])
    while counter<7 and index<len(lat1):
        p1diag1l1=p1diag1l1+lat1[index]
        if lat1[index]=="/":
            counter=counter+1
        index=index+1
    p1diag1l2="&& $"
    while index<len(lat1)-1:
        p1diag1l2=p1diag1l2+lat1[index]
        index=index+1
        
    p1diag1l2=p1diag1l2+"$& \\\\ \\hline"
    p1diag1l1=p1diag1l1+"$&"+str(checker(L1diag1[i],basisA12,orderList2))+"\\\\ "
    
   # print(p1diag1l1)
   # print(p1diag1l2)
    #print(p1diag2)
    #print("&&& $$ \\\\ \\hline")


    p2diag1l1=str(i*4-2)+"& $(\\underline{1+0},"+latexWithoutDollar(lambda1[i])+")$& $"
    p2diag1l2="&& $"
    counter = 0
    index=0
    lat1=latexWithoutDollar(L1diag2[i])
    while counter<7 and index<len(lat1):
        p2diag1l1=p2diag1l1+lat1[index]
        if lat1[index]=="/":
            counter=counter+1
        index=index+1
    p2diag1l2="&& $"
    while index<len(lat1)-1:
        p2diag1l2=p2diag1l2+lat1[index]
        index=index+1
        
    p2diag1l2=p2diag1l2+"$& \\\\ \\hline"
    p2diag1l1=p2diag1l1+"$&"+str(checker(L1diag2[i],basisA12,orderList2))+"\\\\ "
    
  #  print(p2diag1l1)
 #   print(p2diag1l2)




    L2diag1[i]=diagA1(Lie2[i],1,2)
    L2diag2[i]=diagA1(Lie2[i],1,3)

    p2diag1=str(i*4-1)+"& $(\\underline{2},"+latexWithoutDollar(lambda1[i])+")$&"+latex(L2diag1[i])+"&"+str(checker(L2diag1[i],basisA12,orderList2))+"\\\\ "
    p2diag2=str(i*4-0)+"&$(\\underline{2},"+latexWithoutDollar(lambda1[i])+")$&"+latex(L2diag2[i])+"&"+str(checker(L2diag2[i],basisA12,orderList2))+"\\\\ "
#    print(p2diag1)
#    print("&&& $$ \\\\ \\hline")
#    print(p2diag2)
#    print("&&& $$ \\\\ \\hline")
    


















print("In A2A5 with an A1 in A2 and one in A5")
lambda1=[[(0)]]
lambda2=[[(0)]]
l=[[(0)]]

lambda1.append([(5,)])
lambda1.append([(4,),(0,)])
lambda1.append([(3,),(1,)])
lambda1.append([(3,),(0,),(0,)])
lambda1.append([(2,),(2,)])
lambda1.append([(2,),(1,),(0,)])
lambda1.append([(2,),(0,),(0,),(0,)])
lambda1.append([(1,),(1,),(1,)])
lambda1.append([(1,),(1,),(0,),(0,)])
lambda1.append([(1,),(0,),(0,),(0,),(0,)])

    
for i in range(1,len(lambda1)):
    lambda2.append(wedge2(lambda1[i]))
    l.append(tensor(lambda1[i], lambda1[i]))
    temp=[]
    for j in range(0,len(l[i])):
        temp.append((l[i][j],))
    l[i]=temp   
    l[i].remove((0,))
    
Lie1=[0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,0]
Lie2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,len(lambda1)):
    Lie1[i]=concat([(0,)],l[i])
    Lie2[i]=concat([(0,)],l[i])
    
    Lie1[i]=Lie1[i]+concat([(1,),(0,)],lambda2[i])
    Lie1[i]=Lie1[i]+concat([(1,),(0,)],lambda2[i])
    Lie1[i]=Lie1[i]+concat([(2,),(1,),(1,),(0,)],[(0,)])

    Lie2[i]=Lie2[i]+concat([(2,)],lambda2[i])
    Lie2[i]=Lie2[i]+concat([(2,)],lambda2[i])
    Lie2[i]=Lie2[i]+concat([(4,),(2,)],[(0,)])

    c1=checker(Lie1[i],basisA12,orderList2)
    c2=checker(Lie2[i],basisA12,orderList2)
    if c1==-1:
        basisA12.append(Lie1[i])
    if c2==-1:
        basisA12.append(Lie2[i])


for i in range(1,len(lambda1)):
    latL1=latex(lambda1[i])
    done=""
    for j in range(0,len(latL1)):
        if latL1[j]!="(" and latL1[j]!=")" and latL1[j]!=",":
            done=done+latL1[j]
    
    l1p1=str(2*i-1)+"& "+done +" & $1+0$ &$ "
    counter = 0
    index=0
    lat1=latexWithoutDollar(Lie1[i])
    while counter<7 and index<len(lat1):
        l1p1=l1p1+lat1[index]
        if lat1[index]=="/":
            counter=counter+1
        index=index+1
    l2p1="&&& $"
    while index<len(lat1)-1:
        l2p1=l2p1+lat1[index]
        index=index+1
        
    l2p1=l2p1+"$& \\\\ \\hline"
    l1p1=l1p1+"$"


    l1p2=str(2*i)+"& "+done +" & $2$ &$ "
    counter = 0
    index=0
    lat2=latexWithoutDollar(Lie2[i])
    while counter<7 and index<len(lat2):
        l1p2=l1p2+lat2[index]
        if lat2[index]=="/":
            counter=counter+1
        index=index+1
    l2p2="&&& $"
    while index<len(lat2)-1:
        l2p2=l2p2+lat2[index]
        index=index+1
        
    l2p2=l2p2+"$& \\\\ \\hline"
    l1p2=l1p2+"$"
    
        
   # p2=str(2*i)+"& "+done +" & $2$ &" +latex(Lie2[i])+"\\\\"
    l1p1=l1p1+"&"+str(checker(Lie1[i],basisA12,orderList2))+"\\\\"
    l1p2=l1p2+"&"+str(checker(Lie2[i],basisA12,orderList2))+"\\\\"
   
   # print(l1p1)
   # print(l2p1)
   # print(l1p2)
   # print(l2p2)














#In   A7
print("In A7")
lambda1=[(0)]
lambda1.append(expand("[(1,3)]"))
lambda1.append(expand("[(1,2)/(0,1)]"))
lambda1.append(expand("[(1,2)/(1,0)]"))
lambda1.append(expand("[(1,2)/(0,0)^2]"))
lambda1.append(expand("[(5,0)/(0,1)]"))
lambda1.append(expand("[(4,0)/(0,2)]"))
lambda1.append(expand("[(4,0)/(0,1)/(0,0)]"))
lambda1.append(expand("[(3,0)/(0,3)]"))
lambda1.append(expand("[(3,0)/(1,1)]"))
lambda1.append(expand("[(3,0)/(0,2)/(0,0)]"))
lambda1.append(expand("[(3,0)/(1,0)/(0,1)]"))
lambda1.append(expand("[(3,0)/(0,1)^2]"))
lambda1.append(expand("[(3,0)/(0,1)/(0,0)^2]"))
lambda1.append(expand("[(1,1)^2]"))
lambda1.append(expand("[(1,1)/(0,0)^4]"))
lambda1.append(expand("[(1,1)/(0,2)/(0,0)]"))
lambda1.append(expand("[(1,1)/(0,1)^2]"))
lambda1.append(expand("[(1,1)/(1,0)/(0,1)]"))
lambda1.append(expand("[(1,1)/(0,1)/(0,0)^2]"))
lambda1.append(expand("[(2,0)/(0,2)/(0,1)]"))
lambda1.append(expand("[(2,0)/(0,2)/(0,0)^2]"))
lambda1.append(expand("[(2,0)/(0,1)^2/(0,0)]"))
lambda1.append(expand("[(2,0)/(0,1)/(0,0)^3]"))
lambda1.append(expand("[(2,0)/(1,0)/(0,1)/(0,0)]"))
lambda1.append(expand("[(1,0)^3/(0,1)]"))
lambda1.append(expand("[(1,0)^2/(0,1)^2]"))
lambda1.append(expand("[(1,0)^2/(0,1)/(0,0)^2]"))
lambda1.append(expand("[(1,0)/(0,1)/(0,0)^4]"))

LieA7=[(0)]
for i in range(1,len(lambda1)):
    #print("/////////////////////////////////////")
    #print(latex(lambda1[i]))
    l=tensor(lambda1[i],lambda1[i])
    l.remove((0,0))
    l4=wedge4(lambda1[i])
    #print(dimChecker(l4))
    #print(dimChecker(l))


#PROBLEM!!!!!!!
    #print(latex(l4))
    lie=l+l4
    LieA7.append(lie)
    #print(dimChecker(LieA7[i]))
    #print(latex(LieA7[i]))

for i in range(1,len(lambda1)):
    lat=latexWithoutDollar(LieA7[i])
    p1=str(i)+"&"+latex(lambda1[i])+"& $"
    p2="&& $"
    counter=0
    index=0
    while counter<8 and index<len(lat):
        p1=p1+lat[index]
        
        if lat[index]=="/":
            counter=counter+1
        index=index+1
    while index<len(lat):
        p2=p2+lat[index]
        index=index+1


    p1=p1+" $&"+str(checker(LieA7[i],basisA12,orderList2))+" \\\\ "
    p2=p2+"$ & \\\\ \\hline"
    
    #if p2!="&& $$ & \\\\ \\hline":
        #print(p1)
        #print(p2)
   # else:
        
        #print(p1+ "\\hline")
    #print("/////////////////////////////////////")
    #print(latex(lambda1[i]))
    #print(checker(LieA7[i],basisA12,orderList2))


#print("Case2:")
#print(latex(lambda1[2]))
#print(classifyIncomplete(l4[2],basisA12,orderList2))

basisA12.append(expand("[(2, 4)/(2, 2)^3/(2, 0)/(0, 4)^3/(0, 2)^2/(1, 3)^4/(1, 1)^3/(0, 0)^3/(1, 5)/(3, 1)]"))
basisA12.append(expand("[(2, 4)/(2, 2)^3/(2, 0)/(0, 4)^3/(0, 2)/(1, 2)^6/(0, 0)^6/(1, 4)^2/ (3, 0)^2]"))

 
#In A1G2
print("in A1G2")

a=expand("[(0,2)^5/(1,1)^5/(0,4)^3/(1,3)^3/(2,2)^3/(1,1)^3/(0,0)^6/(1,3)/(2,0)/(0,2)]")


b=expand("[(4,2)/(5,1)/(3,1)/(2,4)/(3,3)/(1,3)/(4,2)/(2,2)/(0,2)/(3,1)/(1,1)/(2,0)^2/(1,3)/(2,0)/(0,2)]")

c=expand("[(6,0)^2/(4,0)^2/(2,0)^2/(5,1)^2/(3,1)^3/(1,1)^2/(4,2)/(2,2)/(0,2)/(2,0)^2/(3,1)/(0,2)/(2,0)]")
#print(checker(a,basisA12,orderList2))        

#print(checker(b,basisA12,orderList2))        

#print(checker(c,basisA12,orderList2))        

basisA12.append(expand("[(2,8)/(4,6)/(6,4)/(2,4)/(4,2)/(2,0)/(0,2)]"))


print("one A1 in A1 and one in G2")
lambda1=[(0)]
lambda2=[(0)]
s2=[(0)]
lie=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lambda1.append(expand("[(1,)^2/(0,)^3]"))
lambda1.append(expand("[(2,)/(1,)^2]"))
lambda1.append(expand("[(6,)]"))
lambda1.append(expand("[(2,)^2/(0,)]"))

lambda2.append(expand("[(2,)/(1,)^4/(0,)^3]"))
lambda2.append(expand("[(3,)^2/(2,)/(0,)^3]"))
lambda2.append(expand("[(10,)/(2,)]"))
lambda2.append(expand("[(4,)/(2,)^3]"))

s2.append(expand("[(2,)^3/(0,)^6/(1,)^6]"))
s2.append(expand("[(4,)/(0,)/(3,)^2/(1,)^2/(2,)^3]"))
s2.append(expand("[(12,)/(8,)/(4,)]"))
s2.append(expand("[(4,)^3/(0,)^3/(2,)^3]"))

#for i in range(1,len(lambda1)):
#    s2.append(S2(lambda1[i]))
    

for i in range(1, len(lambda1)):
    lie[i]=concat([(4,)],lambda1[i])+concat([(2,)],s2[i])
    lie[i]=lie[i]+[(2,0)]
    lie[i]=lie[i]+concat([(0,)],lambda2[i])
    #print("///////////////")
    #print(latex(lambda1[i]))
    #print(dimChecker(lie[i]))
    #print(latex(lie[i]))
    #print(checker(lie[i],basisA12,orderList2))
    
basisA12.append(expand("[(4, 6)/(2, 12)/(2, 8)/(2, 4)/(2, 0)/(0, 10)/(0, 2)]"))











#In G2C3
print("In G2")
a=expand("[(2,0)/(0,2)/(1,3)/(0,2)^9/(0,2)^5/(1,1)^9/(1,1)^5/(0,0)^9/(0,0)^9/(0,0)^3]")
print(checker(a,basisA12,orderList2))
print(dimChecker(a))
basisA12.append(a)

#InC3
print("in C3")
b=expand("[(6,0)/(2,0)/(3,1)/(4,0)^4/(0,0)^4/(3,1)^4/(4,0)^3/(3,1)^3/(0,2)/(0,0)^3/(0,0)^8/(0,0)^6]")


c=expand("[(2,0)/(4,2)/(0,2)/(4,0)^4/(2,2)^4/(4,0)^3/(2,2)^3/(0,0)^3/(0,0)^8/(0,0)^3]")


d=expand("[(2,0)^3/(0,2)/(1,1)^2/(2,0)^4/(1,1)^8/(2,0)^3/(1,1)^6/(0,0)^3/(0,0)^9/(0,0)^9/(0,0)^6/(0,0)^9]")


e=expand("[(2,0)/(0,2)/(1,1)^4/(1,0)^8/(0,1)^8/(1,1)^4/(1,0)^8/(0,0)^8/(0,0)^8/(0,1)^8/(0,0)^3/(0,0)^9/(0,0)^3]")


##print(checker(b,basisA12,orderList2))
##print(dimChecker(b))
##
##print(checker(c,basisA12,orderList2))
##print(dimChecker(c))
##
##print(checker(d,basisA12,orderList2))
##print(dimChecker(d))
##
##print(checker(e,basisA12,orderList2))
##print(dimChecker(e))



#One in each#
print("One in each")
l1G2=[(0)]
l2G2=[(0)]
l1C3=[(0)]
l2C3=[(0)]
S2C3=[(0)]
lie=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

l1G2.append(expand("[(1,)^2/(0,)^3]"))
l1G2.append(expand("[(2,)/(1,)^2]"))
l1G2.append(expand("[(6,)]"))
l1G2.append(expand("[(2,)^2/(0,)]"))

l2G2.append(expand("[(2,)/(1,)^4/(0,)^3]"))
l2G2.append(expand("[(3,)^2/(2,)/(0,)^3]"))
l2G2.append(expand("[(10,)/(2,)]"))
l2G2.append(expand("[(4,)/(2,)^3]"))


l1C3.append(expand("[(5,)]"))
l1C3.append(expand("[(3,)/(0,)^2]"))
l1C3.append(expand("[(3,)/(1,)]"))
l1C3.append(expand("[(2,)^2]"))
l1C3.append(expand("[(1,)^3]"))
l1C3.append(expand("[(1,)^2/(0,)^2]"))
l1C3.append(expand("[(1,)/(0,)^4]"))


for i in range(1,len(l1C3)):
    a=wedge2(l1C3[i])
    a.remove((0,))
    l2C3.append(a)

for i in range(1,len(l1C3)):
    S2C3.append(S2(l1C3[i]))
   
index=1
for i in range(1,len(l1C3)):
    for j in range(1,len(l1G2)):
        lie[index]=concat(l1G2[j],l2C3[i])
        lie[index]=lie[index]+concat([(0,)],S2C3[i])
        lie[index]=lie[index]+concat(l2G2[j],[(0,)])
        #print(dimChecker(lie[index]))
        n=checker(lie[index],basisA12,orderList2)
        pl1C3=""
        temp= latex(l1C3[i])
        for t in range(0,len(temp)):
            if temp[t] != "(" and temp[t] != ")" and temp[t] != ",":
                pl1C3=pl1C3+temp[t]
        pl1G2=""
        temp= latex(l1G2[j])
        for t in range(0,len(temp)):
            if temp[t] != "(" and temp[t] != ")" and temp[t] != ",":
                pl1G2=pl1G2+temp[t]
        
        p1=str(index)+"&"+pl1C3+"&"+pl1G2+"& $"
        p2="&&& $"
        temp=latexWithoutDollar(lie[index])
        ind=0
        counter =0

        while ind<len(temp) and counter<7:
            p1=p1+temp[ind]
            if temp[ind]=="/":
                counter=counter+1
            ind=ind+1
        while ind<len(temp):
            p2=p2+temp[ind]
            ind=ind+1

        p1=p1+"$&"+str(n)+"\\\\ "
        p2=p2+"$ &\\\\ \\hline"
        print(p1)
        print(p2)
        index=index+1
        


a=expand("[(10,0)/(10,0)/(8,0)/(6,0)/(4,0)/(2,0)/(8,2)/(6,2)/(4,2)/(4,2)/(2,0)/(2,0)/(0,2)]")
print(dimChecker(a))
print(checker(a,basisA12,orderList2))
basisA12.append(a)

a=expand("[(10,0)/(6,4)/(8,2)/(6,2)/(4,2)/(2,4)/(2,0)/(0,2)/(2,0) ]")
print(dimChecker(a))
print(checker(a,basisA12,orderList2))
basisA12.append(a)

print(len(basisA12))







#In A1F4
print("In F_4")

test=[(0)]
test.append(expand("[(0,10)/(1,9)/(0,6)/(1,3)/(2,0)/(0,2)]"))


test.append(expand("[(0,6)/(1,5)/(0,4)/(1,3)^2/(2,0)/(0,2)^3]"))

test.append(expand("[(0,6)/(1,4)^2/(1,3)/(0,3)^2/(2,0)/(0,2)/(0,0)^3]"))
            
test.append(expand("[(1,4)^2/(0,4)^3/(2,0)/(0,2)/(1,0)^4/(0,0)^3]"))

test.append(expand("[(1,3)/(2,0)/(0,2)^6/(1,1)^5/(0,0)^3]"))

test.append(expand("[(1,2)^2/(2,0)/(0,2)^3/(1,1)^2/(1,0)^4/(0,1)^4/(0,0)^4]"))


test.append(expand("[(2,0)/(0,2)/(1,1)^5/(1,0)^4/(0,1)^4/(0,0)^9/(0,0)]"))

test.append(expand("[(4,1)^2/(4,2)/(0,3)^2/(2,0)/(0,2)/(0,0)^3]"))

test.append(expand("[(2,2)/(2,0)^4/(0,2)^4/(1,1)^4/(0,0)^3]"))

test.append(expand("[(5,1)/(4,2)/(3,1)/(1,3)/(2,0)^2/(0,2)]"))


test.append(expand("[(2,4)^2/(4,0)/(0,4)/(2,0)^3/(0,2)]"))

test.append(expand("[ (0,6)/(2,4)/(0,4)/(1,3)^2/(2,0)^2/(0,2)]"))

test.append(expand("[(4,2)/(2,4)/(0,2)^2/(3,1)/(1,3)]"))

test.append(expand("[(2,2)^2/(2,1)^2/(2,0)^3/(4,0)/(0,2)/(0,1)^2/(0,0)]"))

test.append(expand("[(0,10)/(4,6)/(2,0)/(0,2)]"))

for i in range(1,len(test)):
            print(dimChecker(test[i]))
            test[i] = test[i]+[(0,0),(0,0),(0,0)]
            print(classifyIncomplete(test[i], basisA12,orderList2))




test=[(0)]
test.append(expand("[(0,10)/(1,9)/(0,6)/(1,3)/(2,0)/(0,2)/(0,0)^3/(0,8)^3/(0,4)^3/(1,5)^3]"))


test.append(expand("[(0,6)/(1,5)/(0,4)/(1,3)^2/(2,0)/(0,2)^3/(0,4)^6/(0,2)^3/(0,0)^3/(1,3)^3/(1,1)^3]"))


test.append(expand("[(0,6)/(1,4)^2/(1,3)/(0,3)^2/(2,0)/(0,2)/(0,0)^3/(0,0)^6/(0,4)^3/(0,3)^6/(1,3)^3/(1,0)^6]"))


test.append(expand("[(1,4)^2/(0,4)^3/(2,0)/(0,2)/(1,0)^4/(0,0)^3/(0,0)^3/(0,4)^3/(0,2)^9/(1,2)^6]"))


test.append(expand("[(1,3)/(2,0)/(0,2)^6/(1,1)^5/(0,0)^3/(0,0)^3/(0,2)^9/(0,0)^9/(0,0)^6/(1,1)^9]"))


test.append(expand("[(0,0)^9/(0,0)^3/(1,2)^2/(2,0)/(0,2)^3/(1,1)^2/(1,0)^4/(0,1)^4/(0,0)^4/(0,2)^3/(0,1)^{12}/(1,1)^6/(1,0)^6]"))

test.append(expand("[(2,0)/(0,2)/(1,1)^5/(1,0)^4/(0,1)^4/(0,0)^9/(0,0)^9/(0,0)^9/(0,0)^4/(0,1)^9/(0,0)^3/(1,1)^3/(1,0)^3/(1,0)^9]"))


test.append(expand("[(4,1)^2/(4,2)/(0,3)^2/(2,0)/(0,2)/(0,0)^3/(0,0)^3/(2,2)^3/(4,0)^3/(2,1)^6]"))


test.append(expand("[(2,2)/(2,0)^4/(0,2)^4/(1,1)^4/(0,0)^3/(0,0)^6/(0,0)^9/(0,2)^3/(1,1)^3/(1,1)^9/(2,0)^3]"))



test.append(expand("[(5,1)/(4,2)/(3,1)/(1,3)/(2,0)^2/(0,2)/(0,0)^3/(2,2)^3/(4,0)^3/(3,1)^3/(1,1)^3]"))



##print("New method")
##for i in range(1,len(test)):
##    print("////////////////////////////")
##    print(i)
##    print(dimChecker(test[i]))
##    print(latex(test[i]))
##    print(checker(test[i], basisA12,orderList2))
##
##
##a=expand("[(0,0,6)/(0,1,5)/(0,0,4)/(0,1,3)^2/(0,2,0)/(0,0,2)^3/(2,0,4)^2/(2,0,2)/(2,0,0)/(2,1,3)/(2,1,1)]")
##b=expand("[(0,1,3)/(0,2,0)/(0,0,2)^6/(0,1,1)^5/(0,0,0)^3/(2,0,0)/(2,0,2)^3/(2,0,0)^5/(2,1,1)^3]")
##print(dimChecker(a))
##print(dimChecker(b))



l1C3=[(0)]
l2C3=[(0)]
S2C3=[(0)]
l1C3.append(expand("[(5,)]"))
l1C3.append(expand("[(3,)/(1,)]"))
l1C3.append(expand("[(3,)/(0,)^2]"))
l1C3.append(expand("[(2,)^2]"))
l1C3.append(expand("[(1,)^3]"))
l1C3.append(expand("[(1,)^2/(0,)^2]"))
l1C3.append(expand("[(1,)/(0,)^4]"))

lam1C3=[(0)]
lam1C3.append([(2,1)])

for i in range(1,len(l1C3)):
    a=wedge2(l1C3[i])
    a.remove((0,))
    l2C3.append(a)

for i in range(1,len(l1C3)):
    S2C3.append(S2(l1C3[i]))

lie=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,len(l1C3)):
    lie[i]=[(0,0),(0,0),(0,0),(2,0)]+concat([(0,)],S2C3[i])
    lie[i]=lie[i]+concat([(0,)],l2C3[i])
    lie[i]=lie[i]+concat([(0,)],l2C3[i])
    lie[i]=lie[i]+concat([(0,)],l2C3[i])

    lie[i]=lie[i]+concat([(1,)],l1C3[i])
    lie[i]=lie[i]+concat([(1,)],l1C3[i])
    lie[i]=lie[i]+concat([(1,)],l1C3[i])

    
##    print("///////////////////")
##    print(i)
##    print(latex(l1C3[i]))
##    #print(dimChecker(l1C3[i]))
##    #print(dimChecker(l2C3[i]))
##    #print(dimChecker(S2C3[i]))
##    print(classifyIncomplete(lie[i],basisA12,orderList2))

print("Case 8, 9 and 10 and 11")



a=expand("[(2,1)]")
b=expand("[(1,0)^2,(0,1)]")



#Case 8
lie=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(2,1),(2,1),(2,1),(2,1),(2,1),(2,1)]
lie=lie+[(2,2),(4,0)]
lie=lie+[(2,2),(4,0)]
lie=lie+[(2,2),(4,0)]
#print("CASE 8")
#print(classifyIncomplete(lie,basisA12,orderList2))
lie=lie+[(4,2),(0,2),(2,0)]
lie=lie+[(4,1),(0,3)]
lie=lie+[(4,1),(0,3)]
print(dimChecker(lie))
print(checker(lie,basisA12,orderList2))
print(latex(lie))

#Case10
lie=[(0,0,0),(0,0,0),(0,0,0),(2,0,0),(1,2,1),(1,2,1),(1,2,1)]
lie=lie+[(0,2,2),(0,4,0)]
lie=lie+[(0,2,2),(0,4,0)]
lie=lie+[(0,2,2),(0,4,0)]

#print(classifyIncomplete(lie,basisA12,orderList2))
lie=lie+[(0,4,2),(0,0,2),(0,2,0)]
lie=lie+[(1,4,1),(1,0,3)]
a=expand("[(0, 0, 0)^3/(2, 0, 0)/(1, 2, 1)^3/(0, 2, 2)^3/(0, 4, 0)^3/(0, 4, 2)/(0, 0, 2)/(0, 2, 0)/(1, 4, 1)/(1, 0, 3)]")
a1=diagA1(a,1,2)
a2=diagA1(a,1,3)
b1=expand("[(0,  0)^3/(2,  0)/(3, 1)^3/(1, 1)^3/( 2, 2)^3/( 4, 0)^3/(4, 2)/( 0, 2)/( 2, 0)/(5, 1)/(3, 1)/(1, 3)]")
#b2=expand("[(0, 0, 0)^3/(2, 0, 0)/(1, 2, 1)^3/(0, 2, 2)^3/(0, 4, 0)^3/(0, 4, 2)/(0, 0, 2)/(0, 2, 0)/(1, 4, 1)/(1, 0, 3)]")
#print("CASE 10")
#print(checker(a1,basisA12,orderList2))
#print(latex(a1))
#print(checker(b1,basisA12,orderList2))

#print("CASE 11")
#print(checker(a2,basisA12,orderList2))
#print(latex(a2))


#Case 12
lie=[(0,0,0),(0,0,0),(0,0,0),(2,0,0),(1,0,1),(1,0,1),(1,0,1),(1,3,0),(1,3,0),(1,3,0)]
lie=lie+[(0,3,1),(0,4,0),(0,0,0)]
lie=lie+[(0,3,1),(0,4,0),(0,0,0)]
lie=lie+[(0,3,1),(0,4,0),(0,0,0)]
lie=lie+[(0,6,0),(0,0,2),(0,2,0),
         (0,3,1)]
lie=lie+[(1,3,0),(1,4,1)]
a1=diagA1(lie,1,3)
#print("CASE 12")
#print(checker(a1,basisA12,orderList2))
#print(latex(a1))


#Case 13 and 14
print("cases 13 and 14")
a=expand("[(0,4,2)/(0,2,4)/(2,0,0)^2/(2,2,2)/(0,2,0)/(0,0,2)]")

b=expand("[(0,0,4)/(0,2,2)^2/(0,2,0)/(0,0,2)^3/(0,0,0)/(2,2,0)/(2,0,2)^2/(2,0,0)^2]")

print(latex(removeA1(a,1)))
print(classifyIncomplete(removeA1(a,1), basisA12,orderList2))
print(latex(removeA1(b,1)))
print(classifyIncomplete(removeA1(b,1), basisA12,orderList2))


a=expand("[(0,10)/(4,6)/(2,0)/(0,2)/(0,0)/(0,0)]/(0,0)")
print(latex(a))
print(classifyIncomplete(a, basisA12,orderList2))



#Is case (1,22/00^3) in A1D6 somewhere??

a=expand("[(0, 4)^4/(0, 0)^6/(0, 6)/(0, 2)/(2, 3)^4/(0, 3)^4/(2, 0)^6/(2, 4)]")
print("HERE")
print(classify(a,basisA12,orderList2))









print(len(basisA12))
for i in range(1,len(basisA12)):
    print(dimChecker(basisA12[i]))
    print(latex(basisA12[i]))





