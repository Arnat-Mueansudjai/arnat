text ="AABABBBAA"
max_ab = 0
for i in range(len(text)):
    A=0
    B=0
    for j in range(i, len(text)):
        if text[j] == 'A':
            A += 1
        elif text[j] == 'B':
            B += 1
        if A == B:
            max_ab = max(max_ab, j - i + 1)

print(max_ab)

