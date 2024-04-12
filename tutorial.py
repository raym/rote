import curses
from curses import wrapper
import random
import yaml

NOMINAL_TEXT = 1
SUCCESS_TEXT = 2
ERROR_TEXT = 3

# lib

def calculate_linecount(question):
    return len(question.splitlines())

def key_is_escape(key):
    return ord(key) == 27

def key_is_backspace(key):
    return key in ('KEY_BACKSPACE', '\b', '\x7f')

def welcome_user(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome! You will now be tested...")
    stdscr.addstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def render_screen(stdscr, question, answer, guess):
    stdscr.clear()
    stdscr.addstr(question)
    start_answer_on_line = calculate_linecount(question) + 1
    for i, char in enumerate(guess):
        correct_char = answer[i]
        color = curses.color_pair(SUCCESS_TEXT) if char == correct_char else curses.color_pair(ERROR_TEXT)
        stdscr.addstr(start_answer_on_line, i, char, color)
    stdscr.refresh()

def test_user(stdscr, card):
    question = card['question']
    answer = card['answer']
    guess = ''

    stdscr.timeout(100)
    while guess != answer:
        render_screen(stdscr, question, answer, guess)
        try:
            key = stdscr.getkey()
        except:
            continue
        if key_is_escape(key):
            break
        if key_is_backspace(key):
            guess = guess[:-1]
        else:
            guess += key
    stdscr.timeout(-1)

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

def shuffle_cards(cards):
    shuffled_cards = random.sample(cards, len(cards))
    return shuffled_cards

def congratulate_user(stdscr, card):
    curses.beep()
    start_congratulations_on_line = calculate_linecount(card['question']) + calculate_linecount(card['answer'])
    stdscr.addstr(start_congratulations_on_line + 2, 0, "Yes!\n\nPress ESC to exit. Press any other key to go to the next card...")

def main(stdscr):
    curses.init_pair(NOMINAL_TEXT, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(SUCCESS_TEXT, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(ERROR_TEXT, curses.COLOR_RED, curses.COLOR_BLACK)

    cards = load_cards()
    shuffled_cards = shuffle_cards(cards)

    welcome_user(stdscr)

    for card in shuffled_cards:
        test_user(stdscr, card)
        congratulate_user(stdscr, card)
        try:
            key = stdscr.getkey()
        except:
            continue
        if key_is_escape(key):
            break

wrapper(main)

