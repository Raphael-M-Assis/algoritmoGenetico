class Individuo:
    def __init__(self, id, solucaoParcial, geracao):
        self.id = id
        self.solucaoParcial = solucaoParcial
        self.solucaoFinal = [0] * len(solucaoParcial)
        self.geracao = geracao
        self.indice = 0
        self.fitness = 0

    def calculaLucro(self, solucaoParcial):
        for gene in solucaoParcial:
            if gene.getSelecionado() == 1:
                self.fitness += gene.getValor()
        
        print(" [ ",self.fitness, " De Valor Fitness!  ] --- x: ", self.id, self.geracao)
        return self.fitness

    def adicionaSolucaoFinal(self):
        self.solucaoFinal = [0] * len(self.solucaoParcial)
        
        for i in range(len(self.solucaoParcial)):
            if self.solucaoParcial[i].getSelecionado() == 1:
                self.solucaoFinal[i] = 1
            else:
                self.solucaoFinal[i] = 0
        
        self.calculaLucro(self.solucaoParcial)

        
    def getFitness(self):
        return self.fitness

    def getSolucaoFinal(self):
        return self.solucaoFinal
    
    def getSolucaoParcial(self):
        return self.solucaoParcial

    def setSolucaoParcial(self, solucaoParcial):
        self.solucaoParcial = solucaoParcial
