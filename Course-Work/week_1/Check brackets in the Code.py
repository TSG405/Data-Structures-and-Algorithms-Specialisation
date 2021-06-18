>>
def check(st):
    stack,d,k=[],[],0
    l1=["(","{","["]
    l2=[")","}","]"]
    for i in range(len(st)):
        
        if st[i] in l1:
            stack.append(st[i])
            d.append(i)
        
        elif st[i] in l2:
            p=l2.index(st[i])
            if (len(stack)>0):
                if l1[p]==stack[len(stack)-1]:
                    stack.pop()
                    d.pop(-1)
                else: return(i+1)
            else: return(i+1)
    
    if len(stack)==0: return("Success")
    else: return(d[0]+1)

print(check(input()))



@ CODED BY TSG405, 2021
