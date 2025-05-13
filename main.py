from stats import get_num_words, get_char_count, sort_by_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def format(file_path, num_words, char_num):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(char_num)):
        print(f"{char_num[i]["char"]}: {char_num[i]["num"]}")
    print("============= END ===============")

def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(frankenstein_text)
    char_count = get_char_count(frankenstein_text)
    sorted_char = sort_by_count(char_count)
    format("books/frankenstein.txt", num_words, sorted_char)
main()