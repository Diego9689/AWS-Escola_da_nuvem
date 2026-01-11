'''
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

'''
class CalculePreco:

    def __init__(self, nome_do_produto: str, preço_original: float, Porcentagem_de_desconto : float):
        self.Nome_do_produto = nome_do_produto
        self.Preço_original = preço_original
        self.Porcentagem_de_desconto = Porcentagem_de_desconto

    def Desconto(self) -> float:
        return self.Preço_original*self.Porcentagem_de_desconto 

    def PrecoOriginal(self) -> float:
       return self.Preço_original - self.Desconto()

    def retornar_json(self) -> dict:
        return {
            "produto": self.Nome_do_produto,
            "preco_original": self.Preço_original,
            "desconto": self.Desconto(),
            "porcentagem_desconto": self.Porcentagem_de_desconto,
            "preco_final": self.PrecoOriginal()
        }

def main():
    produto = CalculePreco(
        nome_do_produto="Camiseta",
        preço_original=50.00,
        Porcentagem_de_desconto=0.20
    )

    print(produto.retornar_json())


if __name__ == "__main__":
    main()
