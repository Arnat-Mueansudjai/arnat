c=[]
max=1
text=input("Enter text:")
c.append(text)
x=""
for i in c:
    if c.count(i) > max:
        max = c.count(i)
        x = i
print(f" Max is :{x} counth:{max}")