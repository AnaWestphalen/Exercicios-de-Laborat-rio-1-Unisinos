# Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.

def evenOrOdd():
  number = int(input("Digite um número "))

  if (number % 2 == 0):
    print("O número é par!")
  else:
    print("O número é ímpar!")

evenOrOdd()
