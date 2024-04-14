def key_is_escape(key):
    try:
        is_escape = ord(key) == 27
    except:
        return False
    return is_escape
