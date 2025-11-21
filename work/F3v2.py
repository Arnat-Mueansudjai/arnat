exp = "A+B(C-D)"
output = []
reap = []   
late = []   
fon = []   

for ch in exp:
    if ch.isalnum():     
        fon.append(ch)

    elif ch == '(':
        reap.append(ch)

    elif ch == ')':
        while reap and reap[-1] != '(':
            fon.append(reap.pop())
        reap.pop() 

    elif ch in "*" or ch in "/":         
        while late:
            output.append(late.pop())
        late.append(ch)

    elif ch in "+" or ch in "-":          
        while late:            
            output.append(late.pop())
        while fon:             
            output.append(fon.pop())
        fon.append(ch)

while late:
    output.append(late.pop())
while fon:
    output.append(fon.pop())

print(output)
