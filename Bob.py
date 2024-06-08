def response(message):
    if not message.strip():
        return "Fine. Be that way!"
    if message.isupper():
        if message.endswith('?'):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    if message.strip().endswith('?'):
        return "Sure."
    return "Whatever."
