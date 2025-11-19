c=[]
max=1
text=input("Enter text:")
c.append(text)
d=set()
x=""
for i in c:
    if i in d:
        print(f"df:{i}")
    
    if c.count(i) > max:
        max = c.count(i)
        x = i
print(f" Max is :{x} counth:{max}")
