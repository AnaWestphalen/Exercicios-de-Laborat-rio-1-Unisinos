# Crie um programa que faça a soma dos valores de 0 até 198.

def sumNumbers():
  count = 0
  add = 0

  while count <= 198:
    add += count
    count += 1

  print(f"A soma dos números entre 0 e 198 é",add)

sumNumbers()
