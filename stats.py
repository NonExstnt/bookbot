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

