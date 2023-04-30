import math

def add(n1, n2):
  return n1 + n2

def subtraction(n1, n2):
  return n1 - n2

def multiplication(n1, n2):
  return n1 * n2

def division(n1, n2):
  return n1 / n2

def potentiation(n1, n2):
  return n1 ** n2

def rooting(n1)
  return math.sqrt(n1):

def menu()
  option = 6 #-1
  while option < 0 or

option_menu = menu()
while option_menu != 0:
  print("\n------------------------------------------------------")
  num1 = int(input("Digite o primeiro valor: "))
  num2 = int(input("Digite o segundo valor: "))
  print("\n------------------------------------------------------")

  if (option_menu == 1):
    print("\n{} + {}".format(num1, num2))
    print("SOMA: {}".format(add(num1, num2)))
  elif (option_menu == 2):
    print("\n{} - {}".format(num1, num2))
    print("SUBTRAÇÃO: {}".format(subtraction(num1, num2)))
  elif (option_menu == 3):
    print("\n{} * {}".format(num1, num2))
    print("MULTIPLICAÇÃO: {}".format(multiplication(num1, num2)))
  elif (option_menu == 4):
    print("\n{} / {}".format(num1, num2))
    print("Divisão: {:.2f}".format(division(num1, num2)))
  elif (option_menu == 4):
    print("\n{} / {}".format(num1, num2))
    print("Divisão: {:.2f}".format(division(num1, num2)))
  elif (option_menu == 4):
    print("\n{} / {}".format(num1, num2))
    print("Divisão: {:.2f}".format(division(num1, num2)))

  option_menu = menu()
print("\nFinalizando!")
