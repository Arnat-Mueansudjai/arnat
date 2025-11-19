x = []
arr = int(input("Len Array: "))
for i in range(arr):
    num = int(input(f"Num{i+1}: "))
    x.append(num)
print("Old:",x)
x.sort() #จัดรูปเเบบ
print("New:",x)
find = int(input("Find: "))
left = 0
right = len(x)-1
mid = int((left + right) / 2)
index = 0 

while True:
    if x[mid] == find:
        index = mid
        print(f"find: {find}: index: {index}")
        break 
    elif x[mid] < find:
        left = mid + 1
    else:
        right = mid - 1
    mid = int((left + right) / 2)
    if left > right:
        print("not find")
        break 
