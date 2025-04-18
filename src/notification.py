from threading import Timer
import sys

from win11toast import toast

from settings import ALARM_SOUND_PATH
from .functions import limpar_terminal
from .alarm import PlayAlarm


class Notification(PlayAlarm):

    def __init__(self, title='', message='', duration=15):
        PlayAlarm.__init__(self, ALARM_SOUND_PATH)

        self.title = title
        self._message = message
        self.duration = duration

    def show(self):
        try:
            self.play_ringtone()

            buttons=['Iniciar Agora.', 'Encerrar']
            # Mostrar a notificação do Windows 11
            button_clicked = toast(
                self.title,
                self.message,
                duration='long',
                buttons=buttons,
            )
            limpar_terminal()

            if buttons[0] in button_clicked['arguments']:
                self.onclick_method()
            elif buttons[1] in button_clicked['arguments']:
                self.stop_ringtone()
                sys.exit(0)

            # Configurar o temporizador para parar o toque após a duração
            Timer(self.duration, self.after_notification).start()
        except Exception as e:
            print(f'erro: {e}')

    def onclick_method(self):
        self.stop_ringtone()
        return

    def after_notification(self):
        self.stop_ringtone()
        return

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
