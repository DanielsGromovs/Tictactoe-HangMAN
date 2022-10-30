
from colorama import Fore
from words import words
import os
import random
l = 7
guesses = []
false = []
done = False

#get random word from list without spaces or dashes
while True:
    word = random.choice(words)
    if '-' not in word and ' ' not in word:
        break

os.system('cls|clear')
print("""

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
""")
print('Vārdi ir angļu valodā un ir bez atstarpēm un domuzīmēm')

print(f"""
            _________
            |       {'|' if l == 6 else ' '}
            |       {'0' if l == 5 else ' '}
            |
            |
            |
        __________
""")
while not done:
    def display(l):
        slash = '\\'
        print(f"""
            _________
            |       {'|' if l <= 6 else ' '}
            |       {'0' if l <= 5 else ' '}
            |      {'/' if l <= 3 else ' '}{'|' if l <= 4 else ' '}{slash if l <= 2 else ''}
            |      {'/' if l <= 1 else ' '}{' ' + slash if l == 0 else ''}
            |
        __________
         """)
    print('minētie burti: ',' '.join(guesses))
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    guess = str(input("Uzmini burtu: "))
    if guess.isnumeric() or len(guess) == 0 or len(guess) > 1 or ' ' in guess:
        print(Fore.RED+'Ievadiet vienu burtu'+Fore.RESET)
    else:
        if guess.lower() not in guesses:
            guesses.append(guess.lower())
        if letter.lower() in word:
            print(Fore.GREEN+'\nPAREIZI\n'+Fore.RESET)
        if guess.lower() not in word.lower():
            if guess.lower() in false:
                print('Tu jau šo burtu minēji.')
                display(l)
                continue
            else:
                l -= 1
                display(l)
                print(Fore.RED + 'NEPAREIZI\n'+ Fore.RESET)
            false.append(guess)
            if l == 0:
                break
        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False
        if guess.lower() == word:
            done = True
else:
    print('Vārds ir ', word)
    print(Fore.YELLOW+"""
▀█▀ █░█   █░█ ▀█ █░█ ▄▀█ █▀█ █▀▀ ░░█ █
░█░ █▄█   █▄█ █▄ ▀▄▀ █▀█ █▀▄ ██▄ █▄█ █
    """+Fore.RESET)
    exit()
print(f'Tu zaudēji. Vārds bija {word}')
