# Faça um programa que escreva na tela todos os valores inteiros entre dois valores digitados pelo usuário (num1 e num2).
# Caso num1 seja maior do que num2, seu programa deve imprimir os valores entre num1 e num2 da mesma forma.
def intervalNumbers():
  num1 = int(input("Digite um número inteiro: "))
  num2 = int(input("Digite outro número inteiro: "))
  minValue = min(num1, num2)
  maxValue = max(num1, num2)
  count = minValue + 1

  while (count < maxValue):
    print(count)
    count += 1

intervalNumbers()
