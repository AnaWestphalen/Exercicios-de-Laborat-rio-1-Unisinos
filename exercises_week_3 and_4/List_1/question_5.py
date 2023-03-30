# Crie um programa que recebe o preço de um produto pelo teclado e imprime na
# tela a mensagem adequada, de acordo com o preço:
# • “Preço inválido”, se o preço for negativo ou zero
# • “Preço baixo”, se o preço for entre 0 e 30 (inclusive)
# • “Preço médio”, se o preço for entre 30 e 50 (inclusive)
# • “Preço alto”, se o preço for maior do que 50

def priceClassification():
  price = int(input("Digite o preço do produto: R$"))

  if (price <= 0) :
    print("Preço inválido!")
  elif (0 < price <= 30) :
    print("Preço baixo!")
  elif (30 < price <= 50) :
    print("Preço médio!")
  else:
    print("Preço alto!")

priceClassification()
