x = "CBABCACCC" 
x = list(x)
position = [1,None,None]
for i in x:
    if i == 'A':
        position[0] , position[1] = position[1], position[0]
    elif i == 'B':
        position[1],position[2] = position[2],position[1]
    else:
        position[0],position[2] = position[2],position[0]

if position[0] == 1:
    print(1)
elif position[1] == 1:
    print(2)
else:
    print(3)