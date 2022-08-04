numbersOfWords = int(input())

for a in range(0, numbersOfWords):
    word = input()
    length = len(word)

    if length > 10:
        print(word[0], length-2, word[-1], sep="")
    else:
         print(word)
