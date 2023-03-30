# Crie um programa que pede para o usuário digitar números positivos via Teclado.
# Quando o usuário digitar um número negativo, informe a média de todos os números que ele informou.

def averageNumbers():
  result = 0
  count = 0

  while True:
    value = int(input("Digite um número positivo (negativo se quiser sair): "))
    if value < 0:
      break
    result += value
    count += 1

  average = result / count

  print("Média dos números digitados é:",average)

averageNumbers()
