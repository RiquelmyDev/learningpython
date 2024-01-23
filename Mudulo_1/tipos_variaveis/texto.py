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



