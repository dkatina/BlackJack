from deck import Deck


class Player():
    
    def __init__(self, name):
        self.name = name
        self.bal = 0
        self.hand = []
        self.bet_amount = 0
        self.hand_v = 0

    def get_bal(self):
        return self.bal
    
    def bet(self):
        #Askes player for bet amount:
        #Check to see if player has enough money to bet amount
        #Returns True stores amount & and removes amount from bal
        #Tells player, not enough money and recursivly calls the function=
        pass

    def lose_hand(self):
        #The amount was already taken from bal so the player just doesnt get it back
        #maybe add a print(you lost bet)
        #Set bet amount to 0
        pass

    def draw(self):
        #Player gets back his bet (doesn't win or lose)
        #Set bet amount back to 0
        pass

    def win_hand(self, bet):
        self.bal += (self.bet_amount *2)
        #set bet_amount to 0
        #maybe add a print(you lost bet)

    def display(self):
        print(f"{self.name}")
        print(f"Balance: {self.bal}")
        print(f"Current Bet: {self.bet_amount}")
        print("Hand:")
        for card in self.hand:
            print(card['value'], 'of', card['suit'])
        print("Hand Value: " + self.hand_v)
        

    


    def hit(self, card_dictionary):
        self.hand.append(card_dictionary)
        self.hand_v += card_dictionary['points']
        

    def bust(self, hand_value):
        if self.hand_v > 21:
             return True
        else:
            return False



class Dealer():
    def __init__(self, name):
        self.name = ''
        self.hand = []
        self.hidden_value = 0
        self.true_value = 0



    def hit(self, card_dictionary):
        self.hand.append(card_dictionary)
        if len(self.hand) < 2 or len(self.hand) > 2:
            self.hidden_value += card_dictionary['points']
        self.true_value += card_dictionary['points']
        

    def dealer_display(self):
        print("Dealer's Hand:")
        for i in range(len(self.hand)):
            if i == 2:
                print("Unknown", end='')
            else:
                print(self.hand[i]['value'], 'of', self.hand[i]['suit'])
        print("Shown Hand Value: " + self.hidden_value)

       

    def bust(self):
        if self.true_value > 21:
             return True
        else:
            return False
        


    def true_display(self):
        print("Dealer's Hand:")
        for card in self.hand:
            print(card['value'], 'of', card['suit'])
        print("Hand Value: " + self.true_value)
        
       


class Table():
    game_deck = Deck()

    while game_deck.cards_left < 52:
        game_deck.shuffle()

    def __init__(self):
        self.dealer = None
        self.player1 = None
    
    def welcome(self):
        pass

    def display_all_hidden(self):
        pass
        #While it's not the dealers turn call this to show the table 
        #With the dealers second card facedown and their card value not showing the second cards value

    def display_all_true(self):
        pass
        #While it is the dealers turn call this to show table
        #Shows the dealers second card after its "flipped over" and show his hands_true_value


    def main(self): 
        game_deck = Deck()

        while game_deck.cards_left < 52:
            game_deck.shuffle()   
        #Welcome
        #whose the_dealer
        #whose the_player
        #Define self.dealer = Dealer(the_dealer)
        #Define self.player1 = Player(the_player)

        # bal = How much are you playing with
        # self.player1.bal = bal 

        #Playing a hand (This will be a while loop)
            #Call the bet function
            #Initial Draw
                #player1 gets a card
                #display card
                #Dealer gets a card
                #Dealer_display will show this card
                #player1 gets a card
                #display both card
                #Dealer gets a card
                #Dealer_display will not show the second card

            #Probably set up a while loop that will stop when player stays or busts
                #Player asked to hit or stay
                #If stay: loop breaks
                #If hit call hit function
                #Display
                #See if player busted
                # If busted break loop
                # Else loop continues

            #If player Busted end hand else

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
        pass