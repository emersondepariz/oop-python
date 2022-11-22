# import utilidades
from utilidades import is_cnpj_valido

class Colaborador:
    nome = ""
    salario = 0.0
    id = ""

    def __init__(self, nome:str, salario:float=0.0, id:str=""):
        self.nome = nome
        self.salario = salario
        self.id = id
    
    def __str__(self):
        return (f"({self.id}) {self.nome}")


class Setor:
    nome = ""
    localizacao = ""
    centro_de_custo = ""
    colaboradores = []
    def __init__(self, nome="", localizacao = "", centro_de_custo = ""):
        self.getNome(nome)
        self.localizacao = localizacao
        self.centro_de_custo = centro_de_custo
    def getNome(self, nome):
        if(len(nome) and len(nome) < 2):
            raise TypeError("O nome do setor não deve ser menor que dois caracteres.")
        elif (len(nome) == 0):
            self.nome = "Visitante"
        else:
            self.nome = nome
    
    def informacoes_setor(self, nome, localizacao, centro_de_custo):
        return f"O setor {self.nome} está localizado na {self.localizacao} e pertence o centro de custo {self.centro_de_custo}"
        return f"O setor {nome} está localizado na {localizacao} e pertence o centro de custo {centro_de_custo}"
    
    def colabs(self):
        return self.colaboradores
    
    def addColab(self, colab:Colaborador):
        self.colaboradores.append(colab)

    def addColabs(self, colabs:list):
        for colab in colabs:
            self.addColab(colab)


    def __str__(self):
        # return f"""SETOR:{self.nome}
        # LOCALIZACAO: {self.localizacao}"""
        return f"SETOR:{self.nome}\n\t\tLOCALIZACAO: {self.localizacao}"

class Empresa:
    nome = ""
    cnpj = ""
    endereco = ""
    setores = []
    
    def __init__(self, nome:str = "", cnpj:str = ""):
        self.nome = nome
        self.cnpj = self.setCnpj(cnpj)

    def setCnpj(self, cnpj:str):
        if len(cnpj) > 0 and is_cnpj_valido(cnpj) is False:
            raise TypeError("CNPJ inválido")
        return cnpj

    def addSetor(self, setor:Setor):
        if type(setor) is not Setor:
            raise TypeError("Desculpa, mas você é burro.")
        self.setores.append(setor)

