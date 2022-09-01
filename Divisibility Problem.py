n = int(input())

arr = []
for i in range(0, n):
    k, p = map(int, input().split())
    if (k%p == 0):
        diff = 0
        arr.append(diff)
    else:
        
        carry = int(k/p)
        result = (carry + 1) * p
        diff = result - k
        arr.append(diff)
for i in  range(0, len(arr)):
    print(arr[i])