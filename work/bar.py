import math

N = int(input())
I = []

for i in range(N):
    I.append(list(map(int, input().split())))

s = math.prod(bar[0] for bar in I)
b = sum(bar[1] for bar in I)

print(abs(s - b))
