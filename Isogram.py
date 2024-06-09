def is_isogram(string):
    normalized_word = string.lower().replace(' ', '').replace('-', '')
    seen = set()
    for char in normalized_word:
        if char in seen:
            return False 
        seen.add(char)  
    return True  
