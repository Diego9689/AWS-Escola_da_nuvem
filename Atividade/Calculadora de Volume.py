"""
3- Calculadora de Volume
* Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:

* Comprimento: 12 cm
* Largura: 14 cm
* Altura: 20 cm
O programa deve calcular o volume e exibir o resultado em cm³.
"""
def area(a:int,b:int):
    return a*b
def volume(c:int,d:int,e:int):
    return area(c,d)*e
def printar(num:int,num1:int,num2:int):
    print(volume(num,num1,num2))
Comprimento= 12 
Largura= 14 
Altura= 20 
printar(Comprimento,Largura,Altura)