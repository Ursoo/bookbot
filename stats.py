def read_book_contents(book_path):
    with open(book_path) as f:
        content = f.read()
    return content


def count_words(string: str):
    return len(string.split())

def count_character_occurence(string: str):
    char_occurence = {}
    for character in string:
        if character.lower() in char_occurence:
            char_occurence[character.lower()] += 1
        else:
            char_occurence[character.lower()] = 1
    
    return char_occurence

def sorting_method(word_dict):
    return list(word_dict.values())[0]

def dict_to_sorted_list(word_dict):
    words_list = [{key: value} for key, value in word_dict.items()]
    words_list.sort(reverse=True, key=sorting_method)
    return words_list

def print_report(word_count, char_count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = dict_to_sorted_list(char_count)
    for element in char_count:
        element_key = list(element.keys())[0]
        if element_key.isalpha():
            print(f" {element_key}: {element[element_key]}")
    print("--- End report ---")