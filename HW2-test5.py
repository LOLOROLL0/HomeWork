a = int(input())
j = 0
for i in range (1,a + 1):
    if a % i == 0:
        j = j + 1
        print(i, end="")
if j == 2 :
    print("")
    print("AHTUNG")