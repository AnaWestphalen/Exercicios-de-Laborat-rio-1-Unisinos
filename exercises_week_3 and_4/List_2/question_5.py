# Crie um programa que solicita o time de 10 usuários pelo teclado. Ao final,
# imprima quantos torcedores torcem para o Grêmio.

def listTeams():
  count = 0
  teamGremio = 0

  while (count < 10):
    team = input("Digite o nome do seu time do coração: ")
    if (team.lower() == "grêmio") or (team.lower() == "gremio"):
      teamGremio += 1
    count += 1

  print("O número de torcedores do Grêmio é:",teamGremio)

listTeams()
