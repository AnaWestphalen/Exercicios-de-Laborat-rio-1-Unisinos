# Crie um programa que exibe um menu de calculadora na tela. O menu exibido deve ser o seguinte:
# • Digite 1 para somar dois valores
# • Digite 2 para subtrair dois valores
# • Digite 3 para multiplicar dois valores
# • Digite 4 para dividir dois valores
# • Digite 5 para realizar uma potência entre dois valores
# • Digite 6 para realizar uma radiciação entre dois valores
# • Digite qualquer outro número para sair
# De acordo com a opção informada pelo usuário, solicite os valores necessários para o
# usuário e imprima na tela o resultado da operação realizada.

def calculator():
  print("Bem vindo a Calculadora Python! Escolha uma das opções abaixo")
  print("=============================================================")
  print("Digite 1 para somar dois valores")
  print("Digite 2 para subtrair dois valores")
  print("Digite 3 para multiplicar dois valores")
  print("Digite 4 para dividir dois valores")
  print("Digite 5 para realizar uma potência entre dois valores")
  print("Digite 6 para realizar uma radiciação entre dois valores")
  print("Digite qualquer outro número para sair")
  print("=============================================================")
  option = int(input("Digite a opção escolhida: "))

  if (option == 1) :
    number1 = int(input("Digite um número: "))
    number2 = int(input("Digite outro número: "))
    addition = number1 + number2
    print("O resultado da soma foi:",addition)
  elif (option == 2) :
    number1 = int(input("Digite um número: "))
    number2 = int(input("Digite outro número: "))
    subtraction = number1 - number2
    print("O resultado da subtração foi:",subtraction)
  elif (option == 3) :
    number1 = int(input("Digite um número: "))
    number2 = int(input("Digite outro número: "))
    multiplication = number1 * number2
    print("O resultado da multiplicação foi:",multiplication)
  elif (option == 4) :
    number1 = int(input("Digite um número: "))
    number2 = int(input("Digite outro número: "))
    if number2 != 0:
      division = number1 / number2
      print("O resultado da divisão foi:",division)
    else:
      print("Não posso dividir por zero.")
  elif (option == 5) :
    number1 = int(input("Digite um número: "))
    number2 = int(input("Digite outro número: "))
    potentiation = number1 ** number2
    print("O resultado da potenciação foi:",potentiation)
  elif (option == 6) :
    number1 = int(input("Digite um número: "))
    number2 = int(input("Digite outro número: "))
    rooting = number1 ** (1/number2)
    print("O resultado da radiciação foi:",rooting)
  else:
    print("Obrigada por usar a Calculadora Python!")

calculator()
