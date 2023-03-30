# Crie um programa que imprime os números primos entre 0 e 200, imprimindo ao final a add destes números.

def sumPrimeNumber():
  add = 0
  number = 0

  while number < 200:
    divisor = 2
    isPrime = True

    while divisor < number:
      if number % divisor == 0:
        isPrime = False
        break
      divisor += 1

    if isPrime:
      print(number)
      add += number
    number += 1

  print("Somatório dos números primos entre 0 e 200 é:", add)

sumPrimeNumber()
