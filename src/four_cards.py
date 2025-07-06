from src.utils.game import Game
from src.utils.clear_console import clear_console

class FourCards():
    @staticmethod
    def run():
        four_cards = Game(FourCards.__input_players())
        for player in four_cards.get_players():
            four_cards.player_turn(player)

        # TODO

    @staticmethod
    def __input_players():
        players = []
        player_count = 0
        print('Four Cards')
        print('---------------------------')
        while True:
            name = input('\nEnter player name (or "Start" to begin): ')
            if name.lower() == 'start':
                if player_count < Game.get_minimum_num_of_players():
                    print(f"\nMinimum number of players is 3. Please add {Game.get_minimum_num_of_players() - player_count} more player/s.")
                    continue
                else:
                    clear_console()
                    break
            if name in players:
                print(f"The name {name} already exists. Please choose a unique name.")
                continue
            players.append(name)
            player_count += 1
        return players