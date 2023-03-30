# Crie um programa que imprime os números pares de 0 a 2000.

def upToTwoThousand():
  number = 0

  while (number < 2001):
    if (number % 2 == 0):
      print(number)
    number += 1

upToTwoThousand()
