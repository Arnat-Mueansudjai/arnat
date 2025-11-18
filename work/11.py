w=input("text:")
num=0
for i in range (len(w)):
    if num < w.count(w[i]):
        num = w.count(w[i])
        a=w[i]
print(a,num)