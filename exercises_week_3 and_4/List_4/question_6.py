# Crie um programa que solicita o nome e o estado civil de 20 pessoas pelo teclado.
# Ao final, imprima apenas o nome das pessoas separadas por estado civil:
# solteiras, casadas, divorciadas e viúvas (nesta ordem!)

def maritalStatus():
  allData = []

  for i in range(1, 21):
    print('Pessoa', i)
    name = input('Digite seu nome: ')
    status = input('Digite o seu estado civil: ')
    allData.append([name, status])

  single = []
  married = []
  divorced = []
  widower = []

  for data in allData:
    if (data[1].lower() == 'solteiro') or (data[1].lower() == 'solteira'):
      single.append(data[0])
    elif (data[1].lower() == 'casado') or (data[1].lower() == 'casada'):
      married.append(data[0])
    elif (data[1].lower() == 'divorciado') or (data[1].lower() == 'divorciada'):
      divorced.append(data[0])
    elif (data[1].lower() == 'viúvo') or (data[1].lower() == 'viúvo'):
      widower.append(data[0])

  print('Solteiros(as):',single)
  print('Casados(as):',married)
  print('Divorciados(as):',divorced)
  print('Viúvos(as):',widower)
