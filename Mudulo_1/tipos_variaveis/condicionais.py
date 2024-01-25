"""Oque é uma condicional : Ela permite a gente tomar uma 
decisão com base em uma condição. E essas decisoes vão executar
um bloco de código que vai estar dentro dessa condicional"""

# nas condionais usamos: if, elif e else -- se usa para comparar

# if

idade = 17
if idade >= 18: 
  print("Você é maior de idade")
elif idade >= 15:
  print("Você é um adolecente")
else:
  print("Você é menor de idade")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação!"
print (mensagem)



""" if idade == 19:
  print ("Você tem 19 anos")

if idade < 18:
  print("Você é menor de idade")

if idade != 10:
  print ("Você não tem 10 anos!") """

# else
