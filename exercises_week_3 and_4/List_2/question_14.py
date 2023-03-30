# Crie um programa que diga se o número informado pelo usuário é primo ou não.

def primeNumber():
  number = int(input("Digite um número: "))
  isPrime = True
  i = 2

  while i < number:
    if number % i == 0:
        isPrime = False
        break
    i += 1

  if isPrime:
    print("O número informado é primo")
  else:
    print("O número informado não é primo")

primeNumber()
