# Crie um método que recebe 3 notas por parâmetro e retorna o conceito atingido pela média aritmética das notas.
# Os conceitos são:
# - entre 0.0 e 4.0 (inclusive): conceito "D"
# - entre 4.0 (não incluído) e 7.0 (inclusive): conceito "C"
# - entre 7.0 (não incluído) e 9.0 (inclusive): conceito "B"
# - entre 9.0 (não incluído) e 10.0 (inclusive): conceito "A"
# Caso alguma das notas digitadas seja negativa, retorne o texto "ERRO".

def schoolConcept(result1, result2, result3):
  arithmeticAverage = (result1 + result2 + result3) / 3

  if (result1 > 0) and (result2 > 0) and (result3 > 0):
    if (0.0 < arithmeticAverage < 4.0):
      return "Conceito D"
    elif (4.0 < arithmeticAverage < 7.0):
      return "Conceito C"
    elif (7.0 < arithmeticAverage < 9.0):
      return "Conceito B"
    else:
      return "Conceito A"
  else:
    return "ERRO"

