import Card
import Deck
import Player

# While Game On

player1 = Player.Player("One")
player2 = Player.Player("Two")

new_deck = Deck.Deck()

for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:

    round_num += 1
    print(f'Round {round_num}')

    if len(player1.all_cards) == 0:
        print('Player One, out of cards, Player Two Wins1')
        game_on = False
        break

    if len(player2.all_cards) == 0:
        print('Player Two, out of cards, Player One Wins1')
        game_on = False
        break

    # Start a new round
    player1_cards = []
    player1_cards.append(player1.remove_one())
    player2_cards = []
    player2_cards.append(player2.remove_one())


    at_war = True

    # While at war
    while at_war:

        if player1_cards[-1].value > player2_cards[-1].value:

                # Player One gets the cards
                player1.add_cards(player1_cards)
                player1.add_cards(player2_cards)
                
                at_war = False
            
        # Player Two Has higher Card
        elif player1_cards[-1].value < player2_cards[-1].value:

            # Player Two gets the cards
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            
            at_war = False

        else:
            print('WAR!')
            
            # Check to see if a player is out of cards:
            if len(player1.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player2.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())
