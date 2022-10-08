# Hangmann game
def halt():
    if chance == 5:
        print('''
          +--------+
          |   |
          |
          |
          |
          |
    =========
     ''')
    elif chance == 4:
        print('''   
                +--------+
                  |   |
                  |   O
                  |
                  |
                  |
            =========


     ''')
    elif chance == 3:

        print('''
           ++--------+
             |   |
             |   O
             |  /|
             |   |
             |
          =========

     ''')
    elif chance == 2:

        print('''
           +---+
           |   |
           |   O   
           |  /|\  
           |   |
           |   |
           ========

     ''')
    elif chance == 1:

        print('''
           +---+
           |   |
           |   O   
           |  /|\  
           |   |
           |  /
           ========

     ''')
    elif chance == 0:

        print('''
           +---+
           |   |
           |   O   
           |  /|\  
           |   |
           |  / / 

           ========

     ''')


import random
import hangman_words

word = []

print("*****Welcome to Hangman game*****")
print('''

 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
                   ''')
x = random.choice(hangman_words.word_list)
print(f"you should guess the word of length {len(x)}\n\n")

for element in list(x):
    word.append("-")
print("".join(word))
chance = 6

while "-" in word and chance != 0:
    geuss = input("enter a letter to guess your word\n")

    if geuss not in list(x):
        chance = chance - 1
        halt()
    else:

        for i in range(0, len(x)):
            if geuss == x[i]:
                word[i] = geuss
        print("".join(word))
else:
    print("game over.")

print(f"your word is {x}")

