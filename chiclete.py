def IEC60062(resistencia):
    dicionario_res = {'m': 10**-3, '-': 1, 'K': 10**3, 'M': 10**6, 'G': 10**9}
    cores = ['Preta', 'Marrom', 'Vermelha', 'Laranja', 'Amarela', 'Verde', 'Azul', 'Violeta', 'Cinza', 'Branca']
    dicionario_tol = {'Nenhuma': 20, 'Rosa': 0, 'Prata': 10, 'Dourada': 5, 'Preta': 0, 'Marrom': 1, 'Vermelha': 2, 'Laranja': 0.05, 'Amarela': 0.02, 'Verde': 0.5, 'Azul': 0.25, 'Violeta': 0.1, 'Cinza': 0.01, 'Branca': 0}

    info_res = resistencia.split(" ")
    if len(info_res) == 2:
        info_res.append('')

    valor, multiplicador, tolerancia = info_res
    if not valor.replace(".", "").isdigit():
        raise ValueError(f"Valor inválido: {valor}")
    if multiplicador[-1] not in dicionario_res:
        raise ValueError(f"Multiplicador inválido: {multiplicador}")

    valor = float(valor) * dicionario_res[multiplicador[-1]]
    numero = int(valor * 10**6)

    resistencia_cor = []
    for i in range(2):
        resistencia_cor.append(cores[numero % 10])
        numero //= 10

    if numero > 0:
        resistencia_cor.append(cores[int(math.log10(numero))+1])

    resistencia_cor.append(list(dicionario_tol.keys())[list(dicionario_tol.values()).index(tolerancia)])
    resistencia_cor.reverse()

    return resistencia_cor
