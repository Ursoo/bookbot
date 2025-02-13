
def main():
    path = "./books/frankenstein.txt"
    book_content = read_book_contents(book_path=path)
    word_count = count_words(string=book_content)
    print(f"{word_count} words")

def read_book_contents(book_path):
    with open(book_path) as f:
        content = f.read()
    return content


def count_words(string: str):
    return len(string.split())


main()