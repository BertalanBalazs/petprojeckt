import time
import os
import termios
import tty
import sys

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def stopwatch(seconds):
    timer = int(time.time())
    while int(time.time()) < timer+seconds:
        pass
    if int(time.time()) >= timer+seconds:
        timer_two = int(time.time())
        return timer_two - timer

print(stopwatch(4))