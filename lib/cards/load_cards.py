import yaml

def load_card():
    with open("cards/01.yaml", "r") as file:
        card = yaml.safe_load(file)
    return (card["question"], card["answer"])


def load_cards():
    (question, answer) = load_card()
    cards = [
        {
            'question': question,
            'answer': answer
        },
    ]
    return cards
