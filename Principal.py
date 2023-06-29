from ProblemaMochila import ProblemaMochila

class Principal:
    def __init__(self):
        pass

    def main(self):
        problema = ProblemaMochila(8, 8, 0.05, 5000, 8) #(numeroIndividuos, numeroGenes, taxaMutacao, capacidadeMochila, condicaoParada):
        problema.inicializa()

Principal().main()