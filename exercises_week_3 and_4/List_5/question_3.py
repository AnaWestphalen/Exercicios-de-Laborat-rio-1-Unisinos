# Crie um método que recebe um valor por parâmetro (assuma que será inteiro) e retorna a soma de todos os
# valores entre 0 e o valor recebido. Caso o valor seja negativo, o método deve retornar -1.

def sumValue(value):
  if value < 0:
    return -1
  else:
    addition = 0
    for i in range(value + 1):
      addition += i
    return addition
