import winsound

class PlayAlarm:
    def __init__(self, path):
        self.path = path

    def play_ringtone(self):
        winsound.PlaySound(self.path, winsound.SND_FILENAME | winsound.SND_ASYNC)

    def stop_ringtone(self):
        winsound.PlaySound(None, winsound.SND_PURGE)
