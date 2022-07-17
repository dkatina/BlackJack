from copyreg import dispatch_table
from deck import Deck

#If Hand > 21 and ace in hand ace = 1




class Player():
    
    def __init__(self, name):
        self.name = name
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
                bet = int(input(f'You have ${self.bal}. How much would you like to bet? '))
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

    def lose_hand(self):
        print(f'You lost $', self.bet_amount)
        self.bet_amount = 0
        
    def draw(self):
        self.bal += (self.bet_amount)
        self.bet_amount = 0

    def win_hand(self):
        self.bal += (self.bet_amount *2)
        

    def display(self):
        print(f"{self.name}")
        print(f"Balance: {self.bal}")
        print(f"Current Bet: {self.bet_amount}")
        print("Hand:")
        for card in self.hand:
            print(card['value'], 'of', card['suit'])
        print("Hand Value: ", self.hand_v)

    def hit(self, card_dictionary):
        self.hand.append(card_dictionary)
        self.hand_v += card_dictionary['points']
        if card_dictionary['value'] == 'ACE':
            self.aces.append('ace')
            
        


        
        
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

    def clear_hand(self):
        self.hand_v = 0
        self.hand = []



class Dealer():
    def __init__(self, name):
        self.name = ''
        self.hand = []
        self.hidden_value = 0
        self.true_value = 0
        self.aces = []



    def hit(self, card_dictionary):
        self.hand.append(card_dictionary)
        if len(self.hand) < 2 or len(self.hand) > 2:
            self.hidden_value += card_dictionary['points']
        self.true_value += card_dictionary['points']
        self.aces.append(card_dictionary['value'])
        

    def dealer_display(self):
        print("Dealer's Hand:")
        for i in range(len(self.hand)):
            if i == 1:
                print("Unknown")
            else:
                print(self.hand[i]['value'], 'of', self.hand[i]['suit'])
        print("Shown Hand Value: ", self.hidden_value)

       

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

        


    def true_display(self):
        print("Dealer's Hand:")
        for card in self.hand:
            print(card['value'], 'of', card['suit'])
        print("Hand Value: ", self.true_value)

    def clear_hand(self):
        self.hidden_value = 0
        self.true_value = 0
        self.hand = []
        
       


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

    def display_all_hidden(self):
        {self.dealer.dealer_display()}
        print('\n\n')
        {self.player1.display()}   
        print('\n')

    def display_all_true(self):
        {self.dealer.true_display()}
        print('\n\n')
        {self.player1.display()}   
        print('\n')



    def main(self): 
        game_deck = Deck()

        if game_deck.cards_left < 52:
            game_deck.shuffle()   
        #Welcome
        the_dealer = input("Who will be the dealer?: ")
        the_player = input("Who will be player1?: ")
        self.dealer = Dealer(the_dealer)
        self.player1 = Player(the_player)

        bal = int(input("How much will you be playing with?: "))
        self.player1.bal = bal 

        
        playing = True
        while playing:
            if not self.player1.bet():
                break
            else:
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
                    self.display_all_true()
                
            if self.dealer.bust():
                print("You win!")
                self.player1.win_hand()
            
            else:
                if self.player1.hand_v > self.dealer.true_value:
                    print("You win!")
                    self.player1.win_hand()
                    
                elif self.player1.hand_v == self.dealer.true_value:
                    print("It's a Draw!")
                    self.player1.draw()
                    
                else:
                    print("You lose!")
                    self.player1.lose_hand()
                    

            self.dealer.clear_hand()
            self.player1.clear_hand()

            again = input("Would you like to play again: (Y/N) ").lower()
            if not again == 'y':
                playing = False


                

          
                

            #Else Dealer's turn
                #Dealer displays all cards
                #Set up another while loop
                #While dealers_true_hand_value is =< 17
                    #Dealer_hits
                    #Display_all

                #Evaluate if dealer busted
                    # If dealer busted Player wins
                
                #Else:
                    #If player hand value > Dealer hand value:
                        #Player wins
                    #Elif player hand value == dealer hand value:
                        #Draw, player gets bet back
                    #Else:
                        #PLayer loses

            #Player will be asked to play again
            #If yes loop continues
            #Else:
                #Show player how much they won or lost
                #Break loop
   



if __name__ == '__main__':
    Table().main()