# Crie um programa que permita que o usuário crie sua lista de compras. Primeiramente, solicite que ele
# informe quantos produtos serão adicionados na lista. Depois disto, peça para que o usuário digite
# os produtos que ele vai comprar, e armazene em uma lista. Ao final, imprima a lista de compras do usuário.

def supermarketList():
  amount = int(input("Digite quantos produtos você irá comprar: "))

  marketList = []

  for i in range(0,amount):
    marketList.append(input("Digite o nome do produto: "))

  print("=========================================")
  print("Sua lista de compras de hoje é:")
  print("                                  ")
  for product in marketList:
    print(product)

  print("=========================================")

supermarketList()
