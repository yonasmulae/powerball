import random

print("\n******************** WELCOME TO POWERBALL GAME *********************\n")


class Whiteball_n:
    whiteball_numbers = []

    def whiteball_num(self):
        for whitenum in range(0, 5):
            w_number = random.randint(1, 20)
            self.whiteball_numbers.append(w_number)
        self.whiteball_numbers.sort()


w_ball = Whiteball_n()
w_ball.whiteball_num()