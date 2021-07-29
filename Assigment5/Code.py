def addthree(l,T):
    t=[T-1,T,T+1]
    l1=[]
    l2=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            for k in range(j+1,len(l)):
                l2.append([l[i],l[j],l[k]] )
                l1.append(l[i]+l[j]+l[k])                
    s=""
    c=0
    for i in range(len(l1)):
        for j in range(len(t)):
            if t[j]==l1[i]:
                if c>=1:
                    s=s+" or "
                s=s+str(l2[i])+"="+str(l1[i]) 
                c=c+1
    print("the closest to the target value {} is sum of {}".format(T,s))

l=[1,-4,5,3,2]
T=5
addthree(l,T)
 
