def count_words(text):
    return len(text.split())


def get_book_content(path):
    with open(path) as f:
        return f.read()


def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_content(path)
    word_count = count_words(file_contents)
    print(f"There are {word_count} in this book")


main()
