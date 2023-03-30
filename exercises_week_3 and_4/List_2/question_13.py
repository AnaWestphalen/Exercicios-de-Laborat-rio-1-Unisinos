# Crie um programa que calcule o fatorial de um número informado pelo usuário (não permita números negativos).

def factorial():
  number = int(input("Digite um número para ser calculado seu fatorial: "))
  count = 1
  result = 1

  if (number > 0):
    while (count <= number):
      result *= count
      count += 1
    print("O fatorial desse número é:",result)
  else:
    print("Erro! Você digitou um número negativo!")

factorial()
