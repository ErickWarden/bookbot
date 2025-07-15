import sys
from stats import (
    count_words, 
    count_characters, 
    characters_list, 
    sort_on
)



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)

    # Call two functions to count both the number of words, and number of characters in the book.
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    char_count_list = characters_list(char_count)
    char_count_list.sort(reverse=True, key=sort_on)

    # Format the char_count_list to look nice.
    ccl_print = ""
    for item in char_count_list:
        ccl_print += f"{item['char']}: {item['num']} \n"

    # Print final report, after formating.
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(ccl_print.rstrip())
    print("============= END ===============")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()