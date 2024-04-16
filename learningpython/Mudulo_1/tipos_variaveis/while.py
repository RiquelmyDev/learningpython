# While é um tipo de looping pra repetir um bloco de código, em quanto uma condição for verdadeira

print ("Exemplo de while")
contador = 0
while contador < 5:
  print("Contagem:", contador)
  contador = contador + 1
  if contador == 4:
    break

print("Programa finalizado!")