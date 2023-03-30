# Crie um programa que pede para o usuário digitar 2 valores inteiros via
# Teclado (val1 e val2). Se nenhum dos valores for negativo, escreva os números pares
# entre o menor e o maior valor.

def evenNumbers():
  val1 = int(input("Digite um número inteiro: "))
  val2 = int(input("Digite outro número inteiro: "))
  minValue = min(val1, val2)
  maxValue = max(val1, val2)


  if (val1 > 0) and (val2 > 0):
    while (minValue <= maxValue):
      if (minValue % 2 == 0):
        print(minValue)
      minValue += 1
  else:
    print("Você inseriu um valor negativo")

evenNumbers()
