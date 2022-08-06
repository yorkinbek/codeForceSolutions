n = int(input())

answer = ""

for i in range(0, n):
    
  if (i % 2 == 0):
    answer += "I hate "
  else:
    answer += "I love "
    
  if (i != n - 1):
    answer += "that "
  else:
    answer += "it"

    
print(answer)