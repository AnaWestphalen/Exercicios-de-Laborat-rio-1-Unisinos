# Crie um programa que recebe dois valores inteiros pelo teclado e imprime
# qual dos dois é maior.

def bigNumber():
  numA = int(input("Digite um número: "))
  numB = int(input("Digite outro número: "))

  if (numA > numB) :
    print("O maior número é",numA)
  else:
    print("O maior número é",numB)

bigNumber()
