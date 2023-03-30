# Crie um programa que recebe dois valores inteiros A e B pelo teclado e
# imprime o valor de A dividido por B. Entretanto, se o valor de B for 0, imprima uma
# mensagem de erro e não faça a divisão.

def division():
  A = int(input("Digite um número "))
  B = int(input("Digite outro número "))

  if (B != 0):
    print("O resultado da divisão é", A / B)
  else:
    print("Nâo foi possível realizar a divisão")

division()
