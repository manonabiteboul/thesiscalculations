import math
from collections import Counter



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

def tensor1factor(a,b):
    sol=[]
    n=len(a)
   
    if n==1:
        x=a[0]+b[0]
        while x>=abs(a[0]-b[0]):
            sol.append(x)
            x=x-2
    if n==2:
        temp=[]
        temp.append(tensor1factor((a[0],),(b[0],)))
        temp.append(tensor1factor((a[1],),(b[1],)))
      #  print(temp)
        for i in range(0,len(temp[0])):
            for j in range(0,len(temp[1])):
                sol.append((temp[0][i],temp[1][j]))
    if n>2:
        t=[]
        temp=[]
        for i in range(0,n):
            temp.append(tensor1factor((a[i],),(b[i],)))
        #temp.append(tensor((a[1],),(b[1],)))
        #temp.append(tensor((a[2],),(b[2],)))
     #   print(temp)
        for i in range(0,len(temp[0])):
            for j in range(0,len(temp[1])):
                t.append((temp[0][i],temp[1][j]))
      #  print(t)
        for k in range(2,n):
            t2=[]
            for i in range(0,len(t)):
                for j in range(0,len(temp[k])):
                    t2.append(t[i]+(temp[k][j],))
           # print(t2)
            t=t2
        sol=t
    return sol

#TENSOR PRODUCT
def tensor(x,y):
    
    if len(x)==1 and len(y)==1:
        return tensor1factor(x[0],y[0])

    else:
        sol=[]
        for a in x:
            for b in y:
                sol=sol+tensor1factor(a,b)
        return(sol)        

    
#PRINTS STUFF THAT CAN BE COPY PASTED IN LATEX
def latex(a):
    sol = "$"
    done = []
    for x in a:
        if x not in done:
            if a.count(x)==1:
                sol = sol+str(x)+"/"
            else:
                sol = sol+str(x)+"^"+str(a.count(x))+"/"
            done.append(x)
    sol = sol[:-1]+"$"
    #sol = sol[:-1]+" "
    return(sol)   
        
def latexWithoutDollar(a):
    sol = ""
    done = []
    for x in a:
        if x not in done:
            if a.count(x)==1:
                sol = sol+str(x)+"/"
            else:
                sol = sol+str(x)+"^"+str(a.count(x))+"/"
            done.append(x)
    sol = sol[:-1]+" "
    #sol = sol[:-1]+" "
    return(sol)   
        
def wedge2(a):
    if len(a)==1:
        if len(a[0])==1:
            sol=[]
            x=0
            while 2*a[0][0]-2-4*x>=0:
                 sol.append((2*a[0][0]-2-4*x,))           
                 x=x+1
            return(sol)
        if len(a[0])==2:
            if a[0][0]==0:
                sol=[]
                x=wedge2([(a[0][1],)])
                for t in x:
                    sol.append((0,t[0]))
                return sol
            if a[0][1]==0:
                sol=[]
                x=wedge2([(a[0][0],)])
                for t in x:
                    sol.append((t[0],0))
                return sol
            if a[0]==(1,1):
                return [(2,0),(0,2)]
            if a[0]==(2,1):
                return [(2,2),(4,0),(0,0)]
            if a[0]==(1,2):
                return [(2,2),(0,4),(0,0)]
            if a[0]==(3,1):
                return [(4,2),(6,0),(2,0),(0,2)]
            if a[0]==(1,3):
                return [(2,4),(0,6),(2,0),(0,2)]
            if a[0]==(2,2):
                return [(4,2),(2,4),(2,0),(0,2)]
            if a[0]==(5,1):
                return [(8,2),(4,2),(2,0),(0,2),(10,0),(6,0)]
            if a[0]==(1,5):
                return [(2,8),(2,4),(2,0),(0,2),(0,10),(0,6)]
            if a[0]==(4,2):
                return [(6,4),(8,2),(2,4),(4,2),(6,0),(2,0),(0,2)]
            if a[0]==(2,4):
                return [(4,6),(2,8),(2,4),(4,2),(0,6),(2,0),(0,2)]
            if a[0]==(7,1):
                return [(12,2),(8,2),(4,2),(14,0),(10,0),(6,0),(2,0),(0,2)]
            if a[0]==(1,7):
                return [(2,12),(2,8),(2,4),(0,14),(0,10),(0,6),(2,0),(0,2)]
            if a[0]==(3,3):
                return [(6,4),(4,6),(4,2),(2,4),(6,0),(0,6),(2,0),(0,2)]
            else :
                print("Problem! We do not know the wedge^2 of the following vector: "+str(a[0]))
        elif len(a[0])==3:
            if a[0]==(2,1,0):
                return [(2,0,0),(0,2,0),(4,0,0),(0,0,0)]
            if a[0]==(2,0,1):
                return [(2,0,0),(0,0,2),(4,0,0),(0,0,0)]
            if a[0]==(0,1,2):
                return [(0,0,2),(0,2,0),(0,0,4),(0,0,0)]
            if a[0]==(1,0,2):
                return [(0,0,2),(2,0,0),(0,0,4),(0,0,0)]
            if a[0]==(0,1,3):
                return [(0,2,4),(0,0,6),(0,2,0),(0,0,2)]
            if a[0]==(1,3,0):
                return [(2,4,0),(0,6,0),(2,0,0),(0,2,0)]
            if a[0]==(0,3,1):
                return [(0,4,2),(0,6,0),(0,2,0),(0,0,2)]
            if a[0]==(1,0,3):
                return [(2,0,4),(0,0,6),(2,0,0),(0,0,2)]
            if a[0]==(3,0,1):
                return [(4,0,2),(6,0,0),(2,0,0),(0,0,2)]
            if a[0]==(0,1,5):
                return [(0,2,8),(0,2,4),(0,2,0),(0,0,10),(0,0,2),(0,0,6)]
            if a[0]==(1,0,5):
                return [(2,0,8),(2,0,4),(2,0,0),(0,0,10),(0,0,2),(0,0,6)]
            if a[0]==(5,0,1):
                return [(8,0,2),(4,0,2),(2,0,0),(10,0,0),(0,0,2),(6,0,0)]
            if a[0]==(2,1,1):
                return [(2,2,2),(4,2,0),(4,0,2),(2,0,0),(0,2,0),(0,0,2)]
            if a[0]==(1,2,1):
                return [(2,2,2),(2,4,0),(0,4,2),(2,0,0),(0,2,0),(0,0,2)]
            if a[0]==(1,1,2):
                return [(2,2,2),(2,0,4),(0,2,4),(2,0,0),(0,2,0),(0,0,2)]
            if a[0]==(1,1,1):
                return [(2,2,0),(2,0,2),(0,2,2),(0,0,0)]
            x=0
            for i in range(0,3):
               x=x+a[0][i]

            #y counts the nb of zeros
            y=0
            for i in range(0,3):
                if a[0][i]==0:
                        y=y+1
            if y==2:
                
                for i in range(0,3):
                        if a[0][i]!=0:
                                j=i
                
                if j==0:
                        s=concat(wedge2([(a[0][j],)]),[(0,0)])
                if j==1:
                        s=concat([(0,)],concat(wedge2([(a[0][j],)]),[(0,)]))
                if j==2:
                        s=concat([(0,0)],wedge2([(a[0][j],)]))
                return s;
            if x==0:
                #print("here")    
                s=[]
                return(s)
            if x==2:
                #print("x=2")
                if 2 not in a[0]:
                    s=[]
                    temp=0
                    for j in range(0,3):
                        if a[0][j]==1:
                            if j==0:
                                s.append((2,0,0))
                            else:
                                temp=(0,)
                                for i in range(1,j):
                                    temp=temp+(0,)
                                temp=temp+(2,)
                                for i in range(j+1,3):
                                    temp = temp+(0,)
                                s.append(temp)

                else:
                     s=[a[0]]
                return(s)

            if x==1:
                    s=[(0,0,0)]
                    return(s)
            
                     
                    
            if a[0]==(1,1,1):
                return [(2,2,0),(2,0,2),(0,2,2),(0,0,0)]
            if a[0]==(2,1,1):
                return [(2,2,2),(4,2,0),(4,0,2),(2,0,0),(0,2,0),(0,0,2)]
            if a[0]==(2,2,0):
                return [(4,2,0),(2,4,0),(2,0,0),(0,2,0)]
            if a[0]==(2,0,2):
                return [(4,0,2),(2,0,4),(2,0,0),(0,0,2)]
            if a[0]==(0,2,2):
                return [(0,4,2),(0,2,4),(0,2,0),(0,0,2)]
            if a[0]==(3,1,0):
                return [(4,2,0),(6,0,0),(2,0,0),(0,2,0)]
           
            else :
                print("Problem! We do not know the wedge^2 of the following vector: "+str(a[0]))

        elif len(a[0])==4:
            if a[0]==(1,1,1,1):
                return [(2,2,2,0),(2,2,0,2),(2,0,2,2),(0,2,2,2),(2,0,0,0),(0,2,0,0),(0,0,2,0),(0,0,0,2)]
            #x counts total value
            if a[0]==(3,1,0,0):
                return [(4,2,0,0),(6,0,0,0),(2,0,0,0),(0,2,0,0)]
            if a[0]==(0,0,1,3):
                return [(0,0,2,4),(0,0,0,6),(0,0,0,2),(0,0,2,0)]
            if a[0]==(1,0,0,3):
                return [(2,0,0,4),(0,0,0,6),(0,0,0,2),(2,0,0,0)]
            if a[0]==(0,1,0,3):
                return [(0,2,0,4),(0,0,0,6),(0,0,0,2),(0,2,0,0)]
            if a[0]==(0,3,0,1):
                return [(0,4,0,2),(0,6,0,0),(0,2,0,0),(0,0,0,2)]
            if a[0]==(3,0,0,1):
                return [(4,0,0,2),(6,0,0,0),(2,0,0,0),(0,0,0,2)]
            if a[0]==(0,0,2,2):
                return [(0,0,4,2),(0,0,2,4),(0,0,2,0),(0,0,0,2)]
            if a[0]==(0, 1, 1, 2):
                return [(0,2,2,2),(0,0,2,4),(0,2,0,4),(0,2,0,0),(0,0,2,0),(0,0,0,2)]
            if a[0]==(2,0,0,2):
                return [(2,0,0,4),(4,0,0,2),(2,0,0,0),(0,0,0,2)]
            if a[0]==(0,2,0,2):
                return [(0,2,0,4),(0,4,0,2),(0,2,0,0),(0,0,0,2)]
            if a[0]==(2,2,0,0):
                return [(4,2,0,0),(2,4,0,0),(2,0,0,0),(0,2,0,0)]
            if a[0]== (0, 0, 3, 1):
                return [(0,0,4,2),(0,0,6,0),(0,0,0,2),(0,0,2,0)]
            if a[0]==(1,3,0,0):
                return [(2,4,0,0),(0,6,0,0),(2,0,0,0),(0,2,0,0)]
            if a[0]==(1,0,3,0):
                return [(2,0,4,0),(0,0,6,0),(2,0,0,0),(0,0,2,0)]
            if a[0]==(3,0,1,0):
                return [(4,0,2,0),(6,0,0,0),(2,0,0,0),(0,0,2,0)]
            if a[0]==(0,0,1,2):
                return [(0,0,2,2),(0,0,0,4),(0,0,0,0)]
            if a[0]==(0,0,1,5):
                return [(0,0,2,8),(0,0,2,4),(0,0,2,0),(0,0,0,2),(0,0,0,10),(0,0,0,6)]
            if a[0]==(1,0,1,2):
                return [(2,0,2,2),(0,0,2,4),(2,0,0,4),(2,0,0,0),(0,0,2,0),(0,0,0,2)]
            if a[0]==(2,0,1,1):
                return [(2,0,2,2),(4,0,2,0),(4,0,0,2),(2,0,0,0),(0,0,2,0),(0,0,0,2)]
 

            x=0
            for i in range(0,4):
               x=x+a[0][i]

            #y counts the nb of zeros
            y=0
            for i in range(0,4):
                if a[0][i]==0:
                        y=y+1
            if y==3:
                for i in range(0,4):
                        if a[0][i]!=0:
                                j=i
                
                if j==0:
                        s=concat(wedge2([(a[0][j],)]),[(0,0,0)])
                if j==1:
                        s=concat([(0,)],concat(wedge2([(a[0][j],)]),[(0,0)]))
                if j==2:
                        s=concat([(0,0)],concat(wedge2([(a[0][j],)]),[(0,)]))
                if j==3:
                        s=concat([(0,0,0)],wedge2([(a[0][j],)]))
                return s;
            if x==0:
                #print("here")    
                s=[]
                return(s)
            if x==2:
                #print("x=2")
                if 2 not in a[0]:
                    s=[]
                    temp=0
                    for j in range(0,4):
                        if a[0][j]==1:
                            if j==0:
                                s.append((2,0,0,0))
                            else:
                                temp=(0,)
                                for i in range(1,j):
                                    temp=temp+(0,)
                                temp=temp+(2,)
                                for i in range(j+1,4):
                                    temp = temp+(0,)
                                s.append(temp)

                else:
                     s=[a[0]]
                return(s)

            else:
                print("Problem! We do not know the wedge^2 of the following vector: "+str(a[0]))

        elif len(a[0])==5:
            x=0
            for i in range(0,5):
               x=x+a[0][i]

            #y counts the nb of zeros
            y=0
            for i in range(0,5):
                if a[0][i]==0:
                        y=y+1
            if y==4:
                for i in range(0,5):
                        if a[0][i]!=0:
                                j=i
                
                if j==0:
                        s=concat(wedge2([(a[0][j],)]),[(0,0,0,0)])
                if j==1:
                        s=concat([(0,)],concat(wedge2([(a[0][j],)]),[(0,0,0)]))
                if j==2:
                        s=concat([(0,0)],concat(wedge2([(a[0][j],)]),[(0,0)]))
                if j==3:
                        s=concat([(0,0,0)],concat(wedge2([(a[0][j],)]),[(0,)]))
                if j==4:
                        s=concat([(0,0,0,0)],wedge2([(a[0][j],)]))
                return s;
            if x==0:
                #print("here")    
                s=[]
                return(s)
            if x==2:
                #print("x=2")
                if 2 not in a[0]:
                    s=[]
                    temp=0
                    for j in range(0,5):
                        if a[0][j]==1:
                            if j==0:
                                s.append((2,0,0,0,0))
                            else:
                                temp=(0,)
                                for i in range(1,j):
                                    temp=temp+(0,)
                                temp=temp+(2,)
                                for i in range(j+1,5):
                                    temp = temp+(0,)
                                s.append(temp)

                else:
                     s=[a[0]]
                return(s)
        
            if a[0]==(0,0,0,1,3):
                    return [(0,0,0,2,4),(0,0,0,0,6),(0,0,0,2,0),(0,0,0,0,2)]
            if a[0]==(3,0,0,0,1):
                    return [(4,0,0,0,2),(6,0,0,0,0),(2,0,0,0,0),(0,0,0,0,2)]
            if a[0]==(1,0,0,0,3):
                    return [(2,0,0,0,4),(0,0,0,0,6),(2,0,0,0,0),(0,0,0,0,2)]
            if a[0]==(0,0,0,2,2):
                    return [(0,0,0,2,4),(0,0,0,4,2),(0,0,0,2,0),(0,0,0,0,2)]
            if a[0]==(0,0,1,1,2):
                return [(0,0,2,2,2),(0,0,0,2,4),(0,0,2,0,4),(0,0,2,0,0),(0,0,0,2,0),(0,0,0,0,2)]
                
                
#Missing:(0,0,0,1,3),(0,0,0,2,2),(1,0,0,0,3),(0,0,1,1,2)
            if x==1:
                    s=[(0,0,0)]
                    return(s)

        elif len(a[0])==6:
            #print("a[0] has len 6")
            x=0
            for i in range(0,6):
               x=x+a[0][i]

            if x==0:
                s=[]
            if x==2:
                #print("x=2")
                if 2 not in a[0]:
                    s=[]
                    temp=0
                    for j in range(0,6):
                        if a[0][j]==1:
                            if j==0:
                                s.append((2,0,0,0,0,0))
                            else:
                                temp=(0,)
                                for i in range(1,j):
                                    temp=temp+(0,)
                                temp=temp+(2,)
                                for i in range(j+1,6):
                                    temp = temp+(0,)
                                s.append(temp)

                else:
                     s=[a[0]]

            if x==1:
                s=[(0,0,0,0,0,0)]
                     
            return(s)
                            
                        
            
        else:
                print("Problem! We do not know the wedge^2 of the following vector: "+str(a[0]))

    else:   
        l=tensor([a[0]], a[1:])
        t=[]
        if len(a[0])==1:
            for x in l:       
                t.append((x,))
        else:
            t=list(l)
        sol=wedge2([a[0]])+t+wedge2(a[1:])
        return(sol)


    

def S2(a):
    if len(a)==1:
        if len(a[0])==1:
            sol=[]
            x=0
            if a[0][0]%2==0:
                r=a[0][0]//2
                while 4*r-4*x>=0:
                     sol.append((4*r-4*x,))           
                     x=x+1
                return(sol)
            else:
                r=(a[0][0]-1)//2
                while 4*r+2-4*x>=0:
                     sol.append((4*r+2-4*x,))           
                     x=x+1
                return(sol)
        if len(a[0])==2:
            if a[0][0]==0:
                sol=[]
                x=S2([(a[0][1],)])
                for t in x:
                    sol.append((0,t[0]))
                return sol
            if a[0][1]==0:
                sol=[]
                x=S2([(a[0][0],)])
                for t in x:
                    sol.append((t[0],0))
                return sol
            if a[0]==(1,1):
                return [(2,2),(0,0)]
            if a[0]==(2,1):
                return [(4,2),(0,2),(2,0)]
            if a[0]==(1,2):
                return [(2,4),(0,2),(2,0)]
            else :
                print("Problem! We do not know the wedge^2 of the following vector: "+str(a[0]))
        elif len(a[0])==3:
            if a[0]==(1,1,1):
                return [(2,2,2),(2,0,0),(0,2,0),(0,0,2)]
            else :
                print("Problem! We do not know the wedge^2 of the following vector: "+str(a[0]))

        else:
                print("Problem! We do not know the wedge^2 of the following vector: "+str(a[0]))


    else:   
        l=tensor([a[0]], a[1:])
        t=[]
        if len(a[0])==1:
            for x in l:       
                t.append((x,))
        else:
            t=list(l)
        sol=S2([a[0]])+t+S2(a[1:])
        return(sol)
#print((0,)*3)

def wedge3(a):
    if len(a)==1:
        if dimChecker(a)<3:
            return []
        if dimChecker(a)==3:
            n=len(a[0])
            x=(0,)*n
            return [x]
        if dimChecker(a)==4:
            #print("here")
            return(a)

            
        if len(a[0])==1:
            if a[0][0]==5:
                return [(9,),(5,),(3,)]
            if a[0][0]==6:
                return [(12,),(8,),(6,),(4,),(0,)]
            sol=[]
            x=0
            while 3*a[0][0]-6-4*x>=0:
                 sol.append((3*a[0][0]-6-4*x,))           
                 x=x+1
            return(sol)
        if len(a[0])==2:
            if a[0]==(5,0):
                return [(9,0),(5,0),(3,0)]
            if a[0][0]==0:
                sol=[]
                x=wedge3([(a[0][1],)])
                for t in x:
                    sol.append((0,t[0]))
                return sol
            if a[0][1]==0:
                sol=[]
                x=wedge3([(a[0][0],)])
                for t in x:
                    sol.append((t[0],0))
                return sol
            if a[0]==(1,1):
                return [(1,1)]
            if a[0]==(2,1):
                return [(4,1),(2,1),(0,3)]
            if a[0]==(1,2):
                return [(1,4),(1,2),(3,0)]
            if a[0]==(3,1):
                return [(7,1),(5,1),(3,3),(3,1),(1,1)]
            if a[0]==(1,3):
                return [(1,7),(1,5),(3,3),(1,3),(1,1)]
            if a[0]==(2,2):
                return [(4,4),(4,2),(2,4),(6,0),(0,6),(2,2),(2,0),(0,2)]

            else :
                print("Problem! We do not know the wedge^2 of the following vector: "+str(a[0]))
        elif len(a[0])==3:
            if a[0]==(1,1,1):
                return [(3,1,1),(1,3,1),(1,1,3),(1,1,1)]
            if a[0]==(2,1,0):
                return [(4,1,0),(2,1,0),(0,3,0)]
            if a[0]==(0,0,4):
                return [(0,0,6),(0,0,2)]
            if a[0]==(4,0,0):
                return [(6,0,0),(2,0,0)]
            if a[0]==(0,1,1):
                return [(0,1,1)]
        else :
            print("Problem! We do not know the wedge^3 of the following vector: "+str(a[0]))



    else:   
        l=tensor(wedge2([a[0]]), a[1:])
        t=[]
        if len(a[0])==1:
            for x in l:       
                t.append((x,))
        else:
            t=list(l)
        l2=tensor([a[0]], wedge2(a[1:]))
        t2=[]
        if len(a[0])==1:
            for x in l2:       
                t2.append((x,))
        else:
            t2=list(l2)
        sol=wedge3([a[0]])+t+t2+wedge3(a[1:])
        return(sol)



def wedge4(a):
    if len(a)==1:
        if dimChecker(a)<4:
            return []
        if dimChecker(a)==4:
            n=len(a[0])
            x=(0,)*n
            return [x]
        if dimChecker(a)==5:
            return a
        if dimChecker(a)==6:
            return wedge2(a)
        if dimChecker(a)==7:
            return wedge3(a)
        #if dimChecker(a)==4:
        #    #print("here")
        #    return(a)

            
        if len(a[0])==1:
            if a[0][0]==6:
                return [(12,),(8,),(6,),(4,),(0,)]
            sol=[]
            x=0
         #   while 3*a[0][0]-6-4*x>=0:
         #        sol.append((3*a[0][0]-6-4*x,))           
         #        x=x+1
         #   return(sol)
        if len(a[0])==2:
            if a[0][0]==0:
                sol=[]
                x=wedge3([(a[0][1],)])
                for t in x:
                    sol.append((0,t[0]))
                return sol
            if a[0][1]==0:
                sol=[]
                x=wedge3([(a[0][0],)])
                for t in x:
                    sol.append((t[0],0))
                return sol
            if a[0]==(1,1):
                return [(0,0)]
            if a[0]==(2,1):
                return [(2,2),(4,0),(0,0)]
            if a[0]==(1,2):
                return [(2,2),(0,4),(0,0)]
            if a[0]==(3,1):
                return []
            if a[0]==(1,3):
                return []
            if a[0]==(2,2):
                return []
            else :
                print("Problem! We do not know the wedge^2 of the following vector: "+str(a[0]))
        else :
            print("Problem! We do not know the wedge^2 of the following vector: "+str(a[0]))



    else:   
        l=tensor(wedge3([a[0]]), a[1:])
        t=[]
        if len(a[0])==1:
            for x in l:       
                t.append((x,))
        else:
            t=list(l)
        l2=tensor([a[0]], wedge3(a[1:]))
        t2=[]
        if len(a[0])==1:
            for x in l2:       
                t2.append((x,))
        else:
            t2=list(l2)

        l3=tensor(wedge2([a[0]]), wedge2(a[1:]))
        t3=[]
        if len(a[0])==1:
            for x in l3:       
                t3.append((x,))
        else:
            t3=list(l3)



            
        sol=wedge4([a[0]])+t+t2+t3+wedge4(a[1:])
        return(sol)





def concat(a,b):
    sol=[]
    for x in a:
        for y in b:
           sol.append(x+y)      
    return(sol)    

#print(dimChecker([(0,),(0,),(0,)]))
#print(latex(wedge3([(3,0),(0,4),(2,0)])))
#print(tensor([(2,)],[(3,)]))

#print(latex(tensor([(1,1),(1,1),(0,0)],[(2,2),(2,2)])))

#A12inA1D6inE7

VD6=[[0],[5,5],[10,0],[8,2],[8,0,0,0],[3,3,1,1],[3,3,2,0],[3,3,0,0,0,0],[6,4],[6,1,1,0],[6,2,0,0],[6,0,0,0,0,0],[4,1,1,2],[4,1,1,0,0,0],[4,2,2,0],[4,2,0,0,0,0],[4,0,0,0,0,0,0,0],[1,1,1,1,1,1],[1,1,1,1,2,0],[1,1,1,1,0,0,0,0],[1,1,2,2,0,0],[1,1,2,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[2,2,2,2],[2,2,2,0,0,0],[2,2,0,0,0,0,0,0],[2,0,0,0,0,0,0,0,0,0]]

VD6Vect =[]
for x in VD6:
    temp=[]
    for y in x:
        temp.append((y,))
    VD6Vect.append(temp)
#for x in VD6Vect:
#    if dimChecker(x)==12:
#       print("This is not equal to 12")
#       print(x)
#print(VD6Vect)
LE7=[]
for x in VD6Vect:
    LE7.append([(2,0)]+concat([(0,)], wedge2(x)))
options=[[0]]
Incomplete =[1,4]
LE7[2] = LE7[2]+[(1,15),(1,9),(1,5)]
LE7[3] = LE7[3]+[(1,11),(1,9),(1,5),(1,3)]
#LE7[4] = LE7[4]+[(1,10),(1,10),(1,4),(1,4)]???
#LE727 is the second option of case5
LE7.append(LE7[5]+[(1,5),(1,3),(1,3),(1,3),(1,3),(1,3),(1,1),(1,1),(1,1)])
LE7[5] = LE7[5]+[(1,4),(1,4),(1,4),(1,4),(1,2),(1,2),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0)]

LE7[6] = LE7[6]+[(1,5),(1,4),(1,4),(1,3),(1,2),(1,2),(1,1),(1,1),(1,1)]
LE7[7] = LE7[7]+expand("[(1,4)^2,(1,3)^4,(1,0)^6]")
LE7[8] = LE7[8]+expand("[(1,9),(1,7),(1,5),(1,3)^2]")
LE7[9] = LE7[9]+expand("[(1,7),(1,6)^2,(1,5),(1,0)^2,(1,1)]")
LE7[10] = LE7[10]+expand("[(1,7)^2,(1,5)^2,(1,1)^2]")



#for i in range(1,11):
   # print(dimChecker(LE7[i]))
#print(latex(LE7[10]))

#print(expand("[(1,5),(2,3)^2]"))














#printLE8 prints lambda_1\downarrow A1n and LE8 \downarrow A1n so can go in a latex long table

def latex2(a):
    sol = ""
    done = []
    for x in a:
        if x not in done:
            if a.count(x)==1:
                sol = sol+str(x)+"/"
            else:
                sol = sol+str(x)+"^"+str(a.count(x))+"/"
            done.append(x)
    sol = sol[:-1]
    #sol = sol[:-1]+" "
    return(sol)

def printLE8(i,l1,E8):
    f=""
    f=f+str(i)+"&$A_1A_1D_6$&$(1,1,"
    letter=0
    nb1=0
    #max1 counts number of factors per line on lambda_1 and max2 counts number of factors per line of LE8 \downarrow A_1^n
    max1=2
    max2=6
    while  nb1<max1:
        if letter<len(l1):
                f=f+l1[letter]
        letter=letter+1
        if letter<len(l1):
                if l1[letter]== "/":
                    nb1=nb1+1
        else:
                nb1=max1
        
    f=f+"/$&$"
    nb2=0
    letter2=0
    while  nb2<max2:
        f=f+E8[letter2]
        letter2=letter2+1
        if E8[letter2]== "/":
            nb2=nb2+1
    f=f+"/$\\\\"
    letter = letter+1
    letter2 = letter2+1
    print(f)
    while letter<len(l1)-1 or letter2<len(E8)-1:
       # print("letter = "+str(letter))
       # print("len(l1) = "+str(len(l1)))
        
        if letter > len(l1)-1:
            f="&&&"
        else:
            f="&&$"
            nb1=0
            while  nb1<max1 and letter<len(l1)-1:
                f=f+l1[letter]
                letter=letter+1
                if l1[letter]== "/":
                    nb1=nb1+1
            
            if letter>len(l1)-2:
                f=f+l1[letter]+")$&"
            else:
                f=f+l1[letter]+"$&"
        
        nb2=0
        f=f+"$"
        while  nb2<max2 and letter2<len(E8)-1:
            f=f+E8[letter2]
            letter2=letter2+1
            if E8[letter2]== "/":
                nb2=nb2+1
        f=f+E8[letter2]+"$\\\\"
        letter = letter+1
        letter2 = letter2+1
        print(f)
    print("\hline")

   
