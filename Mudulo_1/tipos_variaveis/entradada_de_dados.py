# entrada de dados

idade = int(input ("Qual sua idade?"))

if idade >= 18:
  print("Você é maior de idade!")
elif idade >= 15:
  print("Você é um adolecente!")
else:
  print("Você é menor de idade.")

mensagem = "Cara, voce ja tem 18 anos, entao voce pode tirar a porra da sua carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação!"
print (mensagem)



time = input("Teste seu conhecimento no futebol, respondendo umas perguntas. Pronto?")


campeao = input ("Qual maior campeao da Champions")
if campeao == "Real Madrid":
  print ("isso ai, voce esta certo!")

else:
  print("Você errou, tente denovo!")

campeao = input ("Qual maior campeao da Champions")
if campeao == "Real Madrid":
  print ("isso ai, voce esta certo!")

