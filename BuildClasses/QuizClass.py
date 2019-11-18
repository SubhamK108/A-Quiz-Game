import random
import os
import json

class QuizApp:
    def __init__(self, name):
        self.Name = name
        self.Score = 0

    def StartScreen(self):
        os.system('clear')
        print('QUIZ GAME'.center(95, '.'))
        print(f'Welcome {self.Name}'.center(95))
        print('\n')
        print('GAME MENU'.center(95, '.'))
        print()
        print('1. Game Instructions')
        print('2. Start the Quiz')
        print('3. Exit')
        print('\n')
    
    def PlayGame(self):
        msgSuccess = ['Yay', 'Woohoo', "Hooray", 'Well Done', 'Nice', 'Great', 'Good Job']
        msgFailure = ['Oops', 'Oh No', 'Oh Oh', 'Sorry']
        raw_data = open(r'AppDatabase/Questions.json', 'r')
        data = json.load(raw_data)
        noOfQuestions = len(data)
        unusedQuestions = [i for i in range(noOfQuestions)]
        for i in range(10):
            os.system('clear')
            print('QUIZ GAME'.center(95, '.'))
            print('\n')
            random.seed(os.urandom(1024))
            obj = random.choice(unusedQuestions)
            unusedQuestions.remove(obj)
            print(f'Q.{i + 1}: {data[obj]["question"]}')
            for option in data[obj]['options']:
                print(option)
            answer = input("\nEnter your option: ")
            if answer[0].upper() in data[obj]['answer'][0]:
                print(f'\n{random.choice(msgSuccess)}, Your option is Correct !')
                self.Score += 1
            else:
                print(f'\n{random.choice(msgFailure)}, Your option is incorrect !')
            delay = input('\nPress Enter to view the next question... ')
        os.system('clear')
        print('RESULTS'.center(95, '.'))
        print('\n')
        print('OK, the Quiz has ended.')
        print(f'Your Final Score: {self.Score}')

    def ViewInstructions(self):
        os.system('clear')
        print('GAME INSTRUCTIONS'.center(95, '.'))
        print()
        print('1. Each round consists of 10 random questions.')
        print('2. To answer, enter the option (case insensitive).')
        print('3. Your final score will be displayed at the end of each round.')
        print('4. Each question consist of 1 Point and there are no negative markings for wrong options.')