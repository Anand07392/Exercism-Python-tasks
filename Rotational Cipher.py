def rotate(text, key):
    def shift_char(c, key):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + key) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + key) % 26 + ord('A'))
        else:
            return c   
    return ''.join(shift_char(c, key) for c in text)
