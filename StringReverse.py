def Reverse(palavra):
    reverso = ''
    for i in palavra:
        reverso = i + reverso 

    return reverso

def main():
    print(Reverse('apple'))

main()
