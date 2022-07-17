import os
from colorama import Fore
from colorama import Style
from colorama import init

#init for colorama to fixed windows wierdness
init()

def print_yellow(s):
    print(Fore.YELLOW, Style.BRIGHT,s,Style.RESET_ALL)

def print_red(s):
    print(Fore.RED, Style.BRIGHT,s,Style.RESET_ALL)    

def print_blue(s):
    print(Fore.BLUE, Style.BRIGHT,s,Style.RESET_ALL)
    
def input_yellow(s):
    print(Fore.YELLOW, Style.BRIGHT, end='')
    response = input(s)
    print(Style.RESET_ALL)
    return response

def input_green(s):
    print(Fore.GREEN, Style.BRIGHT, end='')
    response = input(s)
    print(Style.RESET_ALL)
    return response

def input_red(s):
    print(Fore.RED, Style.BRIGHT, end='')
    response = input(s)
    print(Style.RESET_ALL)
    return response

def input_blue(s):
    print(Fore.BLUE, Style.BRIGHT, end='')
    response = input(s)
    print(Style.RESET_ALL)
    return response

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    

def print_diamonds():
    print(Fore.RED, Style.BRIGHT,'Diamonds' ,Style.RESET_ALL, end='   ')
def print_hearts():
    print(Fore.MAGENTA, Style.BRIGHT,'Hearts' ,Style.RESET_ALL, end='   ')
def print_clubs():
    print(Fore.GREEN, Style.BRIGHT,'Clubs' ,Style.RESET_ALL, end='   ')
def print_spades():
    print(Fore.CYAN, Style.BRIGHT,'Spades' ,Style.RESET_ALL, end='   ')