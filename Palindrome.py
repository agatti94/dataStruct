def Palindrome(palavra):
    reverso = ''
    for i in palavra:
        reverso = i + reverso
    
    if palavra == reverso:
        return True
    else:
        return False

def main():
    print(Palindrome('oio'))
main()
