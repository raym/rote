import os
import yaml

def load_card(filepath):
    with open(filepath, 'r') as file:
        card = yaml.safe_load(file)
    return {
        'question': card['question'],
        'answer': card['answer'],
    }

def load_deck(deck_dir):
    cards = []
    for dir_, _, files in os.walk(deck_dir):
        for filename in files:
            rel_dir = os.path.relpath(dir_)
            rel_file = os.path.join(rel_dir, filename)
            cards.append(load_card(rel_file))
    return cards
