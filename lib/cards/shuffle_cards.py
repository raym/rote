import random

def shuffle_cards(cards):
    shuffled_cards = random.sample(cards, len(cards))
    return shuffled_cards
