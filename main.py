from stats import get_num_words, get_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(frankenstein_text)
    char_count = get_char_count(frankenstein_text)
    print(f"{num_words} words found in the document")
    print(f"{char_count}")
main()