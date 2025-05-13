from stats import (
    get_num_words, 
    get_char_count, 
    sort_by_count
    )
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(file_path, num_words, sorted_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

def arg_check():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def main():
    file_path = arg_check()
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_char = sort_by_count(char_count)
    print_report(file_path, num_words, sorted_char)
main()