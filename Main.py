from classes import Setor, Colaborador, Empresa
from utilidades import removee_acecuacoes,is_cnpj_valido


print(removee_acecuacoes("Noção"))

# setor = Setor(nome="Recursos humanos", localizacao="Segundo andar", centro_de_custo="Administrativo")
# ti = Setor("T.I", centro_de_custo="Administrativo", localizacao="Filial 003")
# print(ti)

# colega001 = Colaborador("Marcelo", ti, 10000, "98765")

# print(colega001.setor.localizacao)

# print(colega001.infoSetor())

# cnpj = ""

# while len(cnpj) == 0:
#     userdata = input("")
#     if(is_cnpj_valido(userdata)):
#         cnpj = userdata

empresa = Empresa(nome="Apple", cnpj="84.854.728/0001-70")

rh = Setor(nome="Recursos humanos", localizacao="Segundo andar", centro_de_custo="Administrativo")

empresa.addSetor(rh)
empresa.addSetor(Setor(nome="Compras", localizacao="Primeiro andar", centro_de_custo="Administrativo"))

for setor in empresa.setores:
    print(setor)

colab01 = Colaborador("Marlise", 28.00, "59354001")
presidente = Colaborador("Luis", 350.00, "1")

rh.addColab(colab01)

for i in rh.colabs():
    print(i)


empresa.setores[1].addColabs([
    Colaborador("Joana", 18.00, "cj3"),
    Colaborador("Juliane", 20.00, "cj4"),
    Colaborador("Estela", 23.00, "cj8"),
    Colaborador("Sheila", 22.00, "cj9"),
    Colaborador("Shimejia", 30.00, "cj2"),
    presidente
])

for y in empresa.setores[1].colabs():
    print(y)




# colaborador = Colaborador(nome="Luiz", salario=1.549, id="14622", setor="Compras")

# colaborador = Colaborador("Luiz",1.549,"14622","Compras")

# empresa = [
#     Colaborador("Luiza", 10.0, "123", "RH"),
#     Colaborador("Marcia", 22.0, "123", "RH"),
#     Colaborador("Suzana", 36.0, "123", "RH"),
#     Colaborador("Vera", 87.0, "123", "RH")
# ]