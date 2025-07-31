from stats import count_words
from stats import count_chars
from stats import sort_dictionary

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text
        #print(book_text)

def main():
 #   words = count_words(get_book_text("books/frankenstein.txt"))
    chars = count_chars(get_book_text("books/frankenstein.txt"))
 #   print(f"{words} words found in the document")
 #   print(chars)
    sort_dictionary(chars)
    
 

main()
