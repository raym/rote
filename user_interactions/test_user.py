import curses
from constants import ERROR_TEXT, SUCCESS_TEXT
from lib import calculate_linecount, key_is_escape, key_is_backspace

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
    while True:
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
        if guess == answer:
            render_screen(stdscr, question, answer, guess)
            break
    stdscr.timeout(-1)
