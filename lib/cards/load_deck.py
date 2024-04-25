import os
import yaml

def path_is_yaml_file(path):
    _, extension = os.path.splitext(path)
    return extension in ['.yaml', '.yml']

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

def load_deck(deck_path):
    cards = []
    if os.path.isdir(deck_path):
        for filename in os.listdir(deck_path):
            reldir = os.path.relpath(deck_path)
            relfile = os.path.join(reldir, filename)
            if path_is_yaml_file(relfile):
                cards += load_cards_from_file(relfile)
    elif path_is_yaml_file(deck_path):
        cards += load_cards_from_file(deck_path)
    return cards
