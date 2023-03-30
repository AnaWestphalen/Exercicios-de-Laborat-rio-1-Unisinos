# Crie um programa que pede para o usuário digitar o nome de 13 pessoas pelo teclado.

def listNames():
  count = 1

  while count <= 13:
    name = input("Digite o nome de uma pessoa: ")
    count += 1

listNames()
