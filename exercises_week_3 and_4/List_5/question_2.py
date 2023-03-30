# Crie um método chamado maiorValor que recebe 3 valores por parâmetro (assuma que serão inteiros) e
# retorna o maior dos três valores.

def maiorValor(val1, val2, val3):
  if (val1 > val2) and (val1 > val3) :
    return val1
  elif (val2 > val1) and (val2 > val3) :
    return val2
  else:
    return val3

maiorValor(val1, val2, val3)
