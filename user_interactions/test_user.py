import curses
from constants import ERROR_TEXT, SUCCESS_TEXT
from lib import calculate_linecount, key_is_escape, key_is_backspace

def render_screen(stdscr, question, answer, guess):
    stdscr.clear()
    stdscr.addstr(question)
    start_answer_on_line = calculate_linecount(question) + 1
    line_num = 0
    col_num = 0
    for i, char in enumerate(guess):
        correct_char = answer[i] if i < len(answer) else None
        color = curses.color_pair(SUCCESS_TEXT) if char == correct_char else curses.color_pair(ERROR_TEXT)
        char_to_print = '↵\n' if char == '\n' else char
        stdscr.addstr(start_answer_on_line + line_num, col_num, char_to_print, color)
        if char == '\n':
            line_num += 1
            col_num = 0
        else:
            col_num += 1
    stdscr.refresh()

def test_user(stdscr, card):
    question = card['question']
    answer = card['answer']
    guess = ''

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
        elif len(guess + key) <= len(answer):
            guess += key
        if guess == answer:
            render_screen(stdscr, question, answer, guess)
            break
