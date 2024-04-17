# Execções são eventos que ocorrem durante a execução do código,
# e podem interromper o programa se não tratadas adequadamente

''' while True:
print("Exemplo de captura de excções: ")
  try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    print(f"Resultado {resultado}")
  except Exception as e:
    print(f"Erro: {e}") '''


# Outras formas de pegar as execções
print("Segundo exemplo de captura de excções: ")

try:
  numero = int(input("Digite um número inteiro: "))
  resultado = 10 / numero
  
except ValueError as e:
  print(f"Erro de value error: {e}")
  raise ValueError("Tipo de variavel incompatível")
except Exception as e:
  print(f"Erro: {e}")
else:
  print(f"Resultado {resultado}")
finally:
  print("Operação finalizada")