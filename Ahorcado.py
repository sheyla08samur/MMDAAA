import random
import os

days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print ('THE HANGMAN')

playing= True
tried= True 
attemps= 0

randomDay= random.randint(0, len(days))
day= days [randomDay]

toguess= ['_'] * len(day)

while playing:
    os.system ('cls')
    print ('Guess the day of the week')
    for letter in toguess:
        print (letter, end= ' ')
    print ('\n')
    print(f'You have {3-attemps} left')
    tried=False                              # Esto por qué es necesario aqui?

    entered= input ('Enter the letter: ')

    for idx, letter in enumerate(day):
        if letter == entered:
            toguess[idx]=entered
            tried=True
        continue

    else:
        if tried == False:
            attemps += 1

    if attemps==3:
        print ('You lost the game')
        playing=False                        # Pq TF no sale el print a menos que ponga esta linea