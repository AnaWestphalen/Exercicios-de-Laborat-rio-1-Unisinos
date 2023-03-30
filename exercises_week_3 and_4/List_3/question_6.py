# Faça um programa que solicita ao usuário que ele digite números que sejam positivos e pares. Quando o usuário digitar um
# número que não seja o solicitado, imprima na tela a soma dos valores positivos e pares digitados.

def sumEvenNumbers():
  result = 0
  count = 0

  while True:
    value = int(input("Digite um número positivo e par (negativo ou ímpar para sair): "))
    if (value < 0) or (value % 2 != 0):
      break
    result += value
    count += 1

  print("A soma dos valores positivos e pares digitados é:",result)

sum EvenNumbers()
