def get_num_words(textblock):
    word_list = textblock.split()
    word_count = len(word_list)
    return word_count

def get_num_char(textblock):
    you_dict = {}
    char = textblock.lower()
    for i in range(128):
        thing = chr(i)
        thing2 = thing + "_count"
        thing2 = char.count(thing)
        you_dict[thing] = thing2
    return you_dict



