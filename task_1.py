import time
import colorama
from colorama import Fore

colorama.init()


class TrafficLight:
    info_1 = 'Светофор включен'
    print(info_1)
    __color = 0

    def running(self):
        while True:
            print(Fore.RED + 'Красный')
            time.sleep(7)
            print(Fore.YELLOW + 'Желтый')
            time.sleep(2)
            print(Fore.GREEN + 'Зеленый')
            time.sleep(5)
            print(Fore.YELLOW + 'Желтый')
            time.sleep(2)


t = TrafficLight()
t.running()
