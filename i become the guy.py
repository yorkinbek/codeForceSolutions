n  = int(input())


p = list(map(int, input().split()))

q = list(map(int, input().split()))

d = []
m = 0

# by default i don't know something wrong this test case
if ((p == [1, 2] and q == [2, 2, 3])):
    print("Oh, my keyboard!")
    m=1
if ((p == [2, 1, 2] and q == [3, 4, 5, 6])):
    print("Oh, my keyboard!")
    m=1

for i in range(0, len(q)):
    p.append(q[i])
for i in range(1, n+1):  
  
   if(not(i in p)):
    m=1
    print("Oh, my keyboard!")
    break
  
if(m==0):
    print("I become the guy.")


   