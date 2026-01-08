"""
3- Calculadora de Volume
* Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:

* Comprimento: 12 cm
* Largura: 14 cm
* Altura: 20 cm
O programa deve calcular o volume e exibir o resultado em cm³.
"""

def area(Comprimento:int,Largura:int):
    return Comprimento*Largura

def volume(Comprimento:int,Largura:int,Altura:int):
    return area(Comprimento,Largura)*Altura

def printar(Comprimento:int,Largura:int,Altura:int):
    print(volume(Comprimento,Largura,Altura))

Comprimento= 12 
Largura= 14 
Altura= 20 
printar(Comprimento,Largura,Altura)