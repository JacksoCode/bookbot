from stats import word_count
from stats import text_count
from stats import characters_in_order
def main():
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at ...")
    print ("----------- Word Count ----------")
    print (f"Found {word_count()} total words")
    print ("--------- Character Count -------")
    print (f"{characters_in_order()}")
    print ("============= END ===============")
main()
