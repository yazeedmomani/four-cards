from src.utils.card import Card

class Player():
    def __init__(self, name):
        self.__name = name
        self.__cards = []

    def get_name(self):
        return self.__name

    def get_cards(self):
        return self.__cards

    def receive_card(self, card):
        Card.validate_card(card)
        self.__cards.append(card)

    def drop_card(self, card):
        Card.validate_card(card)
        for index, current in enumerate(self.__cards):
            if current.equals(card):
                del self.__cards[index]
                return
        print(f"Error: Card not found in player {self.__name}'s hand")

    def has_card(self, card):
        Card.validate_card(card)
        for current in self.__cards:
            if current.equals(card):
                return True
        return False

    def has_card_rank(self, rank):
        Card.validate_rank(rank)
        for current in self.__cards:
            if current.rank_equals(rank):
                return True
        return False

    def has_card_suit(self, suit):
        Card.validate_suit(suit)
        for current in self.__cards:
            if current.suit_equals(suit):
                return True
        return False

    def has_card_color(self, color):
        Card.validate_color(color)
        for current in self.__cards:
            if current.color_equals(color):
                return True
        return False

    def __str__(self):
        return f"{self.__name}"