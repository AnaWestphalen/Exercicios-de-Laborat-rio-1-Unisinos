# Crie um programa que solicita que o usuário digite uma letra e imprime
# na tela se a letra é uma vogal ou uma consoante.

def vowelOrConsonant():
  letter = input("Digite uma letra: ")
  vowel = 'aeiou'

  if (letter.lower() in vowel):
    print("Você digitou uma vogal!")
  else:
    print("Você digitou uma consoante")

vowelOrConsonant()
