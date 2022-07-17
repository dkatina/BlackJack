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
from pyfiglet import Figlet
#*--> Python package that converts images into ASCII art for terminals
import ascii_magic
#*--> OS for clear screen functions across platforms
import os


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
                bet = int(input(f'{self.name} you have ${self.bal}. How much would you like to bet? '))
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
        print(f'You lost $', self.bet_amount)
        self.bet_amount = 0

#*--> ADJUSTS PLAYERS BALANCE DUE TO TIE HAND ~~~~~~~~~~         
    def draw(self):
        self.bal += (self.bet_amount)
        self.bet_amount = 0

#*--> ADJUSTS PLAYER BALANCE = PLAYER WAGER+DEALER WAGER ~~~~~~~~~~
    def win_hand(self):
        self.bal += (self.bet_amount *2)
        
#*--> DISPLAYS NAME, CARDS, & STATS OF PLAYER ~~~~~~~~~~        
    def display(self):
        print(f"""
        ~~~~~~~~~~~~~~~~~~~~~
              {self.name}
        ~~~~~~~~~~~~~~~~~~~~~
        """)
        print(f"Balance: {self.bal}")
        print(f"Current Bet: {self.bet_amount}")
        print("\nHand:")
        print("------------------")
        for card in self.hand:
            # print(card['value'], 'of', card['suit'])
            
            card_pic = ascii_magic.from_image_file(f"images/{card['image']}.png", columns = 10)
            ace = ascii_magic.to_terminal(card_pic)

        print("\nHand Value: ", self.hand_v)


#*--> DRAWS CARD ON REQUEST OF "HIT" INPUT ~~~~~~~~~~~
#*--> CHECKS IF ACE IN HAND FOR 1/11 VALUE HANDLING ~~
    def hit(self, card_dictionary):
        self.hand.append(card_dictionary)
        self.hand_v += card_dictionary['points']

        if card_dictionary['value'] == 'ACE':
            self.aces.append('ace')

        
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
        
#*--> DISPLAYS NAME, CARDS, & STATS OF DEALER ~~~~~~~~~~
    def dealer_display(self):
        print(f"""
        ~~~~~~~~~~~~~~~~~~~~~
            Dealer's Hand:
        ~~~~~~~~~~~~~~~~~~~~~
        """)
        for i in range(len(self.hand)):
            if i == 1:
                print("Unknown")
            else:
                print(self.hand[i]['value'], 'of', self.hand[i]['suit'])
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
        print(f"""
        ~~~~~~~~~~~~~~~~~~~~~
            Dealer's Hand:
        ~~~~~~~~~~~~~~~~~~~~~
        """)
        for card in self.hand:
            print(card['value'], 'of', card['suit'])
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
        pass

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
        #Welcome
        the_player = input("Whats your name player?: ")
        self.dealer = Dealer()
        self.player1 = Player(the_player)

        bal = int(input(f"How much will you be playing with {self.player1.name}?: "))
        self.player1.bal = bal 

        
        playing = True
        while playing:
            if not self.player1.bet():
                break
            else:
                print("Initial draw!")
                sleep(2)
                self.player1.hit(game_deck.get_card())
                self.display_all_hidden()
                self.dealer.hit(game_deck.get_card())
                self.display_all_hidden()
                self.player1.hit(game_deck.get_card())
                self.player1.bust()
                self.display_all_hidden()
                self.dealer.hit(game_deck.get_card())
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
                    self.player1.bust()
                    self.display_all_hidden()
                    if self.player1.bust():
                        print("BUST!")
                        print("You Lose......bitch")
                        self.player1.lose_hand()
                        hitting = False
                        player_busts = True
                    

            if not player_busts:
                self.display_all_true()
                while self.dealer.true_value < 17:
                    self.dealer.hit(game_deck.get_card())
                    self.dealer.bust()
                    self.display_all_true()
                
            if self.dealer.bust():
                print("Dealer Busted!\n You Win!")
                self.player1.win_hand()
            
            elif not player_busts:
                if self.player1.hand_v > self.dealer.true_value:
                    print("You win!")
                    self.player1.win_hand()
                    
                elif self.player1.hand_v == self.dealer.true_value:
                    print("It's a Draw!")
                    self.player1.draw()
                    
                else:
                    print("You lose!")
                    self.player1.lose_hand()
                    

#*-->  WIN OR LOSE THE PLAYER IS GIVEN OPTION TO PLAY AGAIN OR NOT ~~~~~~~~~
            self.dealer.clear_hand()
            self.player1.clear_hand()
            again = input("Would you like to play again: (Y/N) ").lower()
            os.system('cls' if os.name == 'nt' else '')
            if not again == 'y':
                playing = False


if __name__ == '__main__':
    Table().main()