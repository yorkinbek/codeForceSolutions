n = int(input())
x = 0
for i in range(0, n):
    m = input()

    if(m[1] == '+'):
        x += 1
    else:
        x -=1

print(x)