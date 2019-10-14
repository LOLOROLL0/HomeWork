s = input()
int = len(s)
a = int*23
if a > 100:
    b = a//100
    round(b)
    c = a - b*100
    print(b,"р.",c,"коп.")
else:
    print(a,"коп.") 