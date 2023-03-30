# Exercício 9. Faça novamente todos os exercícios das listas de exercícios sobre WHILE,
# porém utilizando o for para realizar a repetição.

#*************************************************************LISTA 2******************************************************

# Lista 2 - questão 1: Crie um programa que pede para o usuário digitar o nome de 13 pessoas pelo teclado.
def listNames():
  count = 13

  for i in range(count):
    name = input("Digite o nome de uma pessoa: ")
    count -= 1

listNames()

# Lista 2 - questão 2: Crie um programa que imprime os números de 0 a 1000.
def printToThousand():
  for i in range(1, 1001):
    print(i)

printToThousand()

# Lista 2 - questão 3: Crie um programa que imprime os números pares de 0 a 2000.
def printToTwoThousand():
  for i in range(0, 2001):
    if (number % 2 == 0):
      print(number)

printToTwoThousand()

# Lista 2 - questão 4: Crie um programa que imprime os números de 0 a 1000 em ordem decrescente (ou seja, de 1000 a 0).
def upToZero():
  for number in range(1000, -1, -1):
    print(number)

upToZero()

# Lista 2 - questão 5: Crie um programa que solicita o time de 10 usuários pelo teclado. Ao final,
# imprima quantos torcedores torcem para o Grêmio.
def listTeams():
  count = 10
  teamGremio = 0

  for i in range(count):
    team = input("Digite o nome do seu time do coração: ")
    if (team.lower() == "grêmio") or (team.lower() == "gremio"):
      teamGremio += 1
    count -= 1

  print("O número de torcedores do Grêmio é:",teamGremio)

listTeams()

# Lista 2 - questão 6: Crie um programa que pede para o usuário digitar 20 números com ponto flutuante pelo teclado. Ao final,
# seu programa deve imprimir todos os números digitados. Dica: armazene-os em uma string e concatene os valores digitados. No final,
# imprima a string.
def listFloats():
  count = 20
  floats = ""

  for i in range(count):
    number = input("Digite um número decimal: ")
    floats = floats + str(number) + "\n"
    count -= 1

  print("Os valores digitados foram:\n"+floats)

listFloats()

# Lista 2 - questão 7: Crie um programa que solicita para o usuário que ele digite 10 valores inteiros.
# Ao final, imprima a soma de todos os valores digitados.
def sumNumbers():
  sum = 0
  count = 10

  for i in range(count):
    number = int(input("Digite um número inteiro: "))
    sum += number
    count -= 1

  print(f"A soma dos números digitados é",sum)

sumNumbers()

# Lista 2 - questão 8: Crie um programa que pergunta para o usuário (via Teclado) quantos números ele irá digitar
# e armazena em uma variável chamada quant. Logo após, faça com que o usuário digite quant números inteiros,
# e para cada número digitado imprima na tela se o número é negativo, positivo ou zero.
def typeNumber():
  quant = int(input("Quantos números você vai digitar? "))

  for i in range(quant):
    number = int(input("Digite um número inteiro: "))
    if (number > 0):
      print("O número digitado é positivo!")
    elif (number < 0):
      print("O número digitado é negativo!")
    else:
      print("O número digitado é zero!")
    quant -= 1

typeNumber()

# Lista 2 - questão 9: Crie um programa que pede para o usuário digitar 2 valores inteiros via Teclado (val1 e val2).
# Se nenhum dos valores for negativo, escreva os números pares entre o menor e o maior valor.
def evenNumbers():
  val1 = int(input("Digite um número inteiro: "))
  val2 = int(input("Digite outro número inteiro: "))
  minValue = min(val1, val2)
  maxValue = (max(val1, val2) + 1)


  if (val1 > 0) and (val2 > 0):
    for i in range(minValue, maxValue):
      if (minValue % 2 == 0):
        print(minValue)
      minValue += 1
  else:
    print("Você inseriu um valor negativo")

evenNumbers()

# Lista 2 - questão 10: Crie um programa que faça a soma dos valores de 0 até 198.
def sumNumbers():
  count = 0
  add = 0

  for i in range(0, 199):
    add += count
    count += 1

  print(f"A soma dos números entre 0 e 198 é",add)

sumNumbers()

# Lista 2 - questão 11: Crie um programa que imprima a soma dos valores pares e a soma dos valores ímpares entre dois números
# quaisquer digitados pelo usuário.
def sumNumbers():
  val1 = int(input("Digite um número inteiro: "))
  val2 = int(input("Digite outro número inteiro: "))
  sumEven = 0
  sumOdd = 0
  count = val1
  max = (val2 - 1)

  if (val1 < val2):
    for i in range(max):
      if (count % 2 == 0):
        sumEven += count
      else:
        sumOdd += count
      count += 1
    print("A soma dos números pares é",sumEven)
    print("A soma dos números ímpares é",sumOdd)
  else:
    print("Erro, o valor do primeiro número é maior ou igual ao do segundo número digitado.")

sumNumbers()

# Lista 2 - questão 12: Crie um programa que pede para o usuário digitar números positivos via Teclado.
# Quando o usuário digitar um número negativo, informe a média de todos os números que ele informou.
def sumPositiveNumbers():
  result = 0
  count = 0

  for value in range(1, 10000):
    value = int(input("Digite um número positivo (negativo para sair): "))
    if (value > 0):
      result += value
      count += 1
    else:
      average = result / count
      print("A soma dos números positivos digitados é: ",average)
      break

sumPositiveNumbers()

# Lista 2 - questão 13: Crie um programa que calcule o fatorial de um número informado pelo usuário (não permita números negativos).
def factorial():
  number = int(input("Digite um número para ser calculado seu fatorial: "))
  count = 1
  result = 1

  if (number > 0):
    for i in range(number):
      result *= count
      count += 1
    print("O fatorial desse número é:",result)
  else:
    print("Erro! Você digitou um número negativo!")

factorial()

# Lista 2 - questão 14: Crie um programa que diga se o número informado pelo usuário é primo ou não.
def primeNumber():
  number = int(input("Digite um número inteiro: "))

  if (number > 1):
    for i in range(2, number):
      if (number % i) == 0:
        print("O número não é primo.")
        break
    else:
      print("O número informado é primo.")
  else:
    print("O número informado não é primo.")

primeNumber()

# Lista 2 - questão 15: Crie um programa que imprime os números primos entre 0 e 200, imprimindo ao final a soma destes números.
def sumPrimeNumber():
  add = 0
  count = 0

  for number in range(2, 201):
    count = 0

    for i in range(1, number + 1):
      if number % i == 0:
        count += 1

    if (count == 2):
      print(number)
      add += number

  print("Somatório dos números primos entre 0 e 200 é:", add)

sumPrimeNumber()

#*************************************************************LISTA 3******************************************************
# Lista 3 - questão 1:
def fluxogram():

  for i in range(10):
    number = int(input("digite um número: "))
    if (number < 0):
      print("Número negativo")
    elif (number > 0):
      print("Número positivo")
    else:
      print("Zero")

fluxogram()

# Lista 3 - questão 2: Faça um programa que escreva na tela todos os números inteiros entre 0 (inclusive) e 1000 (inclusive).
def upToThousand():
  for number in range(0, 1001):
    print(number)

upToThousand()

# Lista 3 - questão 3: Faça um programa que escreva na tela todos os valores inteiros que estão entre dois valores digitados pelo usuário
# (num1 e num2). Caso num1 seja maior do que num2, imprima uma mensagem de erro e não imprima.
def intervalNumbers():
  num1 = int(input("Digite um número inteiro: "))
  num2 = int(input("Digite outro número inteiro: "))
  count = num1 + 1

  if (num1 < num2):
    for i in range(num1 + 1, num2):
      print(i)
  else:
    print("Erro, o valor do primeiro número é maior ou igual ao do segundo número digitado.")

intervalNumbers()

# Lista 3 - questão 4: Faça um programa que escreva na tela todos os valores inteiros entre dois valores digitados pelo usuário (num1 e num2).
# Caso num1 seja maior do que num2, seu programa deve imprimir os valores entre num1 e num2 da mesma forma.
def intervalNumbers():
  num1 = int(input("Digite um número inteiro: "))
  num2 = int(input("Digite outro número inteiro: "))
  minValue = min(num1, num2)
  maxValue = max(num1, num2)
  count = minValue + 1

  for i in range(count, maxValue):
    print(i)

intervalNumbers()

# Lista 3 - questão 5: Faça um programa que imprima na tela a soma de todos os valores entre 1 e 1000.
def sumNumbers():
  count = 0
  add = 0

  for i in range(1, 1001):
    add += count
    count += 1

  print(f"A soma dos números entre 1 e 1000 é",add)

sumNumbers()

# Lista 3 - questão 6: Faça um programa que solicita ao usuário que ele digite números que sejam positivos e pares. Quando
# o usuário digitar um número que não seja o solicitado, imprima na tela a soma dos valores positivos e pares digitados.
def sumEvenNumbers():
  result = 0

  for value in range(1, 10000):
    value = int(input("Digite um número positivo e par (negativo ou ímpar para sair): "))
    if (value > 0) and (value % 2 == 0):
      result += value
    else:
      print("A soma dos números positivos e pares digitados é: ",result)
      break

sumEvenNumbers()

# Lista 3 - questão 7: O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um
# programa que solicita ao usuário que ele digite seu usuário e senha. O programa só termina
# quando ele acertar o usuário e a senha. Quando ele acertar, você deve informar a mensagem: LOGIN EFETUADO COM SUCESSO.

def authentication():

  for i in range(1, 1000):
    user = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")

    if (user == "USER10") and (password == "PASSWORD1234"):
      print("LOGIN EFETUADO COM SUCESSO.")
      break
    else:
      print("Não foi possível efetuar o login. Tente novamente!")

authentication()

# Lista 3 - questão 8: O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um programa que
# solicita ao usuário que ele digite seu usuário e senha. O programa termina quando ele
# acertar o usuário e a senha ou quando ele exceder o máximo de 3 tentativas. Quando ele acertar, o programa deve
# informar a mensagem: LOGIN EFETUADO COM SUCESSO. Caso ele exceda a quantidade de tentativas, o
# programa deve informar a mensagem: NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO!

def authentication():
  attempt = 3

  for i in range(attempt):
    user = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")

    if (user == "USER10") and (password == "PASSWORD1234"):
      print("LOGIN EFETUADO COM SUCESSO.")
      break
    else:
      attempt -= 1
      print("Não foi possível efetuar o login. Tente novamente!")

  if (attempt == 0):
    print("NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO! Tente novamente mais tarde.")

authentication()
