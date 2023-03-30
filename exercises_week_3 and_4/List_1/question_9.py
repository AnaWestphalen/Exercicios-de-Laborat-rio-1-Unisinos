# Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo
# teclado e imprime na tela se será necessário ou não realizar o Grau C (considere o
# sistema de avaliação da Unisinos). Caso algum valor informado seja negativo, informe
# uma mensagem de erro e não realize o cálculo.

def approval():
  grauA = int(input("Digite sua nota do Grau A: "))
  grauB = int(input("Digite sua nota do Grau B: "))

  if (grauA < 0 or grauB < 0):
    print("Nota inválida. Não é possível realizar o cálculo!")
  else:
    result = (0.3 * grauA) + (0.7 * grauB)
    if (result > 6):
      print("Parabéns, você está aprovado! Sua nota foi", result,"!")
    else:
      print("Que pena, você terá que realizar o Grau C! Sua nota foi", result,"!")

approval()
