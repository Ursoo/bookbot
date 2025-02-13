
def main():
    path = "./books/frankenstein.txt"
    book_content = read_book_contents(book_path=path)
    word_count = count_words(string=book_content)
    char_dict = count_character_occurence(string=book_content)
    print(f"words_counted: {word_count},\n")
    print(f"chars_counted: {char_dict}, \n")

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

main()