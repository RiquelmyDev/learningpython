# dicionario em python é uma coleção não ordenada de ( {pares, Chaves, valor} )

# Criando um dicionário

pessoa = {"nome": "Messi", "idade": 36, "pais": "Argentina", }


print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave

print ("Nome:", pessoa ["nome"])
print ("Idade:", pessoa ["idade"])
print ("Pais:", pessoa ["pais"])

"""para adicionar uma nova instancia depois que a variavel foi criada
você da o seguinde comando"""
pessoa["time"] = "Inter Miami"
print("Time atual:" , pessoa ["time"])

#como alterar ou atualizar um valor ja existente

pessoa["idade"] = 31
print ("Idade atualizada:", pessoa ["idade"])

# para remover um elemento do dicionário (chave valor) você usa o comando del

del pessoa["nome"]
print(pessoa)

# metodos: keys (), values (), items ()

"""no metodo keys, para acessar uma chave direto,
você tem que a transformar em uma lista"""


chaves = list (pessoa.keys())

print ("Chaves do dicionário:", chaves)
print ("Primeira chave:", chaves [0])

# método values // também usa o list
valores = pessoa.values()
print ("Valores do dicionário:", valores)

# metodo items

itens = list (pessoa.items()) # retorna uma tupla com a chave
# e seu respectivo valor
print ("Itens do dicionario:", itens)

print ("Meu primeiro item:", itens[0][1])

print ("Primeira chave-valor:  %s = %s" % (itens[0][0], itens[0][1]))


#### ACHEI MUITO COMPLICADO!!!
