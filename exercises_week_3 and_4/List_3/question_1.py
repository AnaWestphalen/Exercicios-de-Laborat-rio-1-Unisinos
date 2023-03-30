def fluxogram():
  count = 0

  while (count < 10):
    number = int(input("digite um número: "))
    if (number < 0):
      print("Número negativo")
    elif (number > 0):
      print("Número positivo")
    else:
      print("Zero")

    count += 1

fluxogram()
