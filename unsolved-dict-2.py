num = [1, 2, 3, 4]
new = current = {}
for n in num:
    current[n] = {}
    current = current[n]
print(new)
