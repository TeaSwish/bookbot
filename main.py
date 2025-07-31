from stats import count_words
from stats import count_chars
from stats import sort_dictionary
from stats import pretty_print

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text
        #print(book_text)

def main():
    words = count_words(get_book_text("books/frankenstein.txt"))
    chars = count_chars(get_book_text("books/frankenstein.txt"))
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at 'books/frankenstein.txt'")
    print(f"------------ Word Count ------------")
    print(f"{words} words found in the document")
    print(f"------------ Character Count ------------")
    for item in sort_dictionary(chars):
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============ END ============")


main()
