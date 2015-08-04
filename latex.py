#print(latex(d[1]))
#sol[1]=sol[1]+e[1]
#print(dimChecker(e[2]))
j=0
for i in range(1,10):
        #sol[i]=sol[i]+e[i]
        print(i)
        print(classifyIncomplete(sol[i],basis2,orderList))
        printer=[]
        #x=latex(d[i])
        #printer.append(str(i)+"&"+str(d[i][0])+"&")
        #for j in range(1,len(d[i])-1):
        #printer.append("&"+str(d[i][j])+"/&")
        #printer.append("&"+str(d[i][len(d[i])-1])+"&")
        x=0
        #for j in range(0,len(printer)):
        #        print(printer[j])
        #print(" \\\\"+" \hline")
        print(str(i)+"&"+latex(d[i])+"&"+latex(sol[i])+"&"+str(j))
        print("\\\\ \hline")
        #print(checker(sol[i],basis2,orderList))
        

##for i in range(1,5):
##        #sol[i]=sol[i]+e[i]
##        #temp=classifyIncomplete(sol[i],basis2,orderList)[1]
##        printer=[]
##        #printer.append(" ")
##        x=latex(d[i])
##        y=latex(sol[i])
##        #var=0
##        t=0
##        j=0
##        while j<len(x):
##                if t==0:
##                        printer.append(str(i)+"&$")
##                else:
##                        printer.append("&$")
##                var=0
##                while var<2 and j<len(x):
##                        if x[j]!="$":
##                                printer[t]=printer[t]+x[j]
##                        if x[j]== "/":
##                                var=var+1
##                        j=j+1
##                printer[t]=printer[t]+"$"
##                var=0
##                j=0
##                while var<4 and j<len(y):
##                        if y[j]!="$":
##                                printer[t]=printer[t]+y[j]
##                        if y[j]== "/":
##                                var=var+1
##                        j=j+1
##                print(printer[t])
##                t=t+1
                
        
