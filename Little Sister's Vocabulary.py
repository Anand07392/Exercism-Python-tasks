def add_prefix_un(word):
    return 'un'+word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    result = f"{prefix} :: " + " :: ".join(prefixed_words)
    return result


def remove_suffix_ness(word):
    if not word.endswith('ness'):
        return word  
    root = word[:-4]
    if len(root) > 1 and root[-1] == 'i' and root[-2] not in 'aeiou':
        root = root[:-1] + 'y'
    return root


def adjective_to_verb(sentence, index):
    list = sentence.split()
    for word in list:
        if word == list[index]:
            return word.strip(".") + "en"
        else:
            pass
