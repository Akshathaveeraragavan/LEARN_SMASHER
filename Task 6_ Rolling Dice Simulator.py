# THIS IS A DICE ROLLER SIMULATOR
import random

def roll_dice():
    print('Hey user , Welcome to our dice roller application!')
    no_dice=int(input('How many dice would you like to roll?'))
    if no_dice<1:
        print('Invalid choice!Please try again')
    else:
        for i in range(no_dice):
            print('Dice',i,'is rolling...')
            print('Dice',i,'gives',random.randint(1,6))
    
while True:
    roll_dice()
    roll_again=input('Would you like to roll again? Y/N')
    if (roll_again=='Y' or roll_again=='y'):
        continue
    else:
        print('Thanks for using the application')
        break
