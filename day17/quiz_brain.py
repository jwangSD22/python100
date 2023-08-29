from question_model import Question
from data import question_data
import random
import html



question_bank = []

for item in question_data:
    question_bank.append(Question(html.unescape(item['question']), item['correct_answer']))


class QuizBrain:
    def __init__(self):
        self.question = None
        self.player_choice = ''

    def load_question(self):
        self.question = random.choice(question_bank)

    def ask_question(self):
        print(f'{self.question.text}\n')
        self.player_choice = input(f'True or False?  ')

    def check_answer(self):
        if self.player_choice.lower() == self.question.answer.lower():
            return True
        return False
