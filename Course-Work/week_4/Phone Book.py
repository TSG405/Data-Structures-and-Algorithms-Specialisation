>>
d={}

t=int(input())


def queryadd(n,name,d):
    d[n]=name
    return d
  
def querydel(n,d):
    j=queryfind(n,d)
    if j != 'not found':
        d.pop(n)
    return d
  
def queryfind(n,d):
    if n in d:return (d[n])
    else:return ("not found")
      
while(t>0):
  
    q1=input().split()
    q=q1[0]
    n=q1[1]
    
    if q=='add':
        name=q1[2]
        queryadd(n,name,d)
        
    elif q=='del':
        querydel(n,d)
        
    else:
        k3=queryfind(n,d)
        print(k3)
        
    t-=1
    
    
    
 @ CODED BY TSG405, 2021
