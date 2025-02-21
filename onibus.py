import datetime

class Veiculos:
    def __init__(self, fabricante, modelo, ano, cor, qtde_passageiros, revisoes_feitas):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.qtde_passageiros = qtde_passageiros
        self.revisoes_feitas = revisoes_feitas
    def exibir_info(self):
        print('-*-'*10)
        print(f' Fabricante: {self.fabricante}\n'
              f' Modelo: {self.modelo}\n'
              f' Ano: {self.ano}\n'
              f' Cor: {self.cor}\n'
              f' Qtde Passageiros: {self.qtde_passageiros}\n')
        print('-*-'*10)


class Onibus(Veiculos):
    def __init__(self, fabricante, modelo, ano, cor, qtde_passageiros, quilometragem, revisoes_feitas):
        super().__init__(fabricante, modelo, ano, cor, qtde_passageiros, revisoes_feitas)
        self.quilometragem = quilometragem
    # polimorfismo, função sobrescrita
    def exibir_info(self):
        print('-*-' * 10)
        print(f' Fabricante: {self.fabricante}\n'
              f' Modelo: {self.modelo}\n'
              f' Ano: {self.ano}\n'
              f' Cor: {self.cor}\n'
              f' Qtde Passageiros: {self.qtde_passageiros}\n'
              f' Quilometragem: {self.quilometragem} Km')
        print('-*-' * 10)

    def verifica_revisao(self):
        print('-*-' * 10)
        # idade = 2024 - self.ano
        km = self.quilometragem
        c = 0
        if int(km / 1000) == self.revisoes_feitas:
            print('-*-' * 10)
            while km % 1000 != 0:
                km += 1
                c += 1
            if c == 0:
                print('O ônibus não foi utilizado após a revisão')
            else:
                print(f'ainda faltam {c}km para a revisao')
        else:
            print('-*-' * 10)
            if self.revisoes_feitas == 0:
                self.revisoes_feitas = 1
            tempo_atraso = km - self.revisoes_feitas * 1000
            if tempo_atraso < 0:
                print(f'revisao adiantada em {tempo_atraso * -1}kms')
            else:
                if tempo_atraso == 0:
                    print('revisao recem vencida, renove imediatamente')
                else:
                    print(f'revisao atrasada em {tempo_atraso}kms')



class Aviao(Veiculos):
    def __init__(self, fabricante, modelo, ano, cor, qtde_passageiros, horas_voo, revisoes_feitas):
        super().__init__(fabricante, modelo, ano, cor, qtde_passageiros, revisoes_feitas)
        self.horas_voo = horas_voo

    # polimorfismo, função sobrescrita
    def exibir_info(self):
        print('-*-' * 10)
        print(f' Fabricante: {self.fabricante}\n'
              f' Modelo: {self.modelo}\n'
              f' Ano: {self.ano}\n'
              f' Cor: {self.cor}\n'
              f' Qtde Passageiros: {self.qtde_passageiros}\n'
              f' Horas de voo: {self.horas_voo}')
        print('-*-' * 10)

    def verifica_revisao(self):
        print('-*-' * 10)
        hr = self.horas_voo
        c=0
        if int(hr / 100) == self.revisoes_feitas:
            while hr % 100 != 0:
                hr += 1
                c += 1
            print('revisão em dia')
            if c == 0:
                print('Não foi utilizado após a revisão')
            else:
                print(f'ainda faltam {c}hrs\n')
        else:
            print('-*-' * 10)
            if self.revisoes_feitas == 0:
                self.revisoes_feitas = 1
            tempo_atraso = hr - self.revisoes_feitas * 100
            if tempo_atraso < 0:
                print(f'revisao adiantada em {tempo_atraso * -1}hrs')
            else:
                if tempo_atraso == 0:
                    print('revisao necessária imediatamente, recem vencida')
                else:
                    print(f'revisao atrasada em {tempo_atraso}hrs')




bus1 = Onibus('Volkswagen','Viaggio G7 900',
              2005, 'Azul', 35000, 3200, 3)
# bus2 = Onibus('Volvo', '9700 Grand S',
#               2012, 'Amarelo', 15000, 45, 0)
av1 = Aviao('Embraer','aviao1', 2008, 'azul', 120, 250, 2)
av2 = Aviao('Boing','aviao2', 2024, 'azul', 120, 100, 0)
# lista_bus = [bus1, bus2]
# for bus in lista_bus:
#     bus.exibir_info()
# av1.verifica_revisao()
av2.verifica_revisao()
# bus1.verifica_revisao()