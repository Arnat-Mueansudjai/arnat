for i in range(4):
    teams = input("enter name:").strip()

goals = []
for j in range(4):
    goals.append(list(map(int, input("enter point:").split())))

stats = []
for i in range(4):
    point = 0
    gf = 0
    ga = 0

    for j in range(4):
        gf += goals[i][j]
        ga += goals[j][i]

        if i != j:
            if goals[i][j] > goals[j][i]:
                point += 3
            elif goals[i][j] == goals[j][i]:
                point += 1

    gd = gf - ga
    stats.append([teams[i], point, gd, gf])

stats.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for name, point,gd,gs in stats:
    print(name, point)