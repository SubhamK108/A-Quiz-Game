import BuildClasses.QuizClass as QC
import os

os.system('clear')
playerName = input('Enter your Name: ')

newPlayer = QC.QuizApp(playerName)

while (True):
    os.system('clear')
    newPlayer.StartScreen()
    choice = int(input('Enter you choice: '))
    if choice == 1:
        newPlayer.ViewInstructions()
    elif choice == 2:
        newPlayer.PlayGame()
    elif choice == 3:
        print('\n')
        print(f'Thank You for playing {playerName}'.center(95))
        print('\n')
        exit()
    else:
        print('\nInvalid Option !')
    delay = input('\nPress Enter to move back to the Main Menu... ')