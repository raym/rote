import curses
from constants import ERROR_TEXT, NOMINAL_TEXT, SUCCESS_TEXT
from curses import wrapper
from lib import calculate_linecount, key_is_backspace, key_is_escape
from lib.cards import load_cards, shuffle_cards
from user_interactions import congratulate_user, test_user, welcome_user

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

