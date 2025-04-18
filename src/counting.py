import functools
import time

def contagem_regressiva_inicial(atributo):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            intervalo_atual = getattr(self, atributo)
            if intervalo_atual == 1:
                tempo_contagem_regressiva = 5
                for i in reversed(range(1, tempo_contagem_regressiva + 1)):
                    plural = True if i == 1 else False
                    print(f'\rIniciando Pomodoro🍅 em {i} {'segundo' if plural else 'segundos'}. ', end='', flush=True)
                    time.sleep(1)
                print('\r' + ' ' * 50, end='\r')
            return func(self, *args, **kwargs)
        return wrapper
    return decorator