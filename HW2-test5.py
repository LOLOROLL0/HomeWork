c, d = 0, 1
for i in range(int(input())):
    a, b = int(input()), int(input())
    c = c * b + a * d
    d = b * d
x, y = c, d
while y > 0:
    x, y = y, x % y
print(c // x, '/', d // x, sep='')