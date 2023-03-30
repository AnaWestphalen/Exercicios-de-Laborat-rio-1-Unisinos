# Faça um programa que escreva na tela todos os valores inteiros que estão entre dois valores digitados pelo usuário
# (num1 e num2). Caso num1 seja maior do que num2, imprima uma mensagem de erro e não imprima.

def intervalNumbers():
  num1 = int(input("Digite um número inteiro: "))
  num2 = int(input("Digite outro número inteiro: "))
  count = num1 + 1

  if (num1 < num2):
    while (count < num2):
      print(count)
      count += 1
  else:
    print("Erro, o valor do primeiro número é maior ou igual ao do segundo número digitado.")

intervalNumbers()
