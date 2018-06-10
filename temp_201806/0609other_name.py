a = [1, [11, 22], (1, 2, 3)]
b = list(a)
a.append(100)
a[1].remove(11)
print(a)
print(b)
b[1] += [33, 44]
b[2] += (4, 5)
print(a)
print(b)
