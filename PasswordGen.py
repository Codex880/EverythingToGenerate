def create_key(key_len):
    key = ''
    valid_characters_list = string.letters + string.digits
    for i in range(key_len):
        character = choice(valid_characters_list)
        key = key + character
    return key

def create_key_list(key_num):
    keys = []
    for i in range(key_num):
        key = create_key(key_len)
        if key not in keys:
            keys.append(key)
    return keys
