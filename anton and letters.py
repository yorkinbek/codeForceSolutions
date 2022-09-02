
a=input()
a=a.strip(',')
b=list(a)
b.sort()
count=0
for i in range(len(b)):
	if(b[i]!='{' and b[i]!='}' and b[i]!=',' and b[i]!=' '):
		if (b[i]!=b[i-1]):
			count+=1
print(count)
