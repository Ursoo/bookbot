import sys
from stats import count_character_occurence, count_words, read_book_contents, print_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_content = read_book_contents(book_path=path)
    word_count = count_words(string=book_content)
    char_count_dict = count_character_occurence(string=book_content)
    #print(f"Found {word_count} total words")
    #print(f"chars_counted: {char_count_dict}")
    print_report(word_count= word_count, char_count=char_count_dict)



main()