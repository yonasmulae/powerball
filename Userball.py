import random
from colorama import Fore


class Userball_n:
    user_numbers = []

    def userball_num(self):
        for usernum in range(0, 5):
            u_number = random.randint(1, 20)
            while u_number in self.user_numbers:
                u_number = random.randint(1, 20)
            self.user_numbers.append(u_number)
        self.user_numbers.sort()
        return self.user_numbers


u_ball = Userball_n()
# u_ball.userball_num()
