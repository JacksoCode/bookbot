def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
        return contents

def word_count():
    words = get_book_text("books/frankenstein.txt")
    word_count = len(words.split())
    return word_count
