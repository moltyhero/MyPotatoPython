# coding=utf-8
from Deck import Deck
from Player import PlayerDeck


def war(player1_card, player2_card, player1, player2, loot):
    # הוספת הקלפים שהוצאנו כבר אל השלל
    loot.add_card(player1_card)
    loot.add_card(player2_card)

    # הוספת 2 קלפים מכל שחקן אל השלל
    for i in range(2):
        if not player1.is_empty():
            temp_card = player1.pop_card()
            loot.add_card(temp_card)
            player1_card = temp_card

        if not player2.is_empty():
            temp_card = player2.pop_card()
            loot.add_card(temp_card)
            player2_card = temp_card

    return player1_card, player2_card, loot


def main():
    deck = Deck()  # יצירת כל הקלפים הקיימים
    deck.shuffle()

    player1 = PlayerDeck()  # חבילה של השחקן הראשון
    player2 = PlayerDeck()  # חבילה של השחקן השני
    loot = PlayerDeck()     # חבילת השלל

    # חלוקת הקלפים ל- 2 השחקנים
    deck.move_cards(player1, 26)
    deck.move_cards(player2, 26)

    while not player1.is_empty() and not player2.is_empty():
        player1_card = player1.pop_card()
        player2_card = player2.pop_card()

        if player1_card.__cmp__(player2_card) == 0:  # יש מלחמה
            player1_card, player2_card, loot = war(player1_card, player2_card, player1, player2, loot)

        elif player1_card.__cmp__(player2_card) > 0:  # הקלף של השחקן הראשון גדול מהקלף של השחקן השני
            player1.add_card(player2_card)
            loot.move_cards(player1, len(loot.cards))
            player1.shuffle()

        else:  # הקלף של השחקן השני גדול מהקלף של השחקן הראשון
            player2.add_card(player1_card)
            loot.move_cards(player2, len(loot.cards))
            player1.shuffle()

    if player1.is_empty():
        print "Player 2 has won!"
    else:
        print "Player 1 has won!"


if __name__ == '__main__':
    main()
