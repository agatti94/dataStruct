def MaxChar(palavra):
    charMap = {}
    maximo = 0
    maxChar = ''

    for i in palavra:
        if charMap.get(i) is not None:
            charMap[i]+=1
        else:
            charMap[i] = 1

    for i in charMap:
        if charMap[i] > maximo:
            maximo = charMap[i]
            maxChar = i

    return maxChar

def main():
    print(MaxChar('Pao com ovo'))

main()
