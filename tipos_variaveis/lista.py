"""Lista é uma coleção de elementos, ordenaveis e mutaveis"""

# Declaração

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo por completo a lista
print ("Minha lista de exemplo", minha_lista)

# Exibindo os elementos:
minha_lista[0] = "troca"
print ("Minha lista de exemplo", minha_lista)
# Adicionando um elemento no final da lista
print ("minha_lista[0]", minha_lista[0])
print ("minha_lista (5)", minha_lista[5])
print ("minha_lista[1:7]", minha_lista[1:7])
print ("minha_lista[:6]", minha_lista[:6])
print ("minha_lista[2:]", minha_lista[2:])

# Métodos de lista

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append("exemplo")
print("item adicionado com o append()", minha_lista)

# Método index : retorna o indice do elemento que eu quero

indice = minha_lista.index(False)
print("indice do elemento False:", indice)

# Método insert(): Insere um elemento em um lugar específico da lista
minha_lista.insert(2, 10)
print ("Após o Insert(2, 10):", minha_lista)

# Métodos para deleção: Pop e remove
# Método pop(): Retira um elemento pelo seu índice
elemento_removido = minha_lista.pop(3)
print ("elemento_removido:", elemento_removido)
print ("Depois do pop(3):", minha_lista)

# Método clear(): Apaga todos os elementos da lista
# Método remove : retira o primeiro elemento com valor especificado
minha_lista.remove(True)
print ("Depois do remove(True):", minha_lista)

# Método sort
# O método sort() organiza os valores numérica ou alfabética
minha_lista.sort()
print ("Lista organizada por ordem alfabetica: ", minha_lista)
