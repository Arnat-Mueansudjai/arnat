base=[]
arr = int(input("Enter your loob:"))
for i in range(arr):
    data=int(input("Enter data:"))
    base.append(data)
sortdata=base.sort
if base == sortdata:
    print(True)
else:
    print(False)