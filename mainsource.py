from Correctnumber import Correct_n
from Powerball import Powerball_n
from colorama import Fore


class Price(Correct_n, Powerball_n):

    def price_condition(self):
        self.correct_number()
        self.powerball_number()
        print("\n\t\t\t\t- The same amount numbers are ", self.correct_num)
        if self.correct_num == 5 and self.whiteball_numbers == self.user_numbers:
            print("\n\t\t\t\t- 5 Correct White Balls and The Powerball: $324,000,000")
        elif self.correct_num == 5 and self.whiteball_numbers != self.user_numbers:
            print("\n\t\t\t\t- 5 Correct White Balls, but no Powerball: $1,000,000")
        elif self.correct_num == 4 and self.whiteball_numbers == self.user_numbers:
            print("\n\t\t\t\t- 4 Correct White Balls and The Powerball: $10,000")
        elif self.correct_num == 4 and self.whiteball_numbers != self.user_numbers:
            print("\n\t\t\t\t- 4 Correct White Balls, but no Powerball: $100")
        elif self.correct_num == 3 and self.whiteball_numbers == self.user_numbers:
            print("\n\t\t\t\t- 3 Correct White Balls and The Powerball: $100")
        elif self.correct_num == 3 and self.whiteball_numbers != self.user_numbers:
            print("\n\t\t\t\t- 3 Correct White Balls, but no Powerball: $7")
        elif self.correct_num == 2 and self.whiteball_numbers == self.user_numbers:
            print("\n\t\t\t\t- 2 Correct White Balls and The Powerball: $7")
        elif self.correct_num == 1 and self.whiteball_numbers == self.user_numbers:
            print("\n\t\t\t\t- 1 Correct White Balls and The Powerball: $4")
        elif self.correct_num == 0 and self.whiteball_numbers == self.user_numbers:
            print("\n\t\t\t\t- No White Balls and The Powerball: $4")

        else:
            print(Fore.GREEN, "\n\t\t\t\t- Try again!", Fore.RESET)


p_fun = Price()
p_fun.price_condition()

