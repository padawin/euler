a = 1000 - 1
n = 3
m = 5
l = [i * n for i in range(1 + a // n)]
l.extend([i * m for i in range(1 + a // m)])
print(sum(set(l)))
