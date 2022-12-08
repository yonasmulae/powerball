from Whiteball import Whiteball_n
from Userball import Userball_n


class Correct_n(Whiteball_n, Userball_n):
    correct_num = 0

    def correct_number(self):
        self.whiteball_num()
        self.userball_num()
        for i in self.whiteball_numbers:
            if i in self.user_numbers:
                self.correct_num += 1
        return self.correct_num


c = Correct_n()

