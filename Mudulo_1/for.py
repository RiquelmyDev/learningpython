#Loop é uma estrutura que permite a gente repetir um bloco de codigo em quanto uma condição for verdadeira
# Ele é utilizado para automatizar tarefas repetitivas, e executada ações repetidas vezes
# existe 2 tipos de loop : while (enquanto) e for (para cada item)

print("For utilizando Lista:")

lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

print("For utilizando tupla:")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

pessoa = {"nome": "Messi", "idade": 36, "cidade": "Miami"}
print("For Utilizando dicionario - chaves")
for chave in pessoa.keys():
  print(chave)

print("\nFor Utilizando dicionario - Valor")
for valor in pessoa.values():
  print(valor)

print("\nFor Utilizando dicionario - items")

for chave, valor in pessoa.items():
    print(f"{chave} tem o valor {valor}")

#truques para fazer o loop for mais rapido

# range(): retorna um intervalo numérico em formato de lista

range(0,11) #para converter para lista só colocar list antes

print ("\n Utilizando a função range():")
for numero in range(6):
  print("Numero:", numero)


print ("\n Utilizando a função range() com len()")

lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
  if indice == 3:
    lista[indice] = 5
  else:
    lista[indice] = 0
    
print(lista)

#geralmente se usa isso para poder alterar um valor dentro dessa lista!


# Função enumerate() extrai as duas informaçoes, o valor e o indice

lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):

  print(f"{indice}:{valor}")
  if indice ==  1:
    print("indice 1")