from stats import get_num_char, sortit_dict
from stats import get_num_words
import sys


def get_book_text(book):
    #print("test point one")
    with open(book, encoding="utf-8") as f:
        #print("test point two")
        file_contents = f.read()
    #print("test point three")
    return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookfile = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookfile}...")
    print("----------- Work Count -----------")
    my_string = get_book_text(bookfile)
    word_output = get_num_words((my_string))
    char_output = get_num_char(my_string)
    print("Found " + str(word_output) + " total words")
    #print(char_output)
    dict_output = sortit_dict(char_output)
    print("--------- Character Count ---------")
    for x in dict_output:
        alph = x['name']
        if alph.isalpha() is True:
            print(x['name'] + ": " + str(x['num']))



main()
