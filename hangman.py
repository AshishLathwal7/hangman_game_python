import pandas as pd
import numpy as np
import random
import hangman_art

def print_blanks(lst):
    for l in lst:
        print(l,end=' ')
        


print(hangman_art.logo)
occupation_csv = pd.read_csv('occupations.csv')['Occupations']
#print(occupation_csv)
occupation_csv_length = len(occupation_csv)
#print(occupation_csv_length)
random_index = np.random.randint(0,occupation_csv_length)
occupation = occupation_csv.loc[random_index].lower()
#print(occupation)
occupation_length = len(occupation)
blanks = ['_'] * occupation_length
life = 6
result = 'You lost'

while life > 0:
    print_blanks(blanks)
    print()
    did_not_find = True
    guess = input("Guess a letter: ").lower()
    if guess in blanks:
        print(f'You have already guessed the letter {guess}')
        continue
    
    for i in range(0,occupation_length):
        if occupation[i] == guess:
            did_not_find = False
            blanks[i] = guess

    if did_not_find:
        life -= 1
        print(f'You have guessd letter {guess} which is incorrect. You lost a life, remaining life is {life}.')
    else:
        print(f'You have guessd letter {guess} which is correct!')    
    
    print(hangman_art.stages[life])

    if '_' not in blanks:
        result = "You won"
        print_blanks(blanks)
        print()
        break
    
if life == 0:
    print(occupation)

print(f"Game Over and {result} the game!")
exit()
