import random
from Gene import Gene
from Individuo import Individuo

class ProblemaMochila:
    def __init__(self, numeroIndividuos, numeroGenes, taxaMutacao, capacidadeMochila, condicaoParada):
        self.numeroIndividuos = numeroIndividuos
        self.numeroGenes = numeroGenes
        self.taxaMutacao = taxaMutacao
        self.capacidadeMochila = capacidadeMochila
        self.condicaoParada = condicaoParada

    def geraPrimeiraGeracao(self):
        individuos = []

        for x in range(self.numeroIndividuos):
            genes = []

            gene1 = Gene(1, 400, 200)
            gene2 = Gene(2, 300, 200)
            gene3 = Gene(3, 700, 300)
            gene4 = Gene(4, 900, 400)
            gene5 = Gene(5, 600, 100)
            gene6 = Gene(6, 100, 100)
            gene7 = Gene(7, 600, 5000)
            gene8 = Gene(8, 1000, 300)

            genes.append(gene1)
            genes.append(gene2)
            genes.append(gene3)
            genes.append(gene4)
            genes.append(gene5)
            genes.append(gene6)
            genes.append(gene7)
            genes.append(gene8)

            individuo = Individuo(x, genes, 1)

            for y in range(self.numeroGenes):
                existe = random.randint(0, 1)
                solucaoParcial = individuo.getSolucaoParcial()
                solucaoParcial[y].setSelecionado(existe)

            individuos.append(individuo)

        return individuos

    def inicializa(self):

        if (self.numeroIndividuos % 2) != 0:            
            return print('Quantidade de individuos deve ser par')

        random.seed()
        individuos = []
        solucaoParcial = []
        condicaoParada = self.condicaoParada - 1 # Isso acontece porque a primeira geração já é gerada automaticamente

        individuos = self.geraPrimeiraGeracao()

        print('Gerando a Primeira Geracao:')
        for x in range(self.numeroIndividuos):
            individuos[x].adicionaSolucaoFinal()

        print('\nOrdenando os Elementos da Primeira Geracao')
        individuos = sorted(individuos, key=lambda ind: ind.getFitness(), reverse=True)

        for x in range(self.numeroIndividuos):
            print('x:', individuos[x].id, individuos[x].geracao)
            print('Fitness:', individuos[x].getFitness())
            print('Solucao Final:', individuos[x].getSolucaoFinal())
            print()



problema = ProblemaMochila(8, 8, 0.05, 5000, 8)
problema.inicializa()
