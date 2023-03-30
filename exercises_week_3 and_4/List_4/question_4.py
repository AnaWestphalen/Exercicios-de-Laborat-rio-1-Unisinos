# Sabendo que uma string é uma lista de letras, peça para o usuário digitar um texto e imprima
# na tela a quantidade de vogais que existem no texto.

def countVowels():
  text = input("Digite seu texto aqui: ")
  treatedText = text.replace(" ", "").lower()
  vowel = 'aeiou'
  list = []

  for i in treatedText:
    if (i in vowel):
      list.append(i)

  count = len(list)

  print("O número de vogais no seu texto foi:", count)

countVowels()
