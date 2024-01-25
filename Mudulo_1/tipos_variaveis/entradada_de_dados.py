# entrada de dados

idade = int(input ("Qual sua idade?"))

if idade >= 18:
  print("Você é maior de idade!")
elif idade >= 15:
  print("Você é um adolecente!")
else:
  print("Você é menor de idade.")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação!"
print (mensagem)
