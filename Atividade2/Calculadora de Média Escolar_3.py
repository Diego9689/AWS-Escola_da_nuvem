'''
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando
para duas casas decimais.

'''

def media(lista_de_notas:list) ->float:
    cont=0
    soma=0
    for nota in lista_de_notas:
        cont+=1
        soma+= nota
    return soma/cont

def lista_notas(*notas: float) -> list:
    return list(notas)

def main(*notas: float):
    notas_lista = lista_notas(*notas)
    resultado = media(notas_lista)
    print(f"{resultado:.2f}")



Nota_1 = 7.5
Nota_2 = 8.0
Nota_3 = 6.5
main(Nota_1,Nota_2,Nota_3)