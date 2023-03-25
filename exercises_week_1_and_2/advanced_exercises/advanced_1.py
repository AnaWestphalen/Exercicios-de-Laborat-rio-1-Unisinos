# Faça um programa em Python que:
# – Receba um float digitado pelo usuário e armazena em A
# – Receba um inteiro digitado pelo usuário e armazene em B
# – Imprima as seguintes mensagens na tela (substitua o X e o Y pelo
# resultado da operação indicada na mensagem):
# • “A multiplicado por B é X”
# • “A dividido por B é X”
# • “A mais B é X e A menos B é Y”
# • “A elevado a B é X”

A = float(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

produto = (A * B)
divisao = (A / B)
soma = (A + B)
subtracao = (A - B)
potencia = (A ** B)

print("A multiplicado por B é:  {:.2}".format(produto))
print("A dividido por B é: {:.2}".format(divisao))
print("A mais B é {:.2}".format(soma),"e A menos B é {:.2}".format(subtracao))
print("A elevado a B é: {:.2}".format(potencia))
