import urllib.request, json

cep = input("Informe um CEP:") #Só aceitar Números

with urllib.request.urlopen(f"https://viacep.com.br/ws/{cep}/json/") as url:
    dados = json.loads(url.read().decode())

print('Estado: ' + dados['uf'])

if (dados['bairro'] != ""):
    print('Bairro: ' + dados['bairro'])

print('Cidade: ' + dados['localidade'])

if (dados['logradouro'] != ""):
    print('Rua: ' + dados['logradouro'])

print('DDD: ' + dados['ddd'])

#Nem Sempre o CEP é de uma rua e bairro específico.
