class Veiculos:
    def __init__(self, fabricante, modelo, ano, cor, quilometragem, qtde_passageiros):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem
        self.qtde_passageiros = qtde_passageiros

    def apresentar_veiculo(self):
        print(f'O {self.modelo} - {self.fabricante}')

#       acelerar
#       frear
#       

class Onibus(Veiculos):
    def __init__(self, fabricante, modelo, ano, cor, quilometragem, qtde_passageiros):
        super().__init__(fabricante, modelo, ano, cor, quilometragem, qtde_passageiros)

    def exibir_info(self):
        print('-*-'*10)
        print(f' Fabricante: {self.fabricante}\n'
              f' Modelo: {self.modelo}\n'
              f' Ano: {self.ano}\n'
              f' Cor: {self.cor}\n'
              f' Quilometragem: {self.quilometragem} Km')
        print('-*-'*10)

bus1 = Onibus('Volkswagen', 'Viaggio G7 900',
              2005, 'Azul', 35000, 40)
bus2 = Onibus('Volvo', '9700 Grand S',
              2012, 'Amarelo', 15000, 45)
lista_bus = [bus1, bus2]
for bus in lista_bus:
    bus.exibir_info()
