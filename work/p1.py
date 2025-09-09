rows = int(input("Enter the rows: "))
i = 1
while i <= rows:
    j = 0
    while j < i:
        print(chr(ord('A') + j), end=' ')
        j += 1
    print()
    i += 1