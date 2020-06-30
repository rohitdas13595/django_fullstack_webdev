from random import shuffle


RANKS='2 3 4 5 6 7 8 9 J Q K A'.split()
SUITE='H D S C'.split()


"""mycards = []
for r in RANKS:
    for s in SUITE:
        mycards.append((s,r))"""


class Deck:

    def __init__(self):
        print("Creating a new ordered deck")
        self.allcards =[(s,r)for s in SUITE for r in RANKS]
        """for r in RANKS:
            for s in SUITE:
                allcards.append((s,r))"""

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)
    def spil_in_half(self):
        return(self.allcards[:26],self.allcards[26:])


class Hand:
    def __init__(self,cards):
        self.cards= cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_cards(self):
        return self.cards.pop()


class Player:

    def __init__(self,name,hand):
        self.name= name
        self.hand =hand

    def play_card(self):
        drawn_card =self.hand.remove_cards()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) !=0







print("Welcome to War, Let's begin...")
d =Deck()
d.shuffle()
half1,half2= d.spil_in_half()

#create both players
comp =Player("computer",Hand(half1))

name = input("what is your name?")
user =Player(name,Hand(half2))


total_rounds=0;
war_count=0;

while(user.still_has_cards() and comp.still_has_cards()):
    total_rounds += 1
    print("time for a new round!")
    print("Here are the current standings")
    print(user.name+"has the count: "+str(len(user.hand.cards)))
    print(comp.name+"has the count :"+str(len(comp.hand.cards)))
    print("play a card!")
    print('\n')

    table_cards =[]
    c_card=comp.play_card()
    p_card=user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if(c_card[1] == p_card[1]):
        war_count += 1

        print("war!")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)


print("game over, number of rounds :"+str(total_rounds))
print("a war happens "+str(war_count)+" times")
print("Does the computer still has cards?")
print(str(comp.still_has_cards()))
print("Does the human player still has cards? ")
print(str(user.still_has_cards()))
