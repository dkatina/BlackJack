import os
from colorama import Fore, Style, Back, init

#init for colorama to fixed windows wierdness
init()

#*--> CLEAR SCREEN FUNCTION
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

#*--> PRINT_*** PRINTS OUPUT MESSAGING TO CORRESPONDING COLOR
def print_yellow(s):
    print(Fore.YELLOW, Style.BRIGHT, s, Style.RESET_ALL)

def print_red(s):
    print(Fore.RED, Style.BRIGHT, s, Style.RESET_ALL)

def print_blue(s):
    print(Fore.BLUE, Style.BRIGHT, s, Style.RESET_ALL)

def print_green(s):
    print(Fore.GREEN, Style.BRIGHT, s, Style.RESET_ALL)

#*--> INPUT_*** PRINTS INPUT PROMPTS TO CORRESPONDING COLOR
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


def print_red_cards(value, suit):
    print(Fore.RED, Back.WHITE, Style.DIM, f'{value.title()} of {suit.title()}', Style.RESET_ALL, end='   ')

def print_black_cards(value, suit):
    print(Fore.BLACK, Back.WHITE, Style.DIM,f'{value.title()} of {suit.title()}', Style.RESET_ALL, end='   ')

def print_unkown():
    print(Fore.RED, Back.WHITE, Style.DIM, ' Unknown  ', Style.RESET_ALL, end='   ')

   
    