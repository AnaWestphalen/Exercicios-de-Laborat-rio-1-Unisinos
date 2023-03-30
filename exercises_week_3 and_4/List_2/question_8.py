# Crie um programa que pergunta para o usuário (via Teclado) quantos números ele irá digitar
# e armazena em uma variável chamada quant. Logo após, faça com que o usuário digite quant números inteiros,
# e para cada número digitado imprima na tela se o número é negativo, positivo ou zero.

def typeNumber():
  quant = int(input("Quantos números você vai digitar? "))
  count = 1

  while count <= quant:
    number = int(input("Digite um número inteiro: "))
    if (number > 0):
      print("O número digitado é positivo!")
    elif (number < 0):
      print("O número digitado é negativo!")
    else:
      print("O número digitado é zero!")
    count += 1

typeNumber()
