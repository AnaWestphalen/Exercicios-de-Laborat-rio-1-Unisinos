# Faça um programa que imprima na tela a soma de todos os valores entre 1 e 1000.

def sumNumbers():
  count = 0
  add = -1

  while count < 1000:
    add += count
    count += 1

  print(f"A soma dos números entre 1 e 1000 é",add)

sumNumbers()
