# Crie um programa que solicita ao usuário que ele defina sua senha. A senha deve ser um texto (string)
# composto apenas por dígitos e deve ter entre 5 e 10 valores. O usuário tem apenas 6 chances de definir
# corretamente a senha. Caso ele defina corretamente a senha nas tentativas que ele tem, imprima uma mensagem de sucesso.
# Caso ele não defina a senha corretamente, imprima uma mensagem de insucesso. Dica: na aula aprendemos a ver
# se uma string é formada apenas por dígitos e aprendemos a descobrir o tamanho do texto digitado.

def authentication():
  attempt = 6

  for i in range(attempt):
    password = input("Defina uma senha com 5 a 10 dígitos: ")
    if (password.isdigit() == True) and (5 <= len(password) <= 10):
      print("Senha definida com sucesso!")
      break
    else:
      attempt -= 1
      print("Você errou!Tente novamente.")

  if (attempt == 0):
    print("NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO! Tente novamente mais tarde.")

authentication()
