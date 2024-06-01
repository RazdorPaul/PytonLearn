def caesarCrypt(str_buff, key, direct):
    key = int(key)
    en_dir = key % 26
    ru_dir = key % 32
    if direct == 1:
        en_dir *= -1
        ru_dir *= -1
    result = ''
    for i in range(len(str_buff)):
        letter = ord(str_buff[i])
        if letter >= ord('A') and letter <= ord('Z'):
            letter = enUpper(letter, en_dir)
        if letter >= ord('a') and letter <= ord('z'):
            letter = enLower(letter, en_dir)
        if letter >= ord('А') and letter <= ord('Я'):
            letter = ruUpper(letter, ru_dir)
        if letter >= ord('а') and letter <= ord('я'):
            letter = ruLower(letter, ru_dir)
        result += chr(letter)
    return result

def enUpper(buff, key):
    buff += key
    if buff < ord('A'):
        buff = ord('A') - buff
        buff = ord('Z') - buff + 1
    if buff > ord('Z'):
        buff -= ord('Z')
        buff += ord('A') - 1
    return buff

def enLower(buff, key):
    buff += key
    if buff < ord('a'):
        buff = ord('a') - buff
        buff = ord('z') - buff + 1
    if buff > ord('z'):
        buff -= ord('z')
        buff += ord('a') - 1
    return buff

def ruUpper(buff, key):
    buff += key
    if buff < ord('А'):
        buff = ord('А') - buff
        buff = ord('Я') - buff + 1
    if buff > ord('Я'):
        buff -= ord('Я')
        buff += ord('А') - 1
    return buff

def ruLower(buff, key):
    buff += key
    if buff < ord('а'):
        buff = ord('а') - buff
        buff = ord('я') - buff + 1
    if buff > ord('я'):
        buff -= ord('я')
        buff += ord('а') - 1
    return buff