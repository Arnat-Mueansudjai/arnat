rows = int(input("Enter the rows: "))
i = 0

while i <= rows:
    j = 0
    while j < i:
        print("*", end=' ')
        j += 1
    print()
    i += 1
