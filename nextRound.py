n, k = map(int, input().split())

line = list(map(int, input().split()))

maxScore = 0

for i in range(0, n):
    if line[k-1] == 0 and line[i] == line[k-1]:
        maxScore = maxScore + 0
    elif line[k-1] <= line[i]:
        maxScore += 1
    else:
        maxScore += 0
print(maxScore)