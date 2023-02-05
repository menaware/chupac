def IEC60062(valor_string):
  valor, tolerancia = valor_string.split(" ")
  
  multiplicadores = {
      "m": 10**-3,
      "-": 1,
      "K": 10**3,
      "M": 10**6,
      "G": 10**9
  }
  
  fator_multiplicador = multiplicadores[valor[-1]]
  valor_numerico = float(valor[:-1]) * fator_multiplicador
  
  cores = [      "preto",      "marrom",      "vermelho",      "laranja",      "amarelo",      "verde",      "azul",      "violeta",      "cinza",      "branco"  ]
  
  tolerancias = {
      "1": "dourado",
      "2": "prateado"
  }
  
  primeira_cor = cores[int(valor_numerico / 100)]
  segunda_cor = cores[int((valor_numerico / 10) % 10)]
  terceira_cor = cores[int(valor_numerico % 10)]
  cor_tolerancia = tolerancias[tolerancia]
  
  return [primeira_cor, segunda_cor, terceira_cor, cor_tolerancia]
