def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
        return contents

def word_count():
    words = get_book_text("books/frankenstein.txt")
    word_count = len(words.split())
    return word_count

def text_count():
    text = get_book_text("books/frankenstein.txt")
    lower_text = text.lower()
    low_letters = list(lower_text)
    letters = " ".join(low_letters)
    now_count = {"a": 0, 
                 "b": 0, 
                 "c": 0, 
                 "d": 0,
                 "e": 0,
                 "f": 0,
                 "g": 0,
                 "h": 0,
                 "i": 0,
                 "j": 0,
                 "k": 0,
                 "l": 0,
                 "m": 0,
                 "n": 0,
                 "o": 0,
                 "p": 0,
                 "q": 0,
                 "r": 0,
                 "s": 0,
                 "t": 0,
                 "u": 0,
                 "v": 0,
                 "w": 0,
                 "x": 0,
                 "y": 0,
                 "z":0
    }
    for character in now_count:
        count = now_count[character]
        if letters == character:
            count += 1
        return now_count
