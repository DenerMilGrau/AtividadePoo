class Veiculos:
    def __init__(self, fabricante, modelo, ano, cor, qtde_passageiros, revisoes_feitas, imposto):
        self._fabricante = fabricante
        self._modelo = modelo
        self._ano = ano
        self._cor = cor
        self._qtde_passageiros = qtde_passageiros
        self._revisoes_feitas = revisoes_feitas
        self._imposto = imposto
    # protegido pode ser acessado chamando de maneira mais complicada
    # privado pode ser acessado nas subclasses somente com o get
    #
    def get_fabricante(self):
        return self._fabricante
    def get_modelo(self):
        return self._modelo
    def get_ano(self):
        return self._ano
    def get_cor(self):
        return self._cor
    def get_qtde_passageiros(self):
        return self._qtde_passageiros
    def get_revisoes_feitas(self):
        return self._revisoes_feitas
    def is_imposto_pago(self):
        return self._imposto

    def add_revisao(self):
        self._revisoes_feitas += 1
        print(self.get_revisoes_feitas())

    def set_imposto(self, status):
        if self.is_imposto_pago() and status:
            print('imposto ja pago')
        elif self.is_imposto_pago() and not status:
            print('imposto estava pago, agora venceu')
            self._imposto = status
        elif not self.is_imposto_pago() and status:
            print('imposto n estava pago, agora esta')
            self._imposto = status
        elif not self.is_imposto_pago() and not status:
            print('imposto ja n estava pago, e continua devendo')
        else:
            print('provavelmente voce inseriu uma parametro errado\n'
                  'fdp burro')
    def exibir_info(self):
        print('-*-'*10)
        print(f' Fabricante: {self.get_fabricante()}\n'
              f' Modelo: {self.get_modelo()}\n'
              f' Ano: {self.get_ano()}\n'
              f' Cor: {self.get_cor()}\n'
              f' Qtde Passageiros: {self.get_qtde_passageiros()}\n'
              f'Imposto: {'Pago' if self.is_imposto_pago() else 'Atrasado'}\n'
              )
        print('-*-'*10)

    # def imposto_em_dia(self):
    #     if self.is_imposto_pago():
    #         print('-*-'*10)
    #         print('Imposto em dia...')
    #     else:
    #         print('-*-'*10)
    #         print('Imposto atrasado...')

class Onibus(Veiculos):
    def __init__(self, fabricante, modelo, ano, cor, qtde_passageiros, quilometragem, revisoes_feitas, imposto):
        super().__init__(fabricante, modelo, ano, cor, qtde_passageiros, revisoes_feitas, imposto)
        self.__quilometragem = quilometragem

    def get_quilometragem(self):
        return self.__quilometragem

    # polimorfismo, função sobrescrita
    def exibir_info(self):
        print('-*-' * 10)
        print(f' Fabricante: {self.get_fabricante()}\n'
              f' Modelo: {self.get_modelo()}\n'
              f' Ano: {self.get_ano()}\n'
              f' Cor: {self.get_cor()}\n'
              f' Qtde Passageiros: {self.get_qtde_passageiros()}\n'
              f' Quilometragem: {self.get_quilometragem()} Km')
        print('-*-' * 10)

    def verifica_revisao(self):
        print('-*-' * 10)
        # idade = 2024 - self.ano
        km = self.get_quilometragem()
        c = 0
        if int(km / 1000) == self.get_revisoes_feitas():
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
            if self.get_revisoes_feitas() == 0:
                self.add_revisao()
            tempo_atraso = km - self.get_revisoes_feitas() * 1000
            if tempo_atraso < 0:
                print(f'revisao adiantada em {tempo_atraso * -1}kms')
            else:
                if tempo_atraso == 0:
                    print('revisao recem vencida, renove imediatamente')
                else:
                    print(f'revisao atrasada em {tempo_atraso}kms')

    def exibir_km(self):
        print('-*-' * 10)
        print(f' Quilometragem: {self.get_quilometragem()}\n')

class Aviao(Veiculos):
    def __init__(self, fabricante, modelo, ano, cor, qtde_passageiros, horas_voo, revisoes_feitas, imposto):
        super().__init__(fabricante, modelo, ano, cor, qtde_passageiros, revisoes_feitas, imposto)
        self.__horas_voo = horas_voo

    def get_horas_voo(self):
        return self.__horas_voo

    # polimorfismo, função sobrescrita
    def exibir_info(self):
        print('-*-' * 10)
        print(f' Fabricante: {self.get_fabricante()}\n'
              f' Modelo: {self.get_modelo()}\n'
              f' Ano: {self.get_ano()}\n'
              f' Cor: {self.get_cor()}\n'
              f' Qtde Passageiros: {self.get_qtde_passageiros()}\n'
              f' Horas de voo: {self.get_horas_voo()}\n')
        print('-*-' * 10)

    def verifica_revisao(self):
        print('-*-' * 10)
        hr = self.get_horas_voo()
        c=0
        if int(hr / 100) == self.get_revisoes_feitas():
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
            if self.get_revisoes_feitas() == 0:
                self.add_revisao()
            tempo_atraso = hr - self.get_revisoes_feitas() * 100
            print(tempo_atraso)
            if tempo_atraso < 0:
                print(f'revisao adiantada em {tempo_atraso * -1}hrs')
            else:
                if tempo_atraso == 0:
                    print('revisao necessária imediatamente, recem vencida')
                else:
                    print(f'revisao atrasada em {tempo_atraso}hrs')

    def exibir_horas(self):
        print('-*-' * 10)
        print(f' Horas de voo: {self.get_horas_voo()}\n')

bus1 = Onibus('Volkswagen','Viaggio G7 900',
              2005, 'Azul', 35000, 1000, 1, True)
# bus2 = Onibus('Volvo', '9700 Grand S',
#               2012, 'Amarelo', 15000, 45, 0)
av1 = Aviao('Embraer','aviao1', 2008, 'azul', 120, 250, 2, True)
av2 = Aviao('Boing','aviao2', 2024, 'azul', 120, 100, 1, True)