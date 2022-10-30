import os
os.system("cls")
gameselect = input("tictactoe or hangman?:").lower()

#-------Tic Tac Toe Game-------#
if gameselect == "tictactoe":
    os.system('python tictactoe.py')


#-------HANGMAN GAME-------#
elif gameselect == "hangman":
    os.system('python hangman.py')