from stats import word_count
from stats import text_count
from stats import characters_in_order
def main():
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at books/frankenstein.txt...")
    print ("----------- Word Count ----------")
    print (f"Found {word_count()} total words")
    print ("--------- Character Count -------")
    mychar = characters_in_order()
    for c in mychar:
        char = c["char"]
        num = c["num"]
        print (f"{char}: {num}")
    print ("============= END ===============")
main()
