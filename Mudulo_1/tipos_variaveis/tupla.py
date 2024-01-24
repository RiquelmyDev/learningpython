# A tupla é uma coleção ordenada e imutavel de elementos
# Tuplas são representadas por parênteses () ou chaves {}
# As tuplas podem conter elementos de diferentes tipos, como:

minha_tupla = (1, 2, 2, 3, 4)

print ("Minha Tupla:", minha_tupla)

print ("Minha Tupla[0]:", minha_tupla [0])
print ("Minha Tupla[2]:", minha_tupla [2])
print ("Minha Tupla[-1]:", minha_tupla [-2])




# Mostrando os valores da tupla
for valor in minha_tupla:
  print(valor)

  # Verificar se um elemento está na tupla

# Metodos count: retorna a quantidade de vezes que o elemento aparece
contagem = minha_tupla.count(2)
print ("Quantidade de vezes que o elemento 2 aparece:", contagem)  

# Metodo index: Retorna a posição do elemento no qual ele foi encontr
posicao = minha_tupla.index(3)
print("A posição do elemento 3 é: ", posicao)