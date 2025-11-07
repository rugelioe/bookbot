def get_num_words(book_text):
	word_list = book_text.split()

	return len(word_list)

def get_chars_dict(book_text):
    character_dict = {}
    for character in book_text:
        lowered = character.lower()
        if lowered in character_dict:
            character_dict[lowered] += 1
        else:
            character_dict[lowered] = 1
    
    return character_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
