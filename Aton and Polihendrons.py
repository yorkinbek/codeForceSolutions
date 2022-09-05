n = int(input())

result = 0
for i in range(0, n):
    str = input()
    if(str[i] == "Tetrahedron"):
        result += 4
    if(str[i] == "Cube"):
        result += 6
    if(str[i] == "Octahedron"):
        result += 8
    if(str[i] == "Dodecahedron"):
        result += 12
    if(str[i] ==  "Icosahedron"):
        result += 20
    print(result)