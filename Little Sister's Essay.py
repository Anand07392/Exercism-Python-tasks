def capitalize_title(title):
    str(title)
    return title.title()


def check_sentence_ending(sentence):
    str(sentence)
    if sentence.endswith('.'):
        return True
    else:
        return False
        
def clean_up_spacing(sentence):
    str(sentence)
    return sentence.strip()

def replace_word_choice(sentence, old_word, new_word):
    str(sentence)
    str(old_word)
    str(new_word)
    return sentence.replace(old_word,new_word)
