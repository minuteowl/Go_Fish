import random

#Build Deck Components
card_keys = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
card_values = list(range(1,14))
card_rank = dict(zip(card_keys, card_values))
print (card_rank)
card_suits = ['Hearts', 'Diamonds', 'Spades', 'Clovers']

#Define classes
class Card:
    def __init__(self, rank, val, suit):
        self.suit = suit    #suit is string object
        self.rank = rank    #self.rank holds the key (eg. Ace) from dictionary as a string
        self.val = val  #val holds numerical value of key as integers
    def show(self):
        print("{rank}({val}) of {suit}".format(rank = self.rank, val = self.val, suit = self.suit))
    def __repr__(self):
        return "{rank} of {suit}".format(rank = self.rank, suit = self.suit)
        
class StockDeck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for suit in card_suits:
            for key in card_rank.keys():
                self.cards.append(Card(key, card_rank[key], suit))
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
        self.is_participant = is_participant
        self.hand = []
        self.pairs_waiting = []
        self.bank = []

        participants.append(self)
        
    def __repr__(self):
        return self.name
    
    def draw_card(self, deck):
        self.hand.append(deck.deal_card())
        
    def show_hand(self):
        for card in self.hand:
            card.show()
            
    #find duplicate ranks in own hand
    def check_pairs(self):
        sorted_hand = sorted(self.hand, key=lambda card: card.val)
        print(sorted_hand)
        if len(self.hand) >= 2:
            #check current card and next card
            try:
                for i in range(len(sorted_hand)-1):
                    if sorted_hand[i].val == sorted_hand[i+1].val:
                        print("Match Found!")
                        print(self.hand.index(sorted_hand[i+1]))
                        this_card = (self.hand.pop(self.hand.index(sorted_hand[i])))
                        next_card = (self.hand.pop(self.hand.index(sorted_hand[i+1])))
                        self.pairs_waiting.append([this_card,next_card])
            #in case there's no more indices to check (hand is empty or has just 1 card)
            except IndexError:
                print("No more pairs can be made!")
        print(self.pairs_waiting)
                    

    #find a match in someone else's hand
    def check_match(self, other, card_rank):
        for card in other.hand:
            if card.rank == card_rank:
                print("{name} has a {rank}!".format(name = other.name, rank = card_rank))
                return True
        else:
            print("{name} doesn't have a {rank}. Go Fish!".format(name = other.name, rank = card_rank))
            return False
        
    #Implement method to find particular card in a hand (based on rank) and move (remove/append) it to different list 
    def get_card(self, other, card):
        pass



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
ithu.check_pairs()
