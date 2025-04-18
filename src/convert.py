import time

class Conversoes:

    @staticmethod
    def formatacao_horario(segundos_totais, prefix='', suffix=''):

        hours = int(segundos_totais // 3600)
        minutes = int((segundos_totais % 3600) // 60)
        seconds = int(segundos_totais % 60)
        return f"{prefix} {hours:02d}:{minutes:02d}:{seconds:02d} {suffix}"

    @staticmethod
    def loop_timer(*args, **kwargs):

        segundos = args[0] * 60
        for segundo in reversed(range(segundos)):
            tempo_restante = Conversoes.formatacao_horario(segundo, **kwargs)
            print(f'\r{tempo_restante}', end='', flush=True)
            time.sleep(1)
            