def get_count(text):
    num_words = len(text.split())
    return num_words

def get_characters(book):
    char_dictionary = {}
    for character in book:
        character = character.lower()
        if character in char_dictionary:
            char_dictionary[character] += 1
        else:
            char_dictionary[character] = 1
    return char_dictionary

def sort_on(char_dict):
    return char_dict["count"]

def sorted_character_count(char_dict):
    def sort_on(dict_item):
        return dict_item["count"]
    chars_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
            
    