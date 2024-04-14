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
    for filename in os.listdir(deck_dir):
        rel_dir = os.path.relpath(deck_dir)
        rel_file = os.path.join(rel_dir, filename)
        cards.append(load_card(rel_file))
    return cards
