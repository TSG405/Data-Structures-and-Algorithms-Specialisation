>>
from collections import deque



def slw(arr,n,k):
    Q = deque()
    
    for i in range(k):
        while Q and arr[i]>=arr[Q[-1]]:
            Q.pop()
            
        Q.append(i)

    for i in range(k,n):
        print(str(arr[Q[0]]) + " ",end=" ")
        
        while Q and Q[0]<=i-k:
            Q.popleft()
            
        while Q and arr[i]>=arr[Q[-1]]:
            Q.pop()
            
        Q.append(i)
        
    print(str(arr[Q[0]]))

    
    
if __name__ == '__main__':
    
    n = int(input())
    arr = []
    tsg = input().split()
    
    for i in tsg:
        arr.append(int(i))

    k = int(input())

    slw(arr,n,k)


    
 @ CODED BY TSG405, 2021
