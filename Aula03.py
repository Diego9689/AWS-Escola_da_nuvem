#CRIANDO UMA API DE CEP

import requests


def Consultar_Cep(cep:str) -> str:
    cep = cep.replace("-","").strip()
    
    if len(cep) !=8 or not cep.isdigit():
        print("CEP inválido. Digite um CEP com 8 números")
        return
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code!=200:
        print("Erro ao acessar a API via CEP")
        return
    
    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado")
        return
    
    print("\nEdenreço encontrado :")
    print(f"Logradouro : {dados.get('logradouro')}")
    print(f"Bairro : {dados.get('bairro')}")
    print(f"Cidade : {dados.get('localidade')}")
    print(f"Estado : {dados.get('uf')}")
    return "certo"

cep_usuario = input("Digite o CEP : ")
while Consultar_Cep(cep_usuario)==None:
    cep_usuario = input("Digite o CEP : ")
    Consultar_Cep(cep_usuario)

