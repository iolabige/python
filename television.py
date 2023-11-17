class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 100
    MIN_CHANNEL = 1
    MAX_CHANNEL = 50

    def __init__(self):
        self.__status = False  # False for off, True for on
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:
            self.__channel = Television.MIN_CHANNEL if self.__channel == Television.MAX_CHANNEL else self.__channel + 1

    def channel_down(self):
        if self.__status:
            self.__channel = Television.MAX_CHANNEL if self.__channel == Television.MIN_CHANNEL else self.__channel - 1

    def volume_up(self):
        if self.__status:
            self.__muted = False
            self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)

    def volume_down(self):
        if self.__status:
            self.__muted = False
            self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)

    def __str__(self):
        power_status = "On" if self.__status else "Off"
        mute_status = "Muted" if self.__muted else "Unmuted"
        return f"Power = {power_status}, Channel = {self.__channel}, Volume = {self.__volume}, Mute Status = {mute_status}"
