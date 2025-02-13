
def main():
    path = "./books/frankenstein.txt"
    book_content = read_book_contents(book_path=path)
    word_count = count_words(string=book_content)
    char_count_dict = count_character_occurence(string=book_content)
    #print(f"words_counted: {word_count}")
    #print(f"chars_counted: {char_dict}")
    print_report(word_count= word_count, char_count=char_count_dict)

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

def print_report(word_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("\n")
    for key in char_count:
        if key.isalpha():
            print(f"The '{key}' character was found {char_count[key]} times")
    print("--- End report ---")

main()