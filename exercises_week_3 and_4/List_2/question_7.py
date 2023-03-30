# Crie um programa que solicita para o usuário que ele digite 10 valores
# inteiros. Ao final, imprima a soma de todos os valores digitados.

def sumNumbers():
  sum = 0
  count = 1

  while count <= 10:
    number = int(input("Digite um número inteiro: "))
    sum += number
    count += 1

  print(f"A soma dos números digitados é", sum)

sumNumbers()
