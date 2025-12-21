K,N,M = map(int,input().split())
A=[]
for i in range(M):#ทางไปมีกี่ทาง
    a , b = map(int,input().split())
    A.append((a,b))

r={1}

for i in K:
    ne=set(r)
    for i in range(len(A)):
        a,b=A[i]
        if a in ne:
            A.append(b)
    r=ne
print(max(r))