from .counting import contagem_regressiva_inicial
from .functions import limpar_terminal
from .convert import Conversoes

from .notification import Notification


class Pomodoro:
    def __init__(self, **kwargs):
        self.trabalho = kwargs.get('trabalho')
        self.intervalo = kwargs.get('intervalo')
        self.descanso = kwargs.get('descanso')

        self.__quantidade_pomodoros = kwargs.get('quantidade_pomodoros')

        self.__ciclo_completo_pomodoro_atual = 1
        self.__pomodoro_atual = 1
        self.__intervalo_atual = 1

    # Pomodoro
    @contagem_regressiva_inicial('pomodoro_atual')
    def init_pomodoro(self):

        print(self.retorna_ciclo_completo_info())

        print(f'\n🍅 {self.pomodoro_atual}/{self.quantidade_pomodoros} Pomodoro Iniciado: ')
        Conversoes.loop_timer(self.trabalho, prefix='Tempo Restante: ', suffix='')
        self.pomodoro_atual = 1

    # Intervalo
    def init_intervalo(self):
        print(self.retorna_ciclo_completo_info())

        print(f'\n⏳ {self.intervalo_atual}/{self.quantidade_pomodoros - 1} Intervalo Iniciado: ')
        Conversoes.loop_timer(self.intervalo, prefix='Tempo Restante: ', suffix='')
        self.intervalo_atual = 1

    # Descanso
    def init_descanso(self):
        print(self.retorna_ciclo_completo_info())

        print('\n😴 Descanso Iniciado: ')
        Conversoes.loop_timer(self.descanso, prefix='Tempo Restante: ', suffix='')
        print('\n')
        self.pomodoro_atual = 1

    # Retorna Ciclo Completo de Pomodoro Atual
    def retorna_ciclo_completo_info(self):
        return f'{self.ciclo_completo_pomodoro_atual}º Ciclo Completo de Pomodoro'

    # Pomodo Atual
    @property
    def pomodoro_atual(self):
        return self.__pomodoro_atual

    @pomodoro_atual.setter
    def pomodoro_atual(self, incremento):
        if incremento > 0:
            self.__pomodoro_atual += incremento
        else:
            raise ValueError("O valor deve ser maior que zero.")

    @pomodoro_atual.setter
    def resetar_pomodoro_atual(self, valor):
        if valor > 0:
            self.__pomodoro_atual = valor
        else:
            raise ValueError("O valor deve ser maior que zero.")

    # Intevalo Atual
    @property
    def intervalo_atual(self):
        return self.__intervalo_atual

    @intervalo_atual.setter
    def intervalo_atual(self, incremento):
        if incremento > 0:
            self.__intervalo_atual += incremento
        else:
            raise ValueError("O valor deve ser maior que zero.")

    @intervalo_atual.setter
    def resetar_intervalo_atual(self, valor):
        if valor > 0:
            self.__intervalo_atual = valor
        else:
            raise ValueError("O valor deve ser maior que zero.")

    # Quantidade de pomodoros
    @property
    def quantidade_pomodoros(self):
        return self.__quantidade_pomodoros

    # Ciclo Completo de Pomodo
    @property
    def ciclo_completo_pomodoro_atual(self):
        return self.__ciclo_completo_pomodoro_atual

    @ciclo_completo_pomodoro_atual.setter
    def incrementar_ciclo_completo_atual(self, valor):
        if valor >= 0:
            self.__ciclo_completo_pomodoro_atual += valor
        else:
            raise ValueError("O valor deve ser maior ou igual a zero.")


class GerenciaPomodoro(Pomodoro):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        notificacao = Notification(title='🍅 Pomodoro 🍅')

        while True:
            while self.pomodoro_atual <= self.quantidade_pomodoros:
                if self.intervalo_atual > 1:
                    notificacao.message = 'Iniciando Pomodoro em 25s.'
                    notificacao.show()
                self.init_pomodoro()
                limpar_terminal()
                if self.intervalo_atual < self.quantidade_pomodoros:

                    notificacao.message = 'Iniciando Intervalo em 25s.'
                    notificacao.show()
                    self.init_intervalo()
                    limpar_terminal()

            notificacao.message = 'Iniciando Descanso em 25s.'
            notificacao.show()
            self.init_descanso()
            limpar_terminal()

            self.incrementar_ciclo_completo_atual = 1
            self.resetar_intervalo_atual = 1
            self.resetar_pomodoro_atual = 1
