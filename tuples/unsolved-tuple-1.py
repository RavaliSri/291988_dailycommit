t=(6,9,6,8,4,6,9,6)
print(t.count(6))
print()
for i in t:
    if t.count(i)>1:
      print(i)