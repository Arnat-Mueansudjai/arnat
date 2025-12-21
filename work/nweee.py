K,N,M= map(int,input().split())
i=0
A=[]
while i<=M:
    a,b=map(int,input().split())
    A.append((a,b))
    i+=1

r=[1]
j=0
k=0
while j<=A:
    ne =set()
    j+=1
    while k < len(A):
        a, b = A[i]
        if a in r:
            ne.add(b)
        k += 1
    r=ne
print(max(r))
