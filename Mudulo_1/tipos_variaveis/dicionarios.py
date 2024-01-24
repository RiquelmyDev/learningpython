# dicionario em python é uma coleção não ordenada de ( {pares, Chaves, valor} )

# Criando um dicionário

pessoa = {"nome": "Messi", "idade": 36, "pais": "Argentina"}


print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave

print ("Nome:", pessoa ["nome"])
print ("Idade:", pessoa ["idade"])
print ("Pais:", pessoa ["pais"])

"""para adicionar uma nova instancia depois que a variavel foi criada
você da o seguinde comando"""
pessoa["time"] = "Inter Miami"
print("Time atual:" , pessoa ["time"])

