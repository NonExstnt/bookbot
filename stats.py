def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_by_count(char_count):
    sorted_list = []
    for char, count in char_count.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
