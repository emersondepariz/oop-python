from classes import ContaBancaria, ContaCorrente, ContaSalario


contas = [
    ContaBancaria("2387654","0001", 10),
    ContaBancaria("2387653","0001"),
    ContaBancaria("2387652","0003", 345.27)
]

print(contas[0].get_saldo())

for conta_bancaria in contas:
    print(conta_bancaria)


contCor = [
    ContaCorrente("659845","0001", 5000000),
    ContaCorrente("659844","0001", 500),
    ContaCorrente("654895","0044", 45.69)
]

#contCor[1].set_saldo(200.00)

print(f"R$ {contCor[1].get_saldo()}")

for conta_corrente in contCor:
    print(conta_corrente)


contSal = [
    ContaSalario("65695","0001", 4000),
    ContaSalario("54953","0044", 325.65),
    ContaSalario("54694","0001", 40.00)
]

for conta_salario in contSal:
    print(conta_salario)

print(contSal[2].set_saldo(400.00))


