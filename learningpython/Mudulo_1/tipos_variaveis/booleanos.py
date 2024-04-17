"""Booleanos são tipos de variaveis que apenas
 comportam 2 tipos de variaveis, são elas as condições:"""

# Condição verdadeira
True

# Condição falsa
False

# Condicionais são blocos de codigos que serão executados caso
# a condição seja verdadeira ou falsa.

if True:
  print ("Bloco IF vai ser executado")
else:
  print("Bloco ELSE não será executado")

  # Operadores lógicos: and e or
  # O and ajuda a comparar duas entradas e dar uma saída

if True and True:
  print("A entrada é verdadeira")

if True and False:
  print ("Bloco não será executado")

if False and False:
  print ("Bloco não será executado")

# Operadores logícos vão comparar

# or só retorna uma condição verdadeira
# se caso uma das condições for verdadeiro

if True or False:
  print("Bloco OR vai ser executado")

if False or False:
  print("Bloco OR não vai ser executado")      

if True or True:
  print("Bloco OR vai ser executado")
