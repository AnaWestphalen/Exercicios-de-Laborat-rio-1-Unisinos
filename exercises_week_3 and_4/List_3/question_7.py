# O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um
# programa que solicita ao usuário que ele digite seu usuário e senha. O programa só termina
# quando ele acertar o usuário e a senha. Quando ele acertar, você deve informar a mensagem: LOGIN EFETUADO COM SUCESSO.

def authentication():
  count = 0

  while True:
    user = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")

    if (user == "USER10") and (password == "PASSWORD1234"):
      break
    else:
      print("Não foi possível efetuar o login. Tente novamente!")
    count += 1

  print("LOGIN EFETUADO COM SUCESSO.")

authentication()
