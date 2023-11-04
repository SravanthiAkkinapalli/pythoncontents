l=[23,2,25,22,22,35,37]
mode=[]
x=l.count(l[0])
mode.append(x)
mode.append(l[0])
for i in range(0,len(l)):
    count=l.count(l[i])
    if count>mode[0]:
        mode[0]=count
        mode[1]=l[i]
print("mode =",mode[1])        
        
        


      
    
