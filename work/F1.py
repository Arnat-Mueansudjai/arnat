ten = int(input("ป้อนเลขฐาน 10:"))
two=[]
while ten>0:
    two.append(ten%2)
    ten=ten//2
two=two[::-1]
print(two)