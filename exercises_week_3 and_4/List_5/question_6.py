# Crie um método que recebe uma lista por parâmetro (assuma que será uma lista de string) e retorna a menor
# string da lista (com menos caracteres).

def smallWord(list):
  smallString = list[0]

  for s in list:
    if len(s) < len(smallString):
        smallString = s
        
  return smallString
