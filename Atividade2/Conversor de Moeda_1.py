'''
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas
decimais.


'''

def convertDolar(valor:float)->  float:
    return valor*5.20

def convertEuro(valor:float)->  float:
    return valor*6.15

def exibir(valor:float):
    print(f"O valor em Dolár é : {convertDolar(valor):.2f}")
    print(f"O valor em Euro é : {convertEuro(valor):.2f}")

Valor_em_reais =  100.00
Taxa_do_dólar =  5.20
Taxa_do_euro =  6.15

exibir(Valor_em_reais)
