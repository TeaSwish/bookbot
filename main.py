from stats import count_words
from stats import count_chars
from stats import sort_dictionary
import sys

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text
        

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    words = count_words(get_book_text(sys.argv[1]))
    chars = count_chars(get_book_text(sys.argv[1]))
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at '{sys.argv[1]}'")
    print(f"------------ Word Count ------------")
    print(f"Found {words} total words")
    print(f"------------ Character Count ------------")
    for item in sort_dictionary(chars):
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============ END ============")


main()
