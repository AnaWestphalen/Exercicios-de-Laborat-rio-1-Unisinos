# O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um programa que
# solicita ao usuário que ele digite seu usuário e senha. O programa termina quando ele
# acertar o usuário e a senha ou quando ele exceder o máximo de 3 tentativas. Quando ele acertar, o programa deve
# informar a mensagem: LOGIN EFETUADO COM SUCESSO. Caso ele exceda a quantidade de tentativas, o
# programa deve informar a mensagem: NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO!

def authentication():
  attempts = 0
  check = False
  user = input("Digite seu usuário: ")
  password = input("Digite sua senha: ")

  while (user != "USER10") or (password != "PASSWORD1234"):
    print("Não foi possível efetuar o login. Usuário ou senha inválidos.")
    user = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")
    attempts += 1

    if (user == "USER10") and (password == "PASSWORD1234"):
      check = True
    elif (attempts == 2):
      break

  if not(check) and (attempts > 0):
    print("NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO!")
  else:
    print("LOGIN EFETUADO COM SUCESSO.")

authentication()
