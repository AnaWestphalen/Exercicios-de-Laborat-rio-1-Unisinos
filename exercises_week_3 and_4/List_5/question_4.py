# Crie um método que recebe um valor por parâmetro (assuma que será uma string) e retorna a quantidade
# de letras ou outros caracteres que não sejam espaço que existem neste texto.

def countChars(letter):
  count = len(letter.replace(" ", ""))
  return count
