# Crie um método que recebe um inteiro por parâmetro e retorna verdadeiro caso seja um valor primo e
# falso caso contrário. Caso o parâmetro seja negativo o método deve retornar falso.

def isPrime(number):
  if (number < 0):
    return False

  if (number == 1) or (number == 2):
    return True
    
  for i in range(2, number):
    if number % i == 0:
      return False
  return True
