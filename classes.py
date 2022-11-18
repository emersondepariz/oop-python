# import utilidades
from utilidades import is_cnpj_valido

class Setor:
    nome = ""
    localizacao = ""
    centro_de_custo = ""
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
    def __str__(self):
        # return f"""SETOR:{self.nome}
        # LOCALIZACAO: {self.localizacao}"""
        return f"SETOR:{self.nome}\n\t\tLOCALIZACAO: {self.localizacao}"
    
    def informacoes_setor(self, nome, localizacao, centro_de_custo):
        return f"O setor {self.nome} está localizado na {self.localizacao} e pertence o centro de custo {self.centro_de_custo}"
        return f"O setor {nome} está localizado na {localizacao} e pertence o centro de custo {centro_de_custo}"
    def informacoes_colaborador(self,nome, pessoa = ""):
        return f"O nome deste setor é {nome} e trabalha o funcionário {pessoa}"

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

class Colaborador:
    nome = ""
    salario = 0.0
    id = ""
    setor = Setor
    """
        O dunder init é chamado toda vez que uma classe é instanciada em um objeto
    """
    def __init__(self, nome:str, setor:Setor, salario:float=0.0, id:str=""):
        self.nome = nome
        self.salario = salario
        self.id = id
        self.setor = setor

    def infoSetor(self):
        return self.setor
    """
    O dunder str serve para descrever em forma de string uma classe
    """
    def __str__(self):
        return (f"O colaboradors {self.nome} recebe {self.salario} por mês, cujo id é {self.id} no setor {self.setor}")
        
    nome = ""
    cnpj = ""
    colaboradores = []
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
    def __str__(self):
        retorno = f"---{self.nome}---"
        for nome, cnpj in self.nome, self.cnpj:
            retorno (f"As empresas são {nome} e {cnpj}")
        return retorno