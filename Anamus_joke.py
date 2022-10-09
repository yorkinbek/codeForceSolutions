a = input()
b = input()
c = input()
d = a+b

c =''.join(sorted(c))
d =''.join(sorted(d))

if d == c:
    print("YES")
else:
    print("NO")