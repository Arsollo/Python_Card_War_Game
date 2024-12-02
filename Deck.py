suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

import Card
import random

class Deck:
	
	def __init__(self):

		self.all_cards = []
		self.size = 52

		#Create the Deck
		for suit in suits:
			for rank in ranks:
				#Create a card
				new_card = Card.Card(suit, rank)

				self.all_cards.append(new_card)

		#shuffle the Deck
		self.shuffle()


	def shuffle(self):

		random.shuffle(self.all_cards)


	def deal_one(self):
		self.size -= 1
		return self.all_cards.pop()





		
new_deck = Deck()
first = new_deck.all_cards[0]
print(first)