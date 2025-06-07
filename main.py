from stats import word_count
from stats import text_count
from stats import characters_in_order
import sys
userpath = sys.argv[1]
def main():
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {userpath}...")
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
