from stats import get_num_char


def get_book_text(book):
    #print("test point one")
    with open("books/" + book, encoding="utf-8") as f:
        #print("test point two")
        file_contents = f.read()
    #print("test point three")
    return file_contents


def main():
    my_string = get_book_text("frankenstein.txt")
    my_output = get_num_char(my_string)
    print(my_output)
main()
