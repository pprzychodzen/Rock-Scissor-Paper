import random


# Simple game from childhood. Rock, scissor, paper. I belive the genesis of this game has some Japan roots
# You chose between rock, scissor and paper. Rock crack scissor, but paper wrap rock and of course scissors cuts paper
# Good luck!

class RockPaperScissor:
    def __init__(self, user_name):
        self.user_name = user_name
        self.random = random.Random()
        self.user_score = 0
        self.ai_score = 0
        self.round_number = 1

    def show_score(self):
        print(f"Round: {self.round_number}")
        print("Score:")
        print(f"{self.user_name} score is : {self.user_score}\nComputer score is : {self.ai_score}")

    def get_ai_answer(self):
        return self.random.randrange(1, 4)

    # Getting user answer with instruction how to choose your bet
    def get_user_answer(self):
        while True:
            print("-" * 15 + "\nWe are playing Rock | Scissors | Paper"
                  + "\n1 for Rock\n2 for Scissors\n3 for paper\n" + "-" * 15 + "\n")
            answer = input(f"{self.user_name} what's your move?\n")
            answer.strip()

            if answer == "1":
                return 1
            if answer == "2":
                return 2
            if answer == "3":
                return 3
            print("I'm sorry, I don't understand your answer. Please try again")

    def add_user_score(self):
        print(f"Point for {self.user_name}!")
        self.user_score += 1

    def add_ai_score(self):
        print("Point for computer!")
        self.ai_score += 1

    # Main method to decide who won the round
    def rsp(self, user, ai):
        if (user, ai) == (1, 2):
            print("Rock breaks scissors!")
            self.add_user_score()
        elif (user, ai) == (1, 3):
            print("Paper covers rock!")
            self.add_ai_score()
        elif (user, ai) == (2, 1):
            print(f"Rock breaks scissors!")
            self.add_ai_score()
        elif (user, ai) == (2, 3):
            print("Scissors cuts peper!")
            self.add_user_score()
        elif (user, ai) == (3, 1):
            print("Paper covers rock!")
            self.add_user_score()
        elif (user, ai) == (3, 2):
            print("Scissors cuts paper!")
            self.add_ai_score()
        else:
            print("It was a Tie!")

    def another_round(self):
        round = input("Another round? [Y/N]")
        round.strip()
        round.lower()
        self.round_number += 1
        if round == "n" or round == "no":
            return False
        elif round == 'y' or round == 'yes':
            return True
        else:
            print("Im sorry I don't understand. Let's try again!")
        self.another_round()

    def play(self):
        while True:

            user_answer = self.get_user_answer()
            ai_answer = self.get_ai_answer()
            self.rsp(user_answer, ai_answer)
            self.show_score()
            if self.another_round() is False:
                return print("Thank you, come again!")


game = RockPaperScissor(input("What's your name? "))
game.play()
