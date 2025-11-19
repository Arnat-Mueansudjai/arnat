a = [10, 10, 5, 5, 5]
d = set()
for i in a:
    if i in d:
        print("First duplicate is:", i)
        break
    d.add(i)
