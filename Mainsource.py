import random
from colorama import Fore
from Correctnumber import Correct_n


class Price(Correct_n):

    def Pricefunction(self):
        self.correct_number()

        pb_number1 = random.randint(1, 10)
        print("\t\t\t\t-Today's Powerball Winning Numbers ")
        print("\t\t\t\t ", Fore.BLUE, self.whiteball_numbers, Fore.RESET, Fore.RED, pb_number1, Fore.RESET)
        pb_number2 = random.randint(1, 10)
        print("\n\t\t\t\t- Your Lucky Numbers ")
        print("\t\t\t\t ", Fore.BLUE, self.user_numbers, Fore.RESET, Fore.RED, pb_number2, Fore.RESET)
        print("\n\t\t\t\t- The same amount of numbers are ", self.correct_num)

        if self.correct_num == 5 and pb_number1 == pb_number2:
            print(Fore.GREEN, "\n\t\t\t\t- 5 Correct White Balls and The Powerball: $324,000,000", Fore.RESET)
        elif self.correct_num == 5 and pb_number1 != pb_number2:
            print(Fore.GREEN, "\n\t\t\t\t- 5 Correct White Balls, but no Powerball: $1,000,000", Fore.RESET)
        elif self.correct_num == 4 and pb_number1 == pb_number2:
            print(Fore.GREEN, "\n\t\t\t\t- 4 Correct White Balls and The Powerball: $10,000", Fore.RESET)
        elif self.correct_num == 4 and pb_number1 != pb_number2:
            print(Fore.GREEN, "\n\t\t\t\t- 4 Correct White Balls, but no Powerball: $100", Fore.RESET)
        elif self.correct_num == 3 and pb_number1 == pb_number2:
            print(Fore.GREEN, "\n\t\t\t\t- 3 Correct White Balls and The Powerball: $100", Fore.RESET)
        elif self.correct_num == 3 and pb_number1 != pb_number2:
            print(Fore.GREEN, "\n\t\t\t\t- 3 Correct White Balls, but no Powerball: $7", Fore.RESET)
        elif self.correct_num == 2 and pb_number1 == pb_number2:
            print(Fore.GREEN, "\n\t\t\t\t- 2 Correct White Balls and The Powerball: $7", Fore.RESET)
        elif self.correct_num == 1 and pb_number1 == pb_number2:
            print(Fore.GREEN, "\n\t\t\t\t- 1 Correct White Balls and The Powerball: $4", Fore.RESET)
        elif self.correct_num == 0 and pb_number1 == pb_number2:
            print(Fore.GREEN, "\n\t\t\t\t- No White Balls and The Powerball: $4", Fore.RESET)
        else:
            print(Fore.GREEN, "\n\t\t\t\t- Try again!", Fore.RESET)


price_a = Price()
price_a.Pricefunction()
