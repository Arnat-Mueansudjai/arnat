a=[1,2,3,4,5,1,2]
b=set()
for i in a:
    if i in b:
        print(f"df:{i}")
        break
    b.add(i)