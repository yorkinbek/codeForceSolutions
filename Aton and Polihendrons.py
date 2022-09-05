n = int(input())
list = ["Tetrahedron", "Cube", "Octahedron", "Dodecahedron", "Icosahedron"]
arr = []
newList = []
for i in range(0, n):
    str = input()
    newList.append(str)

    if(newList[i]== list[0]):
        arr.append(4)
    if(newList[i] == list[1]):
        arr.append(6)
    if(newList[i]== list[2]):
        arr.append(8)
    if(newList[i] == list[3]):
        arr.append(12)
    if(newList[i] ==  list[4]):
        arr.append(20)
print(sum(arr))
