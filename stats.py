import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

userpath = sys.argv[1]

def get_book_text():
    with open(userpath) as f:
        contents = f.read()
        return contents

def word_count():
    words = get_book_text()
    word_count = len(words.split())
    return word_count

def text_count():
    text = get_book_text()
    lower_text = text.lower()
    low_letters = list(lower_text)
    letters = "".join(low_letters)
    characters = {}
    for i in letters:
        if i not in characters:
            characters[i] = 1
        else:
            characters[i] += 1
    return characters

def mysort(d):
    return d["num"]

def characters_in_order():
    run_text = text_count()
    char_sort = []
    for text in run_text:
        if text.isalpha():
            count = run_text[text]
            char_sort.append({"char": text, "num": count})
    char_sort.sort(reverse=True, key=mysort)
    return char_sort
