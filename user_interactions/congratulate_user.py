import curses
from lib import calculate_linecount

def congratulate_user(stdscr, card):
    curses.beep()
    start_congratulations_on_line = calculate_linecount(card['question']) + calculate_linecount(card['answer'])
    stdscr.addstr(start_congratulations_on_line + 2, 0, "Yes!\n\nPress ESC to exit. Press any other key to go to the next card...")
