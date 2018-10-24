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
        key = getch().lower()
        if key == "f":
            songs_menu(1)
        elif key == "v":
            songs_menu(2)
        elif key == "j":
            songs_menu(3)
        else:
            raise ValueError
    except ValueError:
        print("Invalid option or value!")
        sleep(1.5)
        start_menu()


def songs_menu(num):
    os.system("clear")
    if num == 1:
        print(get_menu_txts("Flute menu.txt"))
    elif num == 2:
        print(get_menu_txts("Violin menu.txt"))
    else:
        print(get_menu_txts("ZÁMBÓ menu.txt"))
    key = getch().lower()
    if key == "p":
        if num == 1:
            play_song('Emotional_Flute.mp3', num)
        elif num == 2:
            play_song('bad_violin.mp3', num)
        else:
            play_song('Zámbó_first.mp3', num)
    elif key == "s":
        p.stop()
    elif key == "q":
        start_menu()
    elif key == "f":
        fixer_menu(num)
    else:
        songs_menu(num)


def play_song(songname, num):
    os.system("clear")
    print(get_menu_txts("PLAY menu.txt"))
    p = vlc.MediaPlayer(songname)
    p.play()
    while True:
        try:
            if getch().lower() == "s":
                p.stop()
                songs_menu(num)
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
                print("The next game is uppon on your creativity!")
                sleep(4)
                final_musicar_game(num)
                sleep(10)
        else:
            print("Do you want to try this again? \n Press 'y' to try again \n Press 'n' to go back to the main menu.")
            if getch() == "y":
                os.system("clear")
                print("Good, gooood!")
                sleep(3)
                fixer_menu(num)
            elif getch() == "n":
                os.system("clear")
                print("Az vesse rám az első követ aki még nem csinált ilyet MI??")
                sleep(8)
                start_menu()
            else:
                print("What are you want to do? Please enter y or n!")
    elif int(num) == 2:
        question_one = input("What is the common in the ÚJPEST FC and Mága Zoltán?")
        if question_one in ["violin"]:
            os.system("clear")
            sleep(2)
            print("Vég az eszed mint a menzás kés, Brávó!")
            sleep(2)
            print("Lássuk a következő szintet!")
            sleep(4)
            final_musicar_game(num)
    elif int(num) == 3:
        question_one = input("Mond egy szót amiben benne van 'Zámbó Jimmy'?")
        sleep(1)
        if question_one in ["Koporsó", "koporsó", "koporso", "úrna", "isten", "király"]:
            os.system("clear")
            print("Így van! Habár elment, zenéivel örökre velünk marad!")
            sleep(4)
        elif question_one in ["?", "??", "nem tom", "passz", "nem tudom", "???"]:
            print("Sajnos a válasz a koporsó! Emlékezzünk róla tisztelettel!")
            sleep(4)
        else:
            print("Nem nem nem nyert most! Sajnos a válasz a koporsó! Emlékezzünk róla tisztelettel!")
            sleep(4)
        print("Change to english you want to fix jimmy's song don't you??!")
        sleep(3)
        print("Okey the task is coming for you!")
        final_musicar_game(num)


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


"""def fixer_game_two():
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
                fixer_game_two()"""


# fixer_game_two()


def fixer_game_three():
    os.system("clear")
    print("PREPARE FOR YOU BIGGEST CHALLENGE IN YOUR LIFE!")
    sleep(3)
    print("JIMMY NEM LEHET KIJAVÍTANI EMBER!!!!!!")
    congratulions_player('Zámbó.mp3', 3)


def final_musicar_game(num):
    if num == 1:
        print(get_menu_txts("music_player_flute.txt"))
        while True:
            key = getch().lower()
            if key == "a":
                p = vlc.MediaPlayer("flute_a.mp3")
                p.play()
            elif key == "s":
                p = vlc.MediaPlayer("flute_s.mp3")
                p.play()
            elif key == "d":
                p = vlc.MediaPlayer("flute_d.mp3")
                p.play()
            elif key == "f":
                p = vlc.MediaPlayer("flute_f.mp3")
                p.play()
            elif key == "j":
                p = vlc.MediaPlayer("flute_j.mp3")
                p.play()
            elif key == "k":
                p = vlc.MediaPlayer("flute_k.mp3")
                p.play()
            elif key == "l":
                p = vlc.MediaPlayer("flute_l.mp3")
                p.play()
            elif key == "é":
                p = vlc.MediaPlayer("flute_é.mp3")
                p.play()
            elif key == "q":
                False
                finish_game(num)
    if num == 2:
        print(get_menu_txts("music_player_violin.txt"))
        while True:
            key = getch().lower()
            if key == "a":
                p = vlc.MediaPlayer("violin_a.mp3")
                p.play()
            elif key == "s":
                p = vlc.MediaPlayer("violin_s.mp3")
                p.play()
            elif key == "d":
                p = vlc.MediaPlayer("violin_d.mp3")
                p.play()
            elif key == "f":
                p = vlc.MediaPlayer("violin_f.mp3")
                p.play()
            elif key == "j":
                p = vlc.MediaPlayer("violin_j.mp3")
                p.play()
            elif key == "k":
                p = vlc.MediaPlayer("violin_k.mp3")
                p.play()
            elif key == "l":
                p = vlc.MediaPlayer("violin_l.mp3")
                p.play()
            elif key == "é":
                p = vlc.MediaPlayer("violin_é.mp3")
                p.play()
            elif key == "q":
                False
                finish_game(num)
    if num == 3:
        print(get_menu_txts("music_player_piano.txt"))
        while True:
            key = getch().lower()
            if key == "a":
                p = vlc.MediaPlayer("piano_a.mp3")
                p.play()
            elif key == "s":
                p = vlc.MediaPlayer("piano_s.mp3")
                p.play()
            elif key == "d":
                p = vlc.MediaPlayer("piano_d.mp3")
                p.play()
            elif key == "f":
                p = vlc.MediaPlayer("piano_f.mp3")
                p.play()
            elif key == "j":
                p = vlc.MediaPlayer("piano_j.mp3")
                p.play()
            elif key == "k":
                p = vlc.MediaPlayer("piano_k.mp3")
                p.play()
            elif key == "l":
                p = vlc.MediaPlayer("piano_l.mp3")
                p.play()
            elif key == "é":
                p = vlc.MediaPlayer("piano_é.mp3")
                p.play()
            elif key == "q":
                False
                finish_game(num)


def finish_game(num):
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
        if num == 1:
            congratulions_player('titanic_fixed.mp3', num)
        elif num == 2:
            congratulions_player('good_violin.mp3', num)
        else:
            congratulions_player('zámbó.mp3', num)
    else:
        start_menu()


def congratulions_player(songname, num):
    os.system("clear")
    if num == 3:
        print(get_menu_txts("Jimmy_player.txt"))
    else:
        print(get_menu_txts("Congratulation_player.txt"))
    p = vlc.MediaPlayer(songname)
    p.play()
    while True:
        try:
            if getch().lower() == "s":
                p.stop()
                start_menu()
                False
            else:
                raise ValueError
        except ValueError:
            print("Invalid value!")
            continue
    sleep(15)


start_menu()
