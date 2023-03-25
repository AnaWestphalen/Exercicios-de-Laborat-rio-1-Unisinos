# Crie um programa em Python que recebe os valores inteiros
# a, b e c e retorna as duas raízes da equação de segundo grau correspondente.

A = int(input("Digite A: "))
B = int(input("Digite B: "))
C = int(input("Digite C: "))

delta = (B ** 2) - (4 * A * C)
positiveX = ((B * -1) + (delta ** (1 / 2))) / (2 * A)
negativeX = ((B * -1) - (delta ** (1 / 2))) / (2 * A)

print("***** Raizes da equação *****")
print("x' =",positiveX)
print("x'' =",negativeX)
