# modulos de terceiros são pacotes criados por outras pessoas
# instalando a biblioteca resquest

print("\n Importação e uso de um módulo de terceiros")
import requests 

url = "https://www.example.com"
response = requests.get(url)

print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")

''' Sites para documentação
https://docs.python.org/3/library/index.html
https://www.w3schools.com/python/python_datetime.asp
Documentação de terceiros: https://pypi.org '''