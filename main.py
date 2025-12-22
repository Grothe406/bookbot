def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = len(count_words(text))

    print(f"Found {num_words} total words")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(words):
    word_count = words.split()
    return word_count

main()
