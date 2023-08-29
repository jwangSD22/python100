from quiz_brain import QuizBrain
import os


def clear_console():
    os.system('cls')



class Game:
    def __init__(self):
        self.chances = 10
        self.quiz_brain = QuizBrain()
        self.score = 0

    def reset_score(self):
        clear_console()
        self.chances = 10
        self.score = 0

    def initialize_game(self):
        play_again = True

        while play_again:

            self.quiz_brain.load_question()
            self.quiz_brain.ask_question()
            if self.quiz_brain.check_answer():
                self.score += 1
                print(f'\nCorrect!! Score: {self.score}/10\n')
                self.chances -= 1
            else:
                print(f'\nIncorrect. Score: {self.score}/10\n')
                self.chances -= 1

            if self.chances == 0:
                while True:
                    print(f'FINAL SCORE: {self.score}/10\n')
                    selection = input('Play again? (y)es or (n)o')
                    if selection == 'y':
                        self.reset_score()
                        break

                    elif selection == 'n':
                        play_again = False
                        break
                    else:
                        print('Please select a valid option (y)es or (no ')

        print('Thanks for playing!')


game = Game()

game.initialize_game()
