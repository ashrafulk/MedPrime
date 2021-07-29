def countCurrency(amount):
     
    notes = [100,50, 20, 10, 5, 1]
                
    noteCounter = [0, 0, 0, 0, 0,0, 0]
     
    print ("Currency Count -> ")
    c=0
    txt=[]
    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            c=c+1
            txt.append(str(i))
            
    if c!=1:
        txt.insert(len(txt)-1,"end")
    txt=" ".join(txt)
    print(c,{"by {} notes of {} denomination".format(c,txt)}) 
# Driver code
amount = int(input("enter ammount:"))
countCurrency(amount)
