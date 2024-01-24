# Declaração
nome_completo = "Riquelmy Soares Vasconcelos"

nome_completo_aspas = """Riquelmy
Soares
Vasconcelos"""

nome_completo_quebra = "Gabriel \
Casemiro"

nome = "Riquelmy"
sobrenome = "Vasconcelos"

nome_completo = nome + " " + sobrenome
print (nome_completo)

# Formatação
print ("Nome completo (1a forma):", nome_completo)
print ("Nome completo (2a forma):" + nome_completo)
print ("Nome completo (3a forma):" + "Riquelmy" + "Vasconcelos")
print ("Nome completo (3a forma):" + "Riquelmy", "Vasconcelos")
print ("Nome completo (5a forma):", nome_completo_aspas )
print ("Nome completo (6a forma):", nome_completo_quebra )
print ("Nome completo (7a forma): %s" % nome_completo)

# ATENÇÃO ! quando usar mais de uma variavel em uma string, é nescessario usar parenteses para isolalas! Esse modo é mais seguro
print ("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print (f"Nome completo (9a forma): {nome} {sobrenome}")
print ("Nome completo (10a forma):{} {}".format(nome, sobrenome))



""" Principais métodos de textos:
Para deixar o conteudo de uma variavel todo em maiusculo e minusculo
use as tags upper() e lower() respectivamente

Outras funções são -->>

"count(x)" conta quantas letras da que 
voce deu como alvo existe na string 

" Find " que diz em que posição respectiva letra esta na sua string

" Replace ", que troca alguma coisa por outra coisa na string.

"Encode()" que que coloca seu codigo para ser um byte
"decode()" que transforma de byte para texto

"Replace("")," " " subistitui o alvo que voce deu por uma nova letra

" " "join(variavel)" separa todas as letras da variavel de acordo com o tiipo de espaçamento que você declarar no parenteses

O strip é usado pra tirar os espacos do começo e do fim de
uma linha ou de uma string

"split" " " separa sua string em listas, colocando cada palavras
em um bloco diferente!

startswith e endswith dizem se sua string começa ou termina com determinados caracteres que voce declarou

" " in variavel ) diz se tem esse conjunto de caracteres na sua string
( "" not in variavel ) diz se não tem!






""" 

