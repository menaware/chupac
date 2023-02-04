def IEC60062(res):
    res_dict = {'m': 10**-3, '-': 1, 'K': 10**3, 'M': 10**6, 'G': 10**9}
    colors = ['Preta', 'Marrom', 'Vermelha', 'Laranja', 'Amarela', 'Verde', 'Azul', 'Violeta', 'Cinza', 'Branca']
    tol_dict = {'Nenhuma': 20, 'Rosa': 0, 'Prata': 10, 'Dourada': 5, 'Preta': 0, 'Marrom': 1, 'Vermelha': 2, 'Laranja': 0.05, 'Amarela': 0.02, 'Verde': 0.5, 'Azul': 0.25, 'Violeta': 0.1, 'Cinza': 0.01, 'Branca': 0}

    res_info = res.split(" ")
    if len(res_info) == 2:
        res_info.append('')

    val, mult, tol = res_info
    if not val.replace(".", "").isdigit():
        raise ValueError(f"Invalid value: {val}")

    val = float(val) * res_dict.get(mult[-1], 1)
    num = int(val * 10**6)

    res = []
    for i in range(2):
        res.append(colors[num % 10])
        num //= 10

    if num > 0:
        res.append(colors[int(math.log10(num))+1])

    res.append(list(tol_dict.keys())[list(tol_dict.values()).index(tol)])
    res.reverse()

    return res
