n = int(input())
count = 0

list = [100, 20, 10, 5, 1]
for i in range(0, 5):
    count = int(n/list[i])
    n = n%list[i]
print(count)