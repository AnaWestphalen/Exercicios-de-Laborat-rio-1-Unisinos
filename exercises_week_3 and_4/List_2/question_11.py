# Crie um programa que imprima a soma dos valores pares e a soma dos
# valores ímpares entre dois números quaisquer digitados pelo usuário.

def sumNumbers():
  val1 = int(input("Digite um número inteiro: "))
  val2 = int(input("Digite outro número inteiro: "))
  sumEven = 0
  sumOdd = 0
  count = val1

  if (val1 < val2):
    while (count <= val2):
      if (count % 2 == 0):
        sumEven += count
      else:
        sumOdd += count
      count += 1
    print("A soma dos números pares é",sumEven)
    print("A soma dos números ímpares é",sumOdd)
  else:
    print("Erro, o valor do primeiro número é maior ou igual ao do segundo número digitado.")

sumNumbers()
