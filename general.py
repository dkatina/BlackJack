#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     *    BLACK<(21)>JACK      *
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     *  Created and perfected  *
#     *           By            *
#     *    Dylan K. & Jody S.   *
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~ SYSTEM IMPORTS ~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#*--> Deck import for deckofcardsapi.com to utilize 6 decks of cards at play
from deck import Deck
#*--> Time/Sleep imported for game timing to similate real game play
from time import sleep
#*--> Pyfiglet imported  ASCII text and renders it in ASCII art fonts
from pyfiglet import figlet_format
#*--> Python package that converts images into ASCII art for terminals
import ascii_magic
#*--> OS for clear screen functions across platforms
import os
import color21

# ~~~~~~ PROGRAM EXECUTION ~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#*--> Player actions including wager calculations,
#*--> drawing cards "Hit", win/lose/bust displays.
class Player():
    
    def __init__(self, name):
        self.name = name.title()
        self.bal = 0
        self.hand = []
        self.bet_amount = 0
        self.hand_v = 0
        self.aces = []
            
    def get_bal(self):
        return self.bal
    
    def bet(self):
        betting = True
        while betting:
            if self.bal > 0:
                bet = input(f'\n\n\n{self.name} you have ${self.bal}. How much would you like to bet? ')
                if not bet.isdigit():
                    color21.print_red("Invalid entry please try again.")
                    print()
                else:
                    bet = int(bet)
                    if bet <= self.bal:
                        
                        self.bal=(self.bal - bet)
                        self.pot=(self.bet_amount*2)
                        self.bet_amount = bet
                        return True
                    else:
                        print('You don\'t have enough money to place this bet')
                        more_chips=input('Would you like to buy more chips? Y/N?').lower().strip()
                        if more_chips == 'y':
                            self.bal=(self.bal + 1000)

                        else:
                            print(f'Please adjust your bet amount to continue playing')
            else:
                print('You don\'t have enough money to contiue')
                more_chips=input('Would you like to buy more chips? Y/N?').lower().strip()
                if more_chips == 'y':
                    self.bal=(self.bal+1000)
                    bet = 0
                else:
                    print(f'Thank you for playing, we look forward to nextime you wanna give us your money.')
                    return False

#*--> DISPLAY WAGER LOSS AMT ~~~~~~~~~~
    def lose_hand(self):
        print(f'\n\nYou lost $', self.bet_amount)
        self.bet_amount = 0

#*--> ADJUSTS PLAYERS BALANCE DUE TO TIE HAND ~~~~~~~~~~         
    def draw(self):
        print(f'\n\nYou got your Bet back')
        self.bal += (self.bet_amount)
        self.bet_amount = 0

#*--> ADJUSTS PLAYER BALANCE = PLAYER WAGER+DEALER WAGER ~~~~~~~~~~
    def win_hand(self):
        print(f'\n\nYou Won $', self.bet_amount)
        self.bal += (self.bet_amount *2)
        
#*--> DISPLAYS NAME, CARDS, & STATS OF PLAYER ~~~~~~~~~~        
    def display(self):
        color21.print_blue(f"""
        ~~~~~~~~~~~~~~~~~~~~~
              {self.name}
        ~~~~~~~~~~~~~~~~~~~~~
        """)
        print(f"Balance: {self.bal}")
        print(f"Current Bet: {self.bet_amount}")
        print("\nHand:")
        print("------------------\n\n")
        for card in self.hand:
            if card['suit'] == 'DIAMONDS' or card['suit'] == 'HEARTS':
                color21.print_red_cards(card['value'], card['suit'])
            else:
                color21.print_black_cards(card['value'], card['suit'])

            # card_pic = ascii_magic.from_image_file(f"images/{card['image']}.png", columns = 15)
            # ace = ascii_magic.to_terminal(card_pic)
        print("\n\nHand Value: ", self.hand_v)


#*--> DRAWS CARD ON REQUEST OF "HIT" INPUT ~~~~~~~~~~~
#*--> CHECKS IF ACE IN HAND FOR 1/11 VALUE HANDLING ~~
    def hit(self, card_dictionary):
        self.hand.append(card_dictionary)
        self.hand_v += card_dictionary['points']

        if card_dictionary['value'] == 'ACE':
            self.aces.append('ace')

    def show_draw(self):
        os.system('cls' if os.name == 'nt' else '')
        color21.print_blue(f"\n\n\n  You Drew the {self.hand[-1]['value'].title()} of {self.hand[-1]['suit'].title()}")
        card_pic = ascii_magic.from_image_file(f"images/{self.hand[-1]['image']}.png", columns = 30)
        ascii_magic.to_terminal(card_pic)
        sleep(1.5)

    def blackjack(self):
        if self.hand_v == 21:
            return True
        else:
            return False


#*--> "BUST" ACTIONS WHEN 21 IS EXCEEDED ~~~~~~~~~~~
#*--> VERIFY/ADJUST VALUE OF ACE TO 1 ~~~~~~~~~~~~~~~        
    def bust(self):
        if self.hand_v > 21:
            if self.aces:
                self.hand_v -= 10
                del self.aces[0]
                return False
            else:
                return True
        else:
            return False

#*--> RESETS CARDS FOR NEW GAME PLAY ~~~~~~~~~~~
    def clear_hand(self):
        self.hand_v = 0
        self.hand = []


#*--> Dealer actions during play
#*--> drawing cards "Hit", win/lose/bust displays.
class Dealer():
    def __init__(self):
        self.hand = []
        self.hidden_value = 0
        self.true_value = 0
        self.aces = []

#*--> DRAWS CARD ON REQUEST OF "HIT" INPUT ~~~~~~~~~~~
#*--> CHECKS IF ACE IN HAND FOR 1/11 VALUE HANDLING ~~
    def hit(self, card_dictionary):
        self.hand.append(card_dictionary)
        if len(self.hand) < 2 or len(self.hand) > 2:
            self.hidden_value += card_dictionary['points']
        self.true_value += card_dictionary['points']
        if card_dictionary['value'] == 'ACE':
            self.aces.append('ace')

    def show_draw(self):
        os.system('cls' if os.name == 'nt' else '')
        if len(self.hand) == 2:
            color21.print_red(f"\n\n Dealer Drew an Unknown Card")
            card_pic = ascii_magic.from_image_file(f"images/BACK.PNG", columns = 30)
            ascii_magic.to_terminal(card_pic)
        else:
            color21.print_red(f"\n\n Dealer Drew the {self.hand[-1]['value'].title()} of {self.hand[-1]['suit'].title()}")
            card_pic = ascii_magic.from_image_file(f"images/{self.hand[-1]['image']}.png", columns = 30)
            ascii_magic.to_terminal(card_pic)
        sleep(1.5)

    def dealer_had(self):
        os.system('cls' if os.name == 'nt' else '')
        color21.print_red(f"\n\n Dealer had the {self.hand[1]['value'].title()} of {self.hand[1]['suit'].title()}")
        card_pic = ascii_magic.from_image_file(f"images/{self.hand[1]['image']}.png", columns = 30)
        ascii_magic.to_terminal(card_pic)
        sleep(1.5)
        
#*--> DISPLAYS NAME, CARDS, & STATS OF DEALER ~~~~~~~~~~
    def dealer_display(self):
        color21.print_red(f"""
        ~~~~~~~~~~~~~~~~~~~~~
            Dealer's Hand:
        ~~~~~~~~~~~~~~~~~~~~~
        """)
        for i in range(len(self.hand)):
            if i == 1:
                color21.print_unkown()
            else:
                if self.hand[i]['suit'] == 'DIAMONDS' or self.hand[i]['suit'] == 'HEARTS':
                    color21.print_red_cards(self.hand[i]['value'], self.hand[i]['suit'])
                else:
                    color21.print_black_cards(self.hand[i]['value'], self.hand[i]['suit'])
        print("\n\n")
        print("Shown Hand Value: ", self.hidden_value)

       
#*--> "BUST" ACTIONS WHEN 21 IS EXCEEDED ~~~~~~~~~~~
#*--> VERIFY/ADJUST VALUE OF ACE TO 1 ~~~~~~~~~~~~~~~
    def bust(self):
        if self.true_value > 21:
            if self.aces:
                self.true_value -= 10
                del self.aces[0]
                return False
            else:
                return True
        else:
            return False


#*--> AFTER PLAYER CHOOSES "STAY" DEALER HOLE CARD IS REVEALED ~~
    def true_display(self):
        color21.print_red(f"""
        ~~~~~~~~~~~~~~~~~~~~~
            Dealer's Hand:
        ~~~~~~~~~~~~~~~~~~~~~
        """)
        for card in self.hand:
            if card['suit'] == 'DIAMONDS' or card['suit'] == 'HEARTS':
                color21.print_red_cards(card['value'], card['suit'])
            else:
                color21.print_black_cards(card['value'], card['suit'])
        print("\n\n")
        print("Hand Value: ", self.true_value)

#*--> RESETS CARDS FOR NEW GAME PLAY ~~~~~~~~~~~
    def clear_hand(self):
        self.hidden_value = 0
        self.true_value = 0
        self.hand = []
        
    
#*--> Table actions including card shuffling,  
#*--> holds functions of how/when cards displayed during play.
class Table():
    game_deck = Deck()
    while game_deck.cards_left < 52:
        game_deck.shuffle()

    def __init__(self):
        self.dealer = None
        self.player1 = None
        self.pot = 0

    
    def welcome(self):
        blackjack = ascii_magic.from_image_file(f"images/blackjack.png", columns = 100)
        ascii_magic.to_terminal(blackjack)
        color21.print_green("\t\t\t\tWlesome to J&D's 6 Deck BlackJack")
        color21.input_green("\t\t\t\t     --Press ENTER to Play--")
        os.system('cls' if os.name == 'nt' else '')


#*--> FIRST CARD DISPLAY WITH DEALER HOLE CARD VALUE HIDDEN ~~~~~~~~~
    def display_all_hidden(self):
        os.system('cls' if os.name == 'nt' else '')
        {self.dealer.dealer_display()}
        print('\n\n')
        {self.player1.display()}   
        print('\n')
        sleep(1)

#*--> CARD DISPLAY WITH DEALER HOLE CARD VALUE REVEALED ~~~~~~~~~~~
    def display_all_true(self):
        os.system('cls' if os.name == 'nt' else '')
        {self.dealer.true_display()}
        print('\n\n')
        {self.player1.display()}   
        print('\n')
        sleep(1)


#*--> WELCOME INPUT PROMPT - PLAYER NAME, ~~~ 
#*--> BEGINING BALANCE AMOUNT FOR PLAY  ~~~~~
#*--> BEGINS GAME PLAY LOGIC ~~~~~~~~~~~~~~~~
    def main(self): 
        os.system('cls' if os.name == 'nt' else '')
        game_deck = Deck()

        if game_deck.cards_left < 52:
            game_deck.shuffle()   
        self.welcome()
        the_player = input("\n\nWhats your name player?: ")
        self.dealer = Dealer()
        self.player1 = Player(the_player)

        while True:
            bal = input(f"\n\nHow much will you be playing with {self.player1.name}?: ")
            if not bal.isdigit():
                    color21.print_red("\nInvalid entry please try again.")
                    print()
            else:
                self.player1.bal = int(bal) 
                break

        
        playing = True
        while playing:
            if not self.player1.bet():
                break
            else:
                os.system('cls' if os.name == 'nt' else '')
                print('\n\n\n')
                announce = figlet_format("Initial", font = "alligator2")
                announce2 = figlet_format("           Draw", font = "alligator2")
                print(announce)
                print(announce2)
                sleep(2)
                self.player1.hit(game_deck.get_card())
                self.player1.show_draw()
                # self.display_all_hidden()
                self.dealer.hit(game_deck.get_card())
                self.dealer.show_draw()
                # self.display_all_hidden()
                self.player1.hit(game_deck.get_card())
                self.player1.show_draw()
                self.player1.bust()
                # self.display_all_hidden()
                self.dealer.hit(game_deck.get_card())
                self.dealer.show_draw()
                self.dealer.bust()
                self.display_all_hidden()
            
            player_busts = False
            hitting = True
            while hitting:
                hit = input("Do you want to hit or stay?: ").lower()
                if hit == 'stay':
                    hitting = False
                    self.display_all_hidden()
                else:
                    self.player1.hit(game_deck.get_card())
                    self.player1.show_draw()
                    self.player1.bust()
                    self.display_all_hidden()
                    if self.player1.blackjack():
                        print(figlet_format("BLACKJACK", font="alligator2"))
                        print('\n\n\t\tThe Dealer still has a chance to match')
                        hitting = False
                    elif self.player1.bust():
                        os.system('cls' if os.name == 'nt' else '')
                        color21.print_red(figlet_format("You Busted", font = 'basic'))
                        color21.print_red(figlet_format("           Loser", font = 'basic'))
                        self.player1.lose_hand()
                        hitting = False
                        player_busts = True
                    

            if not player_busts:
                self.dealer.dealer_had()
                self.display_all_true()
                while self.dealer.true_value < 17:
                    self.dealer.hit(game_deck.get_card())
                    self.dealer.show_draw()
                    self.dealer.bust()
                    self.display_all_true()
                
            if self.dealer.bust():
                os.system('cls' if os.name == 'nt' else '')
                color21.print_yellow(figlet_format("Dealer", font = 'alligator2'))
                color21.print_yellow(figlet_format("Busted", font = 'alligator2'))
                color21.print_yellow(figlet_format("You Win", font = 'alligator2'))
                self.player1.win_hand()
            
            elif not player_busts:
                if self.player1.hand_v > self.dealer.true_value:
                    my_hand = figlet_format(f"{self.player1.hand_v} > {self.dealer.true_value}", font = 'univers')
                   
                    color21.print_green(my_hand)
                    print("\t\t\tYou win!")
                    self.player1.win_hand()
                    
                elif self.player1.hand_v == self.dealer.true_value:
                    my_hand = figlet_format(f"{self.player1.hand_v} = {self.dealer.true_value}", font = 'univers')
                    
                    color21.print_blue(my_hand)
                    print("\t\t\tIt's a Draw!")
                    self.player1.draw()
                    
                else:
                    my_hand = figlet_format(f"{self.player1.hand_v} < {self.dealer.true_value}", font = 'univers')
        
                    color21.print_red(my_hand)
                    print("\t\t\tYou lose!")
                    self.player1.lose_hand()
                    

#*-->  WIN OR LOSE THE PLAYER IS GIVEN OPTION TO PLAY AGAIN OR NOT ~~~~~~~~~
            self.dealer.clear_hand()
            self.player1.clear_hand()
            again = input("\n\nWould you like to play again: (Y/N) ").lower()
            os.system('cls' if os.name == 'nt' else '')
            if not again == 'y':
                playing = False


if __name__ == '__main__':
    Table().main()