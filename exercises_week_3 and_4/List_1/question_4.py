# Crie um programa que recebe três valores inteiros pelo teclado e imprime
# qual dos três é menor.

def smallerNumber():
  numA = int(input("Digite um número: "))
  numB = int(input("Digite outro número: "))
  numC = int(input("Digite outro número: "))

  if (numA < numB) and (numA < numC) :
    print("O menor número é",numA)
  elif (numB < numA) and (numB < numC) :
    print("O menor número é",numB)
  else:
    print("O menor número é",numC)

smallerNumber()
