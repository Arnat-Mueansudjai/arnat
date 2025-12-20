import math
N=int(input())
all_recipes = [[1, 0]]
for o in range(N):
    All=list(map(int, input().split()))
    S_new = All[0]
    B_new = All[1]
    new_recipes = []
    for recipe in all_recipes:
        old_S = recipe[0]
        old_B = recipe[1]
        current_S = old_S * S_new
        current_B = old_B + B_new
        new_recipes.append([current_S, current_B])
        all_recipes = all_recipes + new_recipes
min_diff=1000000000
for recipe in all_recipes:
    S = recipe[0]
    B = recipe[1]
    if S==1 and B==0:
        continue
    diff=abs(S-B)
    if diff<min_diff:
        min_diff=diff
print(min_diff)