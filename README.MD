# BLACK(21)JACK

Week 3 Weekend project - Dylan K. & Jody S.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip install requirements.txt
```

## Whiteboard (Phase 1)

```python
# PHASE 1
import os       # To clear screen 
import random   # To choose card values and suits
import time     # Perhaps sleep when displaying?

# Dealer cards
d_cards = []                                         # [*--> Additional concerns/needs <--*]  
# Player cards                                           Welcome screen? Logos? Ascii Magic/Colorama? Do we GUI?
p_cards = []                                          #  Address card suits                              
#                                                        Ace = 1 or 11 (if cards < 21 ( Ace is 1 or 11 )
#                                                              if cards > 21 (Ace =1)
# [[Deal & Display cards]]                               BlackJack vs 21 messaging
#  Dealer game Cards
while len(d_cards) != 2:
    d_cards.append(random.randint(1, 11))
    if len(d_cards) == 2:
        print("Dealer has X &", d_cards[1])

# Player game Cards
while len(p_cards) != 2:
    p_cards.append(random.randint(1, 11))
    if len (p_cards) == 2:
        print("You have ", p_cards)

# [[Display & Play cards]]
# Sum of the Dealer cards
if sum(d_cards) == 21:
    print( "Dealer has 21 and wins!")
elif sum(d_cards) > 21:
    print("Dealer has busted!")

# Sum of the Player cards
while sum(p_cards) < 21:
    action_taken = str(input("Do you want to stay or hit?"))
    if action_taken == "hit":
        p_cards.append(random.randint(1, 11))
        print ("You now have a total of " + str(sum(p_cards)) + " from these cards", p_cards) 
    else:
        print("The dealer has a total of " + str(sum(d_cards)) + " with ", d_cards)
        print("You have a total of " + str(sum(p_cards)) + " with ", p_cards)
        if sum (d_cards) > sum (p_cards):
            print("Dealer wins!")
        else:
            print(" You win!")
            break

if sum(p_cards) > 21:
    print("You BUSTED! Dealer wins.")
elif sum(p_cards) == 21:
    print("You have BLACKJACK! You Win!! 21")
```

## Contributing
https://github.com/ElJody/Wk3_BlackJack_JSheff\n

https://github.com/dkatina/BlackJack

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)