from operator import truediv


class Card():
    __VALID_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    __VALID_SUITS = ['♠', '♥', '♦', '♣']
    __VALID_COLORS = ['Red', 'Black']

    def __init__(self, rank, suit):
        if rank not in Card.__VALID_RANKS:
            raise ValueError(f'Invalid rank: {rank}')
        if suit not in Card.__VALID_SUITS:
            raise ValueError(f'Invalid suit: {suit}')

        self.__rank = rank
        self.__suit = suit
        if self.__suit in ['♥', '♦']:
            self.__color = 'Red'
        else:
            self.__color = 'Black'

    def get_rank(self):
        return self.__rank

    def get_suit(self):
        return self.__suit

    def get_color(self):
        return self.__color

    def equals(self, card):
        if self.rank_equals(card) and self.suit_equals(card) and self.color_equals(card):
            return True
        return False

    def rank_equals(self, rank):
        Card.validate_rank(rank)
        if self.__rank == rank:
            return True
        return False

    def suit_equals(self, suit):
        Card.validate_suit(suit)
        if self.__suit == suit:
            return True
        return False

    def color_equals(self, color):
        Card.validate_color(color)
        if self.__color == color:
            return True
        return False

    def __str__(self):
        return f"Card({self.__rank}, {self.__suit})"

    @staticmethod
    def validate_card(card):
        if not isinstance(card, Card):
            raise TypeError(f"Expected a card, got {type(card).__name__}")

    @staticmethod
    def validate_rank(rank):
        if rank not in Card.__VALID_RANKS:
            raise ValueError(f"Invalid rank: {rank}")

    @staticmethod
    def validate_suit(suit):
        if suit not in Card.__VALID_SUITS:
            raise ValueError(f"Invalid suit: {suit}")

    @staticmethod
    def validate_color(color):
        if color not in Card.__VALID_COLORS:
            raise ValueError(f"Invalid color: {color}")

    @staticmethod
    def get_valid_ranks():
        return Card.__VALID_RANKS

    @staticmethod
    def display_valid_ranks():
        result = "("
        for index, rank in enumerate(Card.__VALID_RANKS):
            if index == len(Card.__VALID_RANKS) - 1:
                result += f"{rank})"
                break
            result += f"{rank}, "
        print(result)

    @staticmethod
    def get_valid_suits():
        return Card.__VALID_SUITS

    @staticmethod
    def display_valid_suits():
        for index, suit in enumerate(Card.__VALID_SUITS):
            print(f"{index+1}: {suit}")

    @staticmethod
    def get_valid_colors():
        return Card.__VALID_COLORS

    @staticmethod
    def display_valid_colors():
        result = "("
        for index, color in enumerate(Card.__VALID_COLORS):
            if index == len(Card.__VALID_COLORS) - 1:
                result += f"{color})"
                break
            result += f"{color}, "
        print(result)
