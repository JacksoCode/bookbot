from stats import word_count
from stats import text_count 
def main():
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at ...")
    print ("----------- Word Count ----------")
    print (f"Found {word_count()} total words")
    print ("--------- Character Count -------")
    print (f"{text_count()}")
    print ("============= END ===============")
main()
