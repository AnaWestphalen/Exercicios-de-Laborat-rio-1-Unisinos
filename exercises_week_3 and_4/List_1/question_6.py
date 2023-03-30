# Crie um programa que aplica uma taxa de juros em um determinado preço
# digitado pelo teclado. A taxa aplicada deve ser:
# • Aumento de 10% caso o valor seja menor do que 100
# • Aumento de 20% caso o valor esteja entre 100 (inclusive) e 300
# • Aumento de 50% caso o valor esteja entre 300 (inclusive) e 1000
# • Aumento de 60% caso o valor esteja seja maior que 1000
# • Imprima uma mensagem de erro se o valor for negativo
# • Ao final, seu programa deve imprimir o novo valor, já com a taxa aplicada.

def interestRate():
  price = int(input("Digite o preço do produto: R$"))

  rateA = (price * 0.10) + price
  rateB = (price * 0.20) + price
  rateC = (price * 0.50) + price
  rateD = (price * 0.60) + price

  if (0 < price < 100) :
    print("O novo preço do produto é R$", rateA)
  elif (100 <= price < 300) :
    print("O novo preço do produto é R$", rateB)
  elif (300 <= price < 1000) :
    print("O novo preço do produto é R$", rateC)
  elif (price <= 0):
    print("Preço do produto é inválido!")
  else:
    print("O novo preço do produto é R$", rateD)

interestRate()
