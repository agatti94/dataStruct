class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimo_valor = -1
        self.valores = [None] * capacidade

    def imprime(self):
        if self.ultimo_valor == -1:
            print('Vetor vazio')
        else:
            for i in range(self.ultimo_valor + 1):
                print(i, '-', self.valores[i])

    def insere(self, valor):
        if self.ultimo_valor == self.capacidade - 1:
            print('Capacidade maxima atingida')
            return 
        
        posicao = 0
        for i in range(self.ultimo_valor + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultimo_valor:
                posicao = i + 1 

        x = self.ultimo_valor
        while x >=posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultimo_valor += 1

    def procurar(self, valor):
        for i in range(self.ultimo_valor + 1):
            if self.valores[i] > valor: 
                return -1 
            if self.valores[i] == valor:
                return i
    
    def excluir(self, valor):
        posicao = self.procurar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimo_valor):
                self.valores[i] == self.valores[i + 1]
            self.ultimo_valor -= 1
    
    def procura_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultimo_valor

        while True:
            posicao_atual = int((limite_inferior + limite_superior)/2)
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif limite_inferior > limite_inferior:
                return -1 
            else:
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1

        

def main():
    vetor = VetorOrdenado(10)
    vetor.insere(6)
    vetor.insere(2)
    vetor.insere(1)
    vetor.insere(7)
    vetor.insere(3)
    print(vetor.procura_binaria(6))
    vetor.imprime()

main()


