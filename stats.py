def count_words(book_text):
    word_list = book_text.split( )
    return len(word_list)

def count_characters(book_text):
    data_text = book_text.lower()
    letter_dictionary = {}
    for char in data_text:
        if char in letter_dictionary:
            letter_dictionary[char] += 1
        else:
            letter_dictionary[char] = 1
    return letter_dictionary

def characters_list(letter_dictionary):
        dict_list = []
        for c, n in letter_dictionary.items():
             if c.isalpha():
                new_dict = {"char": c, "num": n}
                dict_list.append(new_dict)
        return dict_list

def sort_on(items):
    return items["num"]