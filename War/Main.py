import Deck
import Hand


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print find_defining_class(hand, 'shuffle')

    deck.move_cards(hand, 5)
    hand.sort()
    print hand
