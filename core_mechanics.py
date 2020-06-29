import random

#Build Deck Components
card_rank = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12, 'King':13}
card_suits = ['Hearts', 'Diamonds', 'Spades', 'Clovers']

#Define classes
class Card:
    def __init__(self, rank, suit):
        self.suit = suit    #suit is string object
        self.rank = rank    #rank holds the key as a string
    def show(self):
        print("{rank} of {suit}".format(rank = self.rank, suit = self.suit))
    def __repr__(self):
        return "{rank} of {suit}".format(rank = self.rank, suit = self.suit)
        
class StockDeck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for suit in card_suits:
            for key in card_rank.keys():
                self.cards.append(Card(key,suit))
    def show(self):
        for card in self.cards:
            card.show()

    #Randomize card order using random seed for now, implement Fisher Yates shuffle after functionality set        
    def shuffle_deck(self):
        random.seed(0)
        random.shuffle(self.cards)
        #move backwards through a list. For every card at index...
        #for i in range(len(self.cards)-1, 0, -1):
            #choose a random card from the remaining cards
            #r = random.randint(0,i)
            #swap the position of the random card and card at current index.
            #self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, is_participant = True):
        self.name = name
        self.hand = []
        self.is_participant = is_participant
        participants.append(self)
        
    def __repr__(self):
        return self.name
    
    def draw_card(self, deck):
        self.hand.append(deck.deal_card())
        
    def show_hand(self):
        for card in self.hand:
            card.show()

    def check_match(self, other, card_rank):
        for card in other.hand:
            if card.rank == card_rank:
                print("{name} has a {rank}!".format(name = other.name, rank = card_rank))
                return True
        else:
            print("{name} doesn't have a {rank}. Go Fish!".format(name = other.name, rank = card_rank))
            return False

    def check_pairs(self):
        pass
            
            

    def give_card(self, other, rank):
        other.hand.append(hand.pop(index(rank)))



#initialize players
participants = []
ithu = Player('Ithu')
tahsina = Player('Tahsina')
biva = Player('Biva')
rhydi = Player('Rhydi')
#print('Participants:', participants)

#randomize participant order.
random.seed(0)
random.shuffle(participants)
print('Play Order: ',participants)

#initilize deck, shuffle and deal cards to participants.
deck = StockDeck()
deck.shuffle_deck()
#deck.show()

for person in participants:
    for i in range(5):
        person.draw_card(deck)
    print("\n\n{person} has these cards:".format(person = person.name))
    person.show_hand()


#Test functionality of check_match()
ithu.check_match(rhydi,'7')
