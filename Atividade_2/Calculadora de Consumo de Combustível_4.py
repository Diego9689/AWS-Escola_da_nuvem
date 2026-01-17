'''
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os 
seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem,incluindo 
o resultado final arredondado para duas casas decimais

'''
class Calcular_Consumo():
    def __init__(self,distancia:float,combustivel:float):
        self.Distância_percorrida = distancia
        self.Combustível_gasto = combustivel
    
    def consumo_médio(self) -> float:
        return self.Distância_percorrida/self.Combustível_gasto
    
    def Retornar_Json(self) -> str:
        return f"Consumo médio : {self.consumo_médio():.2f} KM/L\nDistância_percorrida : {self.Distância_percorrida} KM\nCombustível_gasto : {self.Combustível_gasto} L"

    def Main(self):
        print(self.Retornar_Json())


def chamarClasse():
    consumo = Calcular_Consumo(distancia=300, combustivel=25)
    consumo.Main()

if __name__ == "__main__":
    chamarClasse()
 
