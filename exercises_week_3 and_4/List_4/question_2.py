# Crie um programa que imprime na tela todos os valores entre dois valores digitados pelo teclado.

def printNumbers():
  val1 = int(input("Digite um número: "))
  val2 = int(input("Digite outro número: "))
  minValue = (min(val1, val2) + 1)
  maxValue = max(val1, val2)

  for i in range (minValue, maxValue):
    print(i)

printNumbers()
