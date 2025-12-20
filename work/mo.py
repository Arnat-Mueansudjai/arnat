nums=set()
for i in range(10):
    num=int(input("Enter number:"))
    nums.add(num%42)

print(len(nums))
