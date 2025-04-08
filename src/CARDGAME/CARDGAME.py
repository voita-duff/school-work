import random
import logging
from card import Card
from deck import Deck
from player import Player

logging.basicConfig(filename="cards_war.log", level=logging.INFO, format="%(asctime)s - %(message)s") #videl jsem na youtubu 

def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)   ## zkouska dekoratoru
        logging.info(result)
        return result
    return wrapper

@log_action
def log_round_info(info):
    return info

def start_game():
    print("Welcome to Card WAR")
    num_players = int(input("How many players? (2-4): "))
    while num_players < 2 or num_players > 4:
        num_players = int(input("Choose between 2 to 4 players: "))

    names = []

    names = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        names.append(name)

    deck = Deck()
    deck.shuffle()
    players_cards = deck.split_deck_for_players(num_players)

    players = []
    for i in range(num_players):
        players.append(Player(players_cards[i], names[i]))

    log_round_info("game started with players: " + ", ".join(names))

    round_count = 0

    while round_count < 1000:
        active_players = [p for p in players if p.has_cards()]
        if len(active_players) == 1:
            log_round_info(f"{active_players[0].name} wins")
            print(active_players[0].name, "wins ⚠️⚠️")
            break

        round_count += 1
        print("\nROUND", round_count)
        round_cards = []

        for p in active_players:
            card = p.play_card()
            if card:
                print(p.name, "plays", card)
                round_cards.append((p, card))

        if not round_cards:
            break

        highest = max(round_cards, key=lambda x: x[1].value)[1].value
        top_cards = [pair for pair in round_cards if pair[1].value == highest]                     #### KEY LAMBDA s pomoci Chatgpt, absolutne jsem si nevedel rady

        pot = [pair[1] for pair in round_cards]

        if len(top_cards) == 1:
            winner = top_cards[0][0]
            winner.collect_cards(pot)
            log_round_info(f"{winner.name} wins the round.")
            print(winner.name, "wins the round.")
        else:
            print("WAR!")
            log_round_info("War started between: " + ", ".join(p[0].name for p in top_cards))
            war_pot = pot[:]
            new_top_cards = []

            for player, _ in top_cards:
                if player.card_count() < 4:
                    log_round_info(f"{player.name} can't continue war. killed.")
                    players.remove(player)
                    continue
                facedown1 = player.play_card()
                facedown2 = player.play_card()
                facedown3 = player.play_card()
                faceup = player.play_card()
                war_pot.extend([facedown1, facedown2, facedown3, faceup])
                print(player.name, "puts 3 facedown cards and then", faceup)
                new_top_cards.append((player, faceup))

            if new_top_cards:
                highest_war = max(new_top_cards, key=lambda x: x[1].value)[1].value
                final = [x for x in new_top_cards if x[1].value == highest_war]
                if len(final) == 1:
                    winner = final[0][0]
                    winner.collect_cards(war_pot)
                    print(winner.name, "wins the war🪖")
                    log_round_info(f"{winner.name} wins the war.")
                else:
                    print("War draw again. cards removed from game.")
                    log_round_info("War draw again. cards removed.")

    else:
        print("Max rounds reached.")
        log_round_info("Max rounds reached. Game ends in draw or current state.")

if __name__ == "__main__":
    start_game()
