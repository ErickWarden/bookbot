from stats import count_words

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    number_of_words = count_words(file_contents)
    print(f"{number_of_words} words found in the document")
    