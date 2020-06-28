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

    #Randomize card order using Fisher Yates shuffle         
    def shuffle_deck(self):
        #move backwards through a list. For every card at index...
        for i in range(len(self.cards)-1, 0, -1):
            #choose a random card from the remaining cards
            r = random.randint(0,i)
            #swap the position of the random card and card at current index.
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

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

    def give_card(self, other, card):
        other.hand.append(hand.pop(index(card)))
        


#initialize players
participants = []
ithu = Player('Ithu')
tahsina = Player('Tahsina')
biva = Player('Biva')
rhydi = Player('Rhydi')
print('Participants:', participants)

#initilize deck, shuffle.
deck = StockDeck()
deck.shuffle_deck()
#deck.show()

#determine order of play using highest to lowest number
max_rank = ""
player_max_rank = ""
for player in participants:
    player.draw_card(deck)
    print player.show_hand()
    
