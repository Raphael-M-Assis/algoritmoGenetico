class Gene:
    def __init__(self, id, peso, valor):
        self.id = id
        self.peso = peso
        self.valor = valor
        self.selecionado = 0

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getSelecionado(self):
        return self.selecionado

    def setSelecionado(self, selecionado):
        self.selecionado = selecionado

    def __str__(self):
        return "id=" + str(self.id) + ", peso=" + str(self.peso) + ", valor=" + str(self.valor) + ", selecionado=" + str(self.selecionado) + "\n"
