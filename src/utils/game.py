from src.utils.player import Player
from src.utils.deck import Deck
from src.utils.card import Card
from src.utils.clear_console import clear_console

class Game():
    __MINIMUM_NUM_OF_PLAYERS = 3

    def __init__(self, player_names):
        self.__players = []
        self.__players_count = 0
        for name in player_names:
            self.__players.append(Player(name.lower()))
            self.__players_count += 1

        self.__deck = Deck()
        self.__deck.shuffle()

        for _ in range(0,4):
            for player in self.__players:
                player.receive_card(self.__deck.draw_card())

    def get_players(self):
        return self.__players

    def display_players(self, current_player=None):
        result = '('
        for index, player in enumerate(self.__players):
            if player == current_player:
                continue
            if index == len(self.__players) - 1:
                result += f"{player.get_name().title()})"
                break
            result += f"{player.get_name().title()}, "
        print(result)

    def get_players_count(self):
        return self.__players_count

    def get_deck(self):
        return self.__deck

    def next_player(self, current_player):
        for index, player in enumerate(self.__players):
            if player == current_player:
                return self.__players[(index + 1) % len(self.__players)]
        return None

    def player_turn(self, player):
        clear_console()
        print(f"{player.get_name().title()}'s turn (only {player.get_name().title()} should look at the screen)")
        print('---------------------------')
        print('\n')

        print('You can only ask about a rank you have in your hand.')
        print('\n')
        print('You have the following cards:')
        player.print_cards()
        print('\n')

        picked_player = self.__pick_player(player)
        print('---------------------------')
        print('\n')

        picked_rank = self.__pick_rank()
        print('---------------------------')
        print('\n')

        if not picked_player.has_card_rank(picked_rank):
            print(f"{picked_player} doesn't have a card with rank {picked_rank}")
            print('\n')
            draw_card = self.__deck.draw_card()
            player.receive_card(draw_card)
            print(f"You have received {draw_card} from the deck.")
            print('\n')
            print('You have the following cards now:')
            player.print_cards()
            print('\n')
            input('Press enter to end your turn...')
            clear_console()
            next_player = self.next_player(player)
            print(f'Now {next_player} look at the screen.')
            print('\n')
            input('Press enter to start your turn...')
            return



        picked_color = self.__pick_color()
        print('---------------------------')
        print('\n')

        picked_suit = self.__pick_suit()
        print('---------------------------')
        print('\n')

        # TODO


    def __pick_player(self, player):
        self.display_players(player)
        print('\n')
        picked_player = None
        while True:
            picked_player = input('Pick a player to ask: ')
            if picked_player.lower() == player.get_name().lower():
                print("You can't choose yourself.")
                continue
            for player in self.__players:
                if picked_player.lower() in player.get_name().lower():
                    return player
            print("Player does not exist.")

    def __pick_rank(self):
        Card.display_valid_ranks()
        print('\n')
        picked_rank = None
        while True:
            picked_rank = input('Pick a rank: ')
            try:
                picked_rank = picked_rank.upper()
            except AttributeError:
                pass
            if picked_rank in Card.get_valid_ranks():
                break
            print("Please pick a valid rank.")
        return picked_rank

    def __pick_suit(self):
        Card.display_valid_suits()
        print('\n')
        picked_number = None
        while True:
            picked_number = input('Pick a suit (1, 2, 3, 4): ')
            try:
                picked_number = int(picked_number)
            except ValueError:
                print('Please provide a number.')
                continue
            else:
                if picked_number not in [1, 2, 3, 4]:
                    print('Please provide a valid number.')
                    continue
                break
        picked_suit = Card.get_valid_suits()[picked_number-1]
        return picked_suit

    def __pick_color(self):
        Card.display_valid_colors()
        print('\n')
        picked_color = None
        while True:
            picked_color = input('Pick a color: ')
            if picked_color.title() in Card.get_valid_colors():
                break
            print('Please pick a valid color.')
        return picked_color.title()


    @staticmethod
    def get_minimum_num_of_players():
        return Game.__MINIMUM_NUM_OF_PLAYERS

