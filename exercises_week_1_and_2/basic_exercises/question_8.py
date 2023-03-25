grauAPratica = float(input("Digite sua nota da atividade prática: "))
grauATeorica = float(input("Digite sua nota da atividade teórica: "))

grauBProvaLab = float(input("Digite sua nota da prova em laboratório: "))
grauBTeste = float(input("Digite sua nota do teste teórico: "))
grauBTrabalho = float(input("Digite sua nota do trabalho extraclasse: "))

notaGrauA = (0.45 * grauAPratica) + (0.55 * grauATeorica)
notaGrauB = (0.60 * grauBProvaLab) + (0.20 * grauBTeste) + (0.20 * grauBTrabalho)
notaFinal = (0.33 * notaGrauA) + (0.67 * notaGrauB)

print("*****************************************")
print("Sua nota final é: {:.2}".format(notaFinal))
print("*****************************************")
