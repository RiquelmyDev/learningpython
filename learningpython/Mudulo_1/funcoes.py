#As funções em Python servem para organizar o código em blocos reutilizáveis e modulares.
#Elas ajudam a tornar o código mais legível, mais fácil de dar manutenção e mais eficiente.

def saudacao(nome):
  print (f"Olá, {nome}!")

print("\n Chamando função saudacao:")
saudacao("Alice")
saudacao("Bob")  

# Funções que retornam informações:

def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("\n Chamando função quadrado:")
resultado_quadrado = quadrado(5)
print ("Resultado da função quadrado:", resultado_quadrado)

# função com multiplos parametros

def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

print ( "\n Chamando função soma:")
soma_de_dois_numeros = soma(3,4)
print ("Soma de dois numeros: ", soma_de_dois_numeros)

# melhorando o codigo

def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

print ( "\n Chamando função soma:")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1,numero2)
print ("A soma do número %s e o número %s é = %s" % (numero1, numero2, resultado_soma))