num = [4,3,2,7,8,2,3,1]
max_num=max(num)
#s=set()
n_m=[]
for i in range(1,max_num):
    if i not in s:
        n_m.append(i)
print(n_m)