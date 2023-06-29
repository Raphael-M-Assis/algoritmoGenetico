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

    def geraGenes(self):
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

        return genes
    
    def geraPrimeiraGeracao(self):
        individuos = []

        for x in range(self.numeroIndividuos):
            genes = self.geraGenes()

            individuo = Individuo(x, genes, 1)

            for y in range(self.numeroGenes):
                existe = random.randint(0, 1)
                solucaoParcial = individuo.getSolucaoParcial()
                solucaoParcial[y].setSelecionado(existe)

            individuos.append(individuo)

        return individuos
    
    def calculaFitnessTotal(self, individuosSorteados):
        fitnessTotal = 0

        for x in range(len(individuosSorteados)):
            fitnessTotal += individuosSorteados[x].getFitness()

        return fitnessTotal
    
    def calculaProbabilidade(self, individuosSorteados, fitnessTotal):
        print('Quantidade de individuos restante', len(individuosSorteados), 'Fitness Total', fitnessTotal)
        for x in range(len(individuosSorteados)):
            individuosSorteados[x].setProbabilidade(individuosSorteados[x].getFitness() / fitnessTotal)
            print('x:', individuosSorteados[x].id, individuosSorteados[x].geracao, 'Probabilidade:', individuosSorteados[x].getProbabilidade(), 'Fitness', individuosSorteados[x].getFitness())

    def sorteiaIndividuo(self, individuosSorteados):
        numeroSorteado = random.random()
        somaProbabilidade = 0
        ciclo = len(individuosSorteados)
        fitnessTotal = self.calculaFitnessTotal(individuosSorteados)
        individuoSorteado = None

        for x in range(ciclo):
            somaProbabilidade += individuosSorteados[x].getProbabilidade()

            if numeroSorteado <= somaProbabilidade:
                print('\nNumero Sorteado:', numeroSorteado)
                self.calculaProbabilidade(individuosSorteados, fitnessTotal)
                individuoSorteado = individuosSorteados[x]
                break

            if x == (ciclo - 1):
                print('\nNumero Sorteado:', numeroSorteado)
                self.calculaProbabilidade(individuosSorteados, fitnessTotal)
                individuoSorteado = individuosSorteados[x]
                break

        if individuoSorteado:
            individuosSorteados.remove(individuoSorteado)
            print(individuoSorteado.id, individuoSorteado.geracao, 'foi sorteado', individuoSorteado.probabilidade, 'e foi removido da lista')

        return individuoSorteado
    
    def geraPares(self, individuosSorteados):
        pares = []

        ciclo = int(self.numeroIndividuos / 2)

        for x in range(ciclo):
            par = []

            par.append(self.sorteiaIndividuo(individuosSorteados))

            par.append(self.sorteiaIndividuo(individuosSorteados))
            pares.append(par)

        return pares
    
    def criaIndividuo(self, filho, individuos, proximaGeracao):
        genes = self.geraGenes()

        for x in range(self.numeroGenes):
            genes[x].setSelecionado(filho[x])
        
        indice = len(individuos) % self.numeroGenes 

        individuo = Individuo(indice, genes, proximaGeracao)

        return individuo

    
    def realizaReproducao(self, pares, individuos, proximaGeracao):
        pai1 = []
        pai2 = []
        filho1 = []
        filho2 = []

        for x in range(self.numeroIndividuos // 2):
            numeroSorteado = random.randint(0, self.numeroGenes - 1)
            pai1 = pares[x][0].getSolucaoFinal()
            pai2 = pares[x][1].getSolucaoFinal()

            for x in range(self.numeroGenes):
                if x <= numeroSorteado:
                    filho1.append(pai1[x])
                    filho2.append(pai2[x])
                else:
                    filho1.append(pai2[x])
                    filho2.append(pai1[x])

            individuos.append(self.criaIndividuo(filho1, individuos, proximaGeracao ))
            individuos.append(self.criaIndividuo(filho2, individuos, proximaGeracao ))

            filho1 = []
            filho2 = []

        return individuos
    
    def realizaMutacao(self, individuos):
        numeroSorteado = random.random()
        
        if numeroSorteado > self.taxaMutacao:
            print('Nao havera mutacao nesta geracao')
            return individuos
        
        print('Havera mutacao nesta geracao')

        individuos = sorted(individuos, key=lambda ind: ind.getFitness(), reverse=True)
        individuosSorteados = individuos.copy()
        
        print('Calculando o Fitness Total da Geracao para Mutacao')
        fitnessTotal = self.calculaFitnessTotal(individuosSorteados)
            
        self.calculaProbabilidade(individuosSorteados, fitnessTotal)

        for x in range(len(individuosSorteados)):
            print(individuosSorteados[x].id, individuosSorteados[x].geracao, 'Probabilidade:', individuosSorteados[x].getProbabilidade(), 'Fitness', individuosSorteados[x].getFitness())

        individuoSorteado = self.sorteiaIndividuo(individuosSorteados)


        if individuoSorteado:
            sorteioGene = random.randint(0, self.numeroGenes - 1)
            print('Gene', sorteioGene, 'do individuo', individuoSorteado.id, 'sera mutado')
            
            individuoSorteado.mutacao(sorteioGene)
            individuosSorteados.append(individuoSorteado)

        return individuosSorteados
    

    def realizaAjustePopulacional(self, individuos):
        x = 0
        individuos = sorted(individuos, key=lambda ind: ind.getFitness(), reverse=True)

        while len(individuos) > self.numeroIndividuos:
            if x >= len(individuos):
                break

            if individuos[x].getPeso() > self.capacidadeMochila and len(individuos) > self.numeroIndividuos:
                print('Individuo', individuos[x].getPeso(), 'sera removido da populacao')
                individuos.remove(individuos[x])
            else:
                # Remover os individuos com menor fitness
                individuos.pop()

            x += 1

        return individuos


    


    def inicializa(self):

        if (self.numeroIndividuos % 2) != 0:            
            return print('Quantidade de individuos deve ser par')

        random.seed()
        individuos = []

        individuos = self.geraPrimeiraGeracao()

        print('\nGerando a Primeira Geracao:')
        for x in range(self.numeroIndividuos):
            individuos[x].adicionaSolucaoFinal()

        # Ordena os elementos da primeira geração
        individuos = sorted(individuos, key=lambda ind: ind.getFitness(), reverse=True)


        print('Calculando o Fitness Total da Primeira Geracao')
            
        for proximaGeracao in range(self.condicaoParada):
            individuos = self.repetePassos(individuos, proximaGeracao + 2)
            
        
    def repetePassos(self, individuos, proximaGeracao):
        if proximaGeracao > self.condicaoParada:
            return 
        
        individuosSorteados = individuos.copy()
        
        
        fitnessTotal = self.calculaFitnessTotal(individuosSorteados)
        self.calculaProbabilidade(individuosSorteados, fitnessTotal)
        
        for x in range(self.numeroIndividuos):
            print('x:', individuos[x].id, individuos[x].geracao)
            print('Fitness:', individuos[x].getFitness())
            print('Solucao Final:', individuos[x].getSolucaoFinal())
            print('Probabilidade:', individuos[x].getProbabilidade())
            print()
                
        pares = self.geraPares(individuosSorteados)

        print('\nGerando Pares:')
        for x in range(len(pares)):
            print('Par:', pares[x][0].id, pares[x][0].geracao, 'e', pares[x][1].id, pares[x][1].geracao)

        individuos = self.realizaReproducao(pares, individuos, proximaGeracao)
        
        print('\nDepois da reproducao')
        for x in range(len(individuos)):
            individuos[x].adicionaSolucaoFinal()

        individuos = self.realizaMutacao(individuos)
        individuos = self.realizaAjustePopulacional(individuos)

        print('\n\nAjuste Populacional')
        for x in range(len(individuos)):
            individuos = sorted(individuos, key=lambda ind: ind.getFitness(), reverse=True)
            print(individuos[x].id, individuos[x].geracao, 'Fitness', individuos[x].getFitness())
            
        return individuos