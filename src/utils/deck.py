from src.utils.card import Card
from random import shuffle

class Deck():
    __FULL_SIZE = 52

    def __init__(self):
        self.__cards = []

        for suit in Card.get_valid_suits():
            for rank in Card.get_valid_ranks():
                self.__cards.append(Card(rank, suit))

        self.__size = len(self.__cards)
        self.__is_empty = False

    def get_size(self):
        return self.__size

    def get_cards(self):
        return self.__cards

    def is_empty(self):
        return self.__is_empty

    def shuffle(self):
        if self.__size == 0:
            raise ValueError('Cannot shuffle an empty deck')

        shuffle(self.__cards)

    def draw_card(self):
        if self.__size == 0:
            raise ValueError('Cannot draw from an empty deck')

        card = self.__cards[0]
        del self.__cards[0]

        self.__size -= 1
        if self.__size == 0:
            self.__is_empty = True

        return card

    @staticmethod
    def get_full_size():
        return Deck.__FULL_SIZE