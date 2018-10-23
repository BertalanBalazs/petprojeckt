import vlc
from time import sleep
import time
import os
import termios
import tty
import sys
import random


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_menu_txts(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    return ''.join(lines)

def start_menu():
    try:
        os.system("clear")
        print(get_menu_txts("Main menu.txt"))
        if getch().lower() == "f":
            fix_songs(1)
        elif getch().lower() == "v":
            fix_songs(2)
        elif getch().lower() == "j":
            fix_songs(3)
        else:
            raise ValueError
    except ValueError:
        print("Invalid option or value!")
        sleep(1.5)
        start_menu()


def fix_songs(num):
    os.system("clear")
    if num == 1:
        print(get_menu_txts("Flute menu.txt"))
    if getch() == "p":
        if num == 1:
            play_song('Emotional_Titanic_Flute.mp3', num)
        elif num == 2:
            play_song('bad_violin.mp3', num)
        else:
            play_song('Zámbó.mp3', num)
    elif getch() == "s":
        p.stop()
    elif getch() == "q":
        start_menu()
    elif getch() == "f":
        fixer_menu(num)
    else:
        fix_songs(num)


def play_song(songname, num):
    os.system("clear")
    player = """
                 Enjoy it?? I don't think so...
                 Fix it to your ear is not blooding in the further!
                 
                    Press("s") to stop and go back to the song menu."""
    print(player)
    p = vlc.MediaPlayer(songname)
    p.play()
    while True:
        try:
            if getch() == "s":
                p.stop()
                fix_songs(num)
                False
            else:
                raise ValueError
        except ValueError:
            print("Invalid value!")
            continue
    sleep(15)


def fixer_menu(num):
    os.system("clear")
    if int(num) == 1:
        question_one = input("What was shunk at the Tinanic catasrophe?")
        if question_one.lower() in ["titanic", "ship", "dicaprio"]:
            os.system("clear")
            sleep(2)
            print("Honestly, you're a genious!")
            sleep(2)
            print("Let see the next game!")
            sleep(4)
            if fixer_game() == "yes":
                sleep(2)
                print("Nice job!!")
                sleep(0.7)
                os.system("clear")
                print("Okay the finish comes for you!!")
                sleep(0.7)
                print("You have to drink a glass of water before you start it!")
                sleep(4)
                finish_game()
        else:
            print("Do you want to try this again? \n Press 'y' to try again \n Press 'n' to go back to the main menu.")
            if getch() == "y":
                os.system("clear")
                print("Good, gooood!")
                sleep(3)
                fixer_menu()
            elif getch() == "n":
                os.system("clear")
                print("Az vesse rám az első követ aki még nem csinált ilyet MI??")
                sleep(8)
                start_menu()
            else:
                print("What are you want to do? Please enter y or n!")
    elif int(num) == 2:
        question_one = input("Milyen tipusú hangszeren játszik a vonós?")
        if question_one in ["vonós", "vonóson", "hegedűn"]:
            os.system("clear")
            sleep(2)
            print("Ha én lettem volna a tehelyben nem tudtam volna, Brávó!")
            sleep(2)
            print("Lássuk a következő szintet!")
            sleep(4)
            fixer_game_two()
    elif int(num) == 3:
        pass


def fixer_game():
    life = 2
    boolen = True
    while boolen:
        os.system("clear")
        row = '♬ ' * 25 + '\n'
        table = [list(row) for i in range(9)]
        even_nums = [num for num in range((len(row)-2)) if num % 2 == 0]
        print("\n LIFE:", life, "\n")
        random_number = random.randint(6, 12)
        print(random_number)
        for i in range(random_number):
            table[random.randint(0, 8)][random.choice(even_nums)] = "♫"
        for row in table:
            print(''.join(row))
        guess_number = input("Hány kakukktojást látsz a táblán?")
        try:
            if int(guess_number) == random_number:
                boolen = False
                print("That correct! You're awesome!")
                return "yes"
            else:
                life -= 1
                if life == 0:
                    print("You don't have enough life sorry! Goodbye!")
                    False
                    start_menu()
                else:
                    print("Do you want to play again? One life is down! \n Press 'y' for again! \n Press 'n' for go to the main menu!")
                    if getch() == "y":
                        continue
                    else:
                        print("Nothing problem! :D (OMG...)")
                        sleep(2)
                        start_menu()
        except ValueError:
            print("Incorret Value!")


def fixer_game_two():
    row = '♬ ' * 20 + '\n'
    table = [list(row) for i in range(9)]
    even_nums = [num for num in range((len(row)-2)) if num % 2 == 0]
    table_new = [''.join(row) for row in table]
    random_multiples = [random.choice(even_nums) for i in range(8)]
    random_multiple_two = random.choice(even_nums)
    f = random_multiple_two
    print(''.join(table_new))
    for i in range(9):
        Boolen = True
        while Boolen:
            try:
                if table_new[i][random_multiples[0]] == "W":
                    raise IndexError
                table_new[i] = list(table_new[i])
                table_new[8] = list(table_new[8])
                table_new[i-2] = list(table_new[i-2])
                table_new[i][random_multiples[0]] = "X"
                if i > 1:
                    table_new[i-2][random_multiples[1]] = "X"
                table_new[8][random_multiples[0]] = "W"
                try:
                    timer = int(time.time())
                    while int(time.time()) < timer+2:
                        if getch().lower() == 'a' and int(time.time()) < timer+2:
                            os.system("clear")
                            f -= 2
                            table_new[8][random_multiples[0]] = "♬"
                            table_new[8][f+2] = "♬"
                            table_new[8][f] = "W"
                            break
                        elif getch().lower() == 'd' and int(time.time()) < timer+2:
                            os.system("clear")
                            f += 2
                            table_new[8][random_multiples[0]] = "♬"
                            table_new[8][f-2] = "♬"
                            table_new[8][f] = "W"
                            break                 
                        elif getch().lower() not in ['a','d'] and int(time.time()) < timer+2:
                            os.system("clear")
                            table_new[8][random_multiples[0]] = "♬"
                            table_new[8][f] = "W"
                            raise ValueError
                            break
                        else:
                            os.system("clear")
                            print("You have to be faster!")
                            sleep(3)
                            os.system("clear")
                            table_new[8][random_multiples[0]] = "♬"
                            break

                    table_new[i] = ''.join(table_new[i])
                    table_new[8] = ''.join(table_new[8])
                    table_new[i-2] = ''.join(table_new[i-2])
                    print(''.join(table_new))
                    sleep(0.1)
                    table_new[i] = '♬ ' * 20 + '\n'
                    table_new[i-2] = '♬ ' * 20 + '\n'
                    Boolen = False
                except ValueError:
                    print("Maan pls press 'a' or 'b'!!")
                    table_new[i] = ''.join(table_new[i])
                    table_new[8] = ''.join(table_new[8])
                    table_new[i-2] = ''.join(table_new[i-2])
                    print(''.join(table_new))
                    os.system("clear")
                    table_new[i] = '♬ ' * 20 + '\n'
                    table_new[i-2] = '♬ ' * 20 + '\n'
            except IndexError:
                print("You lose! I think you really enjoy the sitthy songs man!")
                sleep(8)
                fixer_game_two()


#fixer_game_two()


def fixer_game_three():
    pass


def finish_game():
    os.system("clear")
    welcome = """
              ______________________________________________
             |                                              |      
             |      WELCOME IN THE DEATH VALLEY!!           |   
             |                                              |   
             |          THAT IS A BATTLE GAME               |
             |                                              |   
             | TASK: You have to trhow the basketball       |
             |  to the basket at least 5 time!              |
             |  Be carefull the timer is fast!!             |
             \______________________________________________/ """
    print(welcome)
    sleep(12)
    print("Firstly, I have to know do you realy want to fix the music??")
    print("At the finish you can be a depressionist man! Seriously! \n Press 'y' for of course i want!!! \n Press 'n' if you want to risk your life!")
    if getch() == "y":
        print("All right the counter is starting now!")
        for i in range(6):
            sleep(1)
            print(i)
        print("START")
        congratulions('titanic_fixed.mp3')
    else:
        start_menu()


def congratulions(songname):
    Final = """
            ____________________________________________________________________________________________________________
            |                                                                                                          |
            |                    YOU SUCCESFULLY FIXED THE SONG!! YOU'RE ABSOLUTELY INCREDIBLE!!!!!                    |
            \__________________________________________________________________________________________________________/ """
    print(Final)
    p = vlc.MediaPlayer(songname)
    p.play()
    sleep(15)
    p.stop()
    start_menu()


start_menu()
