def transform(legacy_data):
    new_mapping = {}   
    for score, letters in legacy_data.items():
        for letter in letters:
            new_mapping[letter.lower()] = score 
    return new_mapping
