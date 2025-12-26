from stats import count_words, count_characters, sort_characters
import sys

def main():
    if len(sys.argv) <= 1:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = len(count_words(text))
        num_characters = count_characters(text)
        sorted_characters = sort_characters(num_characters)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_characters:
            if not item["char"].isalpha():
                continue
            print(f"{item["char"]}: {item["num"]}")

        print("============= END ===============")
    

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()
