from colorama import Fore
import os
import random


won = False
slots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
history = []
turn = "X"

# Priekš loop
active = True

difficulty = input("Izvēlies grūtības līmeni: (PVP) - Bez ai, (E) - viegli, (H) - sarežģīti: ").lower()


# Spēles galds
def board():
    board = (
        f"\n"
        f" {slots[0]} │ {slots[1]} │ {slots[2]}\n"
        "───┼───┼───\n"
        f" {slots[3]} │ {slots[4]} │ {slots[5]}\n"
        "───┼───┼───\n"
        f" {slots[6]} │ {slots[7]} │ {slots[8]}\n "
    )
    print(
        board.replace("X",Fore.RED + "X" + Fore.RESET).replace(
            "O",Fore.BLUE + "O" + Fore.RESET
        )
    )
    
# Uzvaras pārbaude
def winner(slots):
    if (
        (slots[0] == slots[1] == slots[2])
        or (slots[3] == slots[4] == slots[5])
        or (slots[6] == slots[7] == slots[8])
    ):
        return True
    elif (
        (slots[0] == slots[3] == slots[6])
        or (slots[1] == slots[4] == slots[7])
        or (slots[2] == slots[5] == slots[8])
    ):
        return True
    elif (slots[0] == slots[4] == slots[8]) or (slots[2] == slots[4] == slots[6]):
        return True
    elif len(history) == 10:
        return "tie"
    else:
        return False

# Mākslīgais intelekts
def ai_move_hard():
    for i in range(9):
        if slots[i] != "X" and slots[i] != "O":
            slots[i] = "O"
            if winner(slots):
                return
            else:
                slots[i] = str(i + 1)

    for i in range(9):
        if slots[i] != "X" and slots[i] != "O":
            slots[i] = "X"
            if winner(slots):
                slots[i] = "O"
                return
            else:
                slots[i] = str(i + 1)

    if slots[4] != "X" and slots[4] != "O":
        slots[4] = "O"
        return
    corners = [0, 2, 6, 8]
    random.shuffle(corners)
    for i in corners:
        if slots[i] != "X" and slots[i] != "O":
            slots[i] = "O"
            return
    sides = [1, 3, 5, 7]
    random.shuffle(sides)
    for i in sides:
        if slots[i] != "X" and slots[i] != "O":
            slots[i] = "O"
            return
    return

board()
while active:
    winner(slots)
    if winner(slots) == False:
        print(f"-{turn} kārta-")

        if turn == "X":
            player = input("\nIzvēlaties kvadrātu: ")
            if player in history:
                history.pop(-1)
                print("Šis kvadrāts jau ir aizņemts!")
                player = input("\nIzvēlaties kvadrātu: ")
        history.append(player)       

        if active == True:
            if turn == "X":
                if slots[int(player) - 1] not in ("X", "O"):
                    slots[int(player) - 1] = "X"
                    turn = "O"
            else:
                if difficulty == "h":
                    ai_move_hard()
                    turn = "X"
                elif difficulty == "e":
                    #dumjais prāts
                    igors = random.choice(slots)
                    if igors not in ("X", "O"):
                        slots[int(igors) - 1] = "O"
                        turn = "X"
                elif difficulty == "pvp":
                  player = input("\nIzvēlaties kvadrātu: ")
                  if slots[int(player) - 1] not in ("X", "O"):
                    slots[int(player) - 1] = turn
                    if turn == "X":
                        turn = "O"
                    else:
                        turn = "X"
    elif winner(slots) == "tie":
        print("Tie")
        active = False
    else:
        active = False
    os.system("cls")
    board()

if turn == "X":
    turn = "O"
else:
    turn = "X"
print("Neizšķirts\n" if winner(slots) == "tie" else f"{turn} uzvarēja!")