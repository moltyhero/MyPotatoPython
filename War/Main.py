# coding=utf-8
from Deck import Deck
from Player import PlayerDeck


def war(player1_card, player2_card, player1, player2, loot):
    # הוספת הקלפים שהוצאנו כבר אל השלל
    loot.add_card(player1_card)
    loot.add_card(player2_card)

    for i in range(2):  # הוספת 2 קלפים מכל שחקן אל השלל
        loot.add_card(player1.pop_card())
        loot.add_card(player2.pop_card())

    return loot

    # קרב חוזר
    # player1_card = player1.pop_card()
    # player2_card = player2.pop_card()
    # if player1_card.__cmp__(player2_card) == 0:
    #     war(player1_card, player2_card, player1, player2, loot)
    # elif player1_card.__cmp__(player2_card) > 0:  # הקלף של השחקן הראשון גדול מהקלף של השחקן השני
    #     player2.add_card(player1_card)
    #     for i in range(4):
    #         player2.add_card(loot.pop_card())
    # else:  # הקלף של השחקן השני גדול מהקלף של השחקן הראשון
    #     player1.add_card(player2_card)
    #     for i in range(4):
    #         player1.add_card(loot.pop_card())


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
            loot = war(player1_card, player2_card, player1, player2, loot)

        elif player1_card.__cmp__(player2_card) > 0:  # הקלף של השחקן הראשון גדול מהקלף של השחקן השני
            player2.add_card(player1_card)
            while not loot.is_empty():
                player2.add_card(loot.pop_card())
        else:  # הקלף של השחקן השני גדול מהקלף של השחקן הראשון
            player1.add_card(player2_card)
            while not loot.is_empty():
                player1.add_card(loot.pop_card())





if __name__ == '__main__':
    main()
