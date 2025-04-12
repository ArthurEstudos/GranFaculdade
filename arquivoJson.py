import json

pessoas = [
    {'nome': 'Arthur', 'telefone': '(11)98550-5864', 'Endereco': 'SP'},
    {'nome': 'joao', 'telefone': '(11)98459-5764', 'Endereco': 'RJ'},
    {'nome': 'maria', 'telefone': '(11)98567-5964', 'Endereco': 'MG'},
] 

with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquiuvo, indent=4)

