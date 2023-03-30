# Crie um programa que imprime a tabuada de um número qualquer digitado pelo usuário.

def tabuada():
  tabuada = int(input("Digite o número que você quer saber a tabuada: "))

  for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada * (count+1)))

tabuada()
