# Modulos são arquivos que tem definições e instruções que podem
# Ser utilizados por outros progamas

print ("exemplo de importação de módulo padrão:")
import  math  #Importa o módulo matemático da linguagem Python.

raiz_quadrada = math.sqrt(25)   #Acessando
print(f"A raiz quadrada de 25 é: {raiz_quadrada}")

# esse é o mais recomendado, importar só aquilo que você precisa
from math import  sqrt, pow   # Importa somente as funções sqrt (raiz quadrada) e pow (potência).


print("\n Exemplo de criação e personalização de um módulo personalizado")
import meu_modulo
from meu_modulo import saudacao, dobro

mensagem = meu_modulo.saudacao("Riquelmy")
resultado_dobro = meu_modulo.dobro(10)
print(mensagem)
print(f"O dobro de 10 é: {resultado_dobro}")


