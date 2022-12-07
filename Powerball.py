import random
from colorama import Fore

from Whiteball import Whiteball_n
from Userball import Userball_n


class Powerball_n(Whiteball_n, Userball_n):
    def powerball_number(self):
        pb_number1 = random.randint(1, 10)
        self.whiteball_numbers.append(pb_number1)
        print("\t\t\t\t-Today's Powerball Winning Numbers ")
        print("\t\t\t\t ", Fore.BLUE, self.whiteball_numbers, Fore.RESET)
        pb_number2 = random.randint(1, 10)
        self.user_numbers.append(pb_number2)
        print("\n\t\t\t\t- Your Lucky Numbers ")
        print("\t\t\t\t ", Fore.BLUE, self.user_numbers, Fore.RESET)


