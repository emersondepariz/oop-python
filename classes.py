class Agencia:
    def __init__(self, numero):
        self.numero = numero
    def __str__(self):
        return self.numero

class ContaBancaria:
    numero:str = ""
    agencia:str = ""
    # saldo:float = 0.00

    def __init__(self,numero:str,agencia:Agencia,saldo:float=0.00):
        self.saldo = 0.00
        self.numero = numero
        self.agencia = agencia
        self.set_saldo(saldo)
    
    def set_saldo(self, saldo:float) -> float:
        try:
            saldo = float(saldo)
        except ValueError as message:
            print(f"Informe um valor float ({type(saldo)} inserido):")
            print(message)
            exit()
        self.saldo += saldo
        return self.saldo
    def get_saldo(self):
        return self.saldo

    def __str__(self):
        return f"{self.agencia} {self.numero}" 


class ContaCorrente(ContaBancaria):
    def __str__(self):
        return f"Conta corrente: {self.agencia} {self.numero}"

class ContaSalario(ContaBancaria):
    def __init__(self, numero:str, agencia:str, saldo:float="") -> None:
        super().__init__(numero, agencia, saldo)
    # def set_saldo(self, saldo):
    
    #     super().set_saldo(saldo)