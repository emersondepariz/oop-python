from classes import ContaCorrente, ContaSalario, Agencia


# contas = [
#     ContaBancaria("2387654","0001", 10),
#     ContaBancaria("2387653","0001"),
#     ContaBancaria("2387652","0003", 345.27)
# ]

# print(contas[0].get_saldo())

# for conta_bancaria in contas:
#     print(conta_bancaria)


agencias = [
    Agencia("0001"),
    Agencia("0049"),
    Agencia("0003")
]

contCor = [
    ContaCorrente("659845", agencias[0]),
    ContaCorrente("659844", agencias[1], 500),
    ContaCorrente("654895", agencias[2], 45.69)
]

print(f"R$ {contCor[1].get_saldo()}")

for conta_corrente in contCor:
    print(conta_corrente)


contSal = [
    ContaSalario("65695",agencias[0], 4000),
    ContaSalario("54953",agencias[2], 325.65),
    ContaSalario("54694",agencias[1], 40.00)
]

for conta_salario in contSal:
    print(conta_salario)

print(contSal[2].set_saldo(400.00))

