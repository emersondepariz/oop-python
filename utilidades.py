from itertools import cycle
from removeaccents import remove_accents
from re import sub

LENGTH_CNPJ = 14


def is_cnpj_valido(cnpj: str) -> bool:
    cnpj = sub(r"[^\w\s]", '', cnpj)
    if len(cnpj) != LENGTH_CNPJ:
        return False

    if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
        return False

    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False

    return True

def removee_acecuacoes(frase:str) -> str:
    # accented_string is of type 'unicode'
    return remove_accents(frase)
    # unaccented_string contains 'Malaga'and is of type 'str'
