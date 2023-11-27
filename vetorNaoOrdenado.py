class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = [None] * capacidade

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(1 , '-', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('capacida maxima atingida')
        else:
            self.ultima_posicao += 1 
            self.valores[self.ultima_posicao] = valor
    
    def pesquisar(self,valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i 
        return -1 

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1

def main():
    a = VetorNaoOrdenado(6)
    a.insere(2)
    a.insere(1)
    a.imprime()
    print(a.pesquisar(2)) 
    a.excluir(2)
    a.imprime()
main()

