import os
import yaml

def load_cards_from_file(filepath):
    with open(filepath, 'r') as file:
        card_list = yaml.safe_load(file)
    return [
        {
            'question': card['front'],
            'answer': card['back'],
        }
        for card in card_list
    ]

def load_deck(deck_dir):
    cards = []
    for filename in os.listdir(deck_dir):
        rel_dir = os.path.relpath(deck_dir)
        rel_file = os.path.join(rel_dir, filename)
        cards += load_cards_from_file(rel_file)
    return cards
