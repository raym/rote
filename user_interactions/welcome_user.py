def welcome_user(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome! You will now be tested...")
    stdscr.addstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey()
