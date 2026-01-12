#Programa para verificar a cotação do dolar em tempo real

import requests 

converter_para_real = lambda valor, cotacao : valor * cotacao

def obter_cotacao_dolar():
    try:
        url="https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url)
        dados = resposta.json()

        if "USDBRL" in dados:
            return float(dados["USDBRL"]["bid"])
        
        else:return

    except requests.exceptions.RequestException:
        print("Erro ao acessar a API da cotação")
        return 
    
def main():
    try:
        valor_dolar =  float(input("Digite o valor em Dólar (USD) : "))

        cotacao = obter_cotacao_dolar()

        if cotacao:
            valor_real = converter_para_real(valor_dolar, cotacao)
            print(f"\nUSD {valor_dolar:.2f}")
            print(f"\nCotação: R$ {cotacao:.2f}")
            print(f"\nValor em reais: R$ {valor_real:.2f}")
            print()
        else:
            print(f"\nNão foi possivel obter a cotação")
    except ValueError:
        print("\nDigite um número válido")
    except Exception as error:
        print("\nErro inesperado : ", error)

main()