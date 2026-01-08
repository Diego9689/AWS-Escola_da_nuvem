"""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado 
final.
"""

def calcula(Preço_unitário:float,quantidade:int):
    return Preço_unitário*quantidade

def retornarJson(nome:str,total:int):
    return f"Nome: {nome} \nTotal: {total}"

def main(Nome_do_produto:str,Preço_unitário:float,Quantidade:int):
    return retornarJson(Nome_do_produto,calcula(Preço_unitário,Quantidade))

def mostrar(Nome_do_produto:str,Preço_unitário:float,Quantidade:int):
    print(main(Nome_do_produto,Preço_unitário,Quantidade))


Nome_do_produto= "Cadeira Infantil"
Preço_unitário= 12.40
Quantidade= 3
mostrar(Nome_do_produto,Preço_unitário,Quantidade)