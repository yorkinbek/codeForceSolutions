l = []
n = int(input())

for a in range(0, n):
    line = input().split()
    count = 0

    if line.count('1') >= 2:
        count += 1
        l.append(count)
print(sum(l))

