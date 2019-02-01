#!/usr/bin/env python
# coding: utf-8

# In[7]:


from IPython.display import clear_output
import random

class Hangman():
    lives = 7
    guess_list = []
    correct_list = []
    
    def __init__(self, difficulty = 1, hangman_ans = ''):
        self.difficulty = difficulty
        self.hangman_ans = hangman_ans
           
        
    def sports(self):
        
        difficulty = int(input('Please enter what difficulty leve you would like to play at. 1 - Easy. 2 - Medium. 3 - Hard.'))
        if difficulty == 1:
            hangman.lives = 7
        elif difficulty == 2:
            hangman.lives = 5
        elif difficulty == 3:
            hangman.lives = 3
        else:
            difficulty = int(input('Not a valid number. Please enter what difficulty leve you would like to play at. 1 - Easy. 2 - Medium. 3 - Hard.'))
        
        sports_list = ['Bruins', 'Patriots', 'Yankees', 'Devils', 'Magic', 'Celtics', 'Chiefs', 'Rangers', 'Coyotes', 'Diamondbacks']
        hangman_ans_og = random.choice(sports_list)
        hangman_ans = hangman_ans_og.lower()
        hangman_ans = list(hangman_ans)
        hangman_hidden = " _ "*len(hangman_ans)
        hangman.guess_list = []
        hangman.correct_list = []

        
        clear_output()
        
        def userGuess():

            guess = input('Guess a letter or solve: ')
            guess = guess.lower()
            hangman.guess_list.append(guess)

            if guess in hangman_ans:
                hangman.correct_list.append(guess)
                hangman_hidden = " ".join(c if c in hangman.correct_list else '_' for c in hangman_ans)
                clear_output()
                print('Correct! Lives left: {}. Guessed letters: {}'.format(hangman.lives, hangman.guess_list))
                print(hangman_hidden)
                userGuess()

            elif guess == hangman_ans_og.lower():
                print('You solved it! {} is the word! '.format(hangman_ans_og))

            elif guess not in hangman_ans:
                hangman.lives = hangman.lives - 1
                print('Wrong. You lost a life. Lives left: {}. Guessed letters: {}'.format(hangman.lives, hangman.guess_list))
                if hangman.lives == 0:
                    print('Game Over')
                    exit()
                elif hangman.lives > 0:
                    userGuess()


        print(hangman_hidden)

        userGuess()
        
    def countries(self):
        difficulty = int(input('Please enter what difficulty leve you would like to play at. 1 - Easy. 2 - Medium. 3 - Hard.'))
        if difficulty == 1:
            hangman.lives = 7
        elif difficulty == 2:
            hangman.lives = 5
        elif difficulty == 3:
            hangman.lives = 3
        else:
            difficulty = int(input('Not a valid number. Please enter what difficulty leve you would like to play at. 1 - Easy. 2 - Medium. 3 - Hard.'))
        
        countries_list = ['Russia', 'Australia', 'Italy', 'Greece', 'Canada', 'Liechenstein', 'Austria', 'Norway', 'Finland', 'Mongolia']
        hangman_ans_og = random.choice(countries_list)
        hangman_ans = hangman_ans_og.lower()
        hangman_ans = list(hangman_ans)
        hangman_hidden = " _ "*len(hangman_ans)
        hangman.guess_list = []
        hangman.correct_list = []
        
        clear_output()

        
        def userGuess():

            guess = input('Guess a letter or solve: ')
            guess = guess.lower()
            hangman.guess_list.append(guess)

            if guess in hangman_ans:
                hangman.correct_list.append(guess)
                hangman_hidden = " ".join(c if c in hangman.correct_list else '_' for c in hangman_ans)
                clear_output()
                print('Correct! Lives left: {}. Guessed letters: {}'.format(hangman.lives, hangman.guess_list))
                print(hangman_hidden)
                userGuess()

            elif guess == hangman_ans_og.lower():
                print('You solved it! {} is the word! '.format(hangman_ans_og))

            elif guess not in hangman_ans:
                hangman.lives = hangman.lives - 1
                print('Wrong. You lost a life. Lives left: {}. Guessed letters: {}'.format(hangman.lives, hangman.guess_list))
                if hangman.lives == 0:
                    print('Game Over')
                    exit()
                elif hangman.lives > 0:
                    userGuess()


        print(hangman_hidden)

        userGuess()
        
        
    def towns(self):
        difficulty = int(input('Please enter what difficulty leve you would like to play at. 1 - Easy. 2 - Medium. 3 - Hard.'))
        if difficulty == 1:
            hangman.lives = 7
        elif difficulty == 2:
            hangman.lives = 5
        elif difficulty == 3:
            hangman.lives = 3
        else:
            difficulty = int(input('Not a valid number. Please enter what difficulty leve you would like to play at. 1 - Easy. 2 - Medium. 3 - Hard.'))
        
        towns_list = ['Attleboro', 'Milford', 'Reading', 'Somerville', 'Lowell', 'Haverhill', 'Methuen', 'Peabody', 'Belchertown', 'Amherst']
        hangman_ans_og = random.choice(towns_list)
        hangman_ans = hangman_ans_og.lower()
        hangman_ans = list(hangman_ans)
        hangman_hidden = " _ "*len(hangman_ans)
        hangman.guess_list = []
        hangman.correct_list = []
        
        clear_output()

        
        def userGuess():

            guess = input('Guess a letter or solve: ')
            guess = guess.lower()
            hangman.guess_list.append(guess)

            if guess in hangman_ans:
                hangman.correct_list.append(guess)
                hangman_hidden = " ".join(c if c in hangman.correct_list else '_' for c in hangman_ans)
                clear_output()
                print('Correct! Lives left: {}. Guessed letters: {}'.format(hangman.lives, hangman.guess_list))
                print(hangman_hidden)
                userGuess()

            elif guess == hangman_ans_og.lower():
                print('You solved it! {} is the word! '.format(hangman_ans_og))

            elif guess not in hangman_ans:
                hangman.lives = hangman.lives - 1
                print('Wrong. You lost a life. Lives left: {}. Guessed letters: {}'.format(hangman.lives, hangman.guess_list))
                if hangman.lives == 0:
                    print('Game Over')
                    exit()
                elif hangman.lives > 0:
                    userGuess()


        print(hangman_hidden)

        userGuess()
    
    
    
    
hangman = Hangman()    
    
while True:
    try:
    # ask user which category they would like to play
        category = int(input('Welcome to Hangman. To start, please enter a category number. 1 - Sports Teams. 2 - for Countries. 3 - for Towns in Massachusetts. 4 - Quit '))
    except ValueError:
        print('Enter a number between 1 and 4. ')
        continue
    if category == 1:
        hangman.sports() # run sports method
    elif category == 2:
        hangman.countries() # run countries method
    elif category == 3: 
        hangman.towns() # run towns method
    elif category == 4:
        break # quit program

