# Crie um programa que pede para o usuário digitar 20 números com ponto
# flutuante pelo teclado. Ao final, seu programa deve imprimir todos os números
# digitados. Dica: armazene-os em uma string e concatene os valores digitados. No final,
# imprima a string.

def listFloats():
  count = 0
  floats = ""

  while (count <20):
    number = input("Digite um número decimal: ")
    floats = floats + str(number) + "\n"
    count += 1

  print("Os valores digitados foram:\n"+floats)

listFloats()
