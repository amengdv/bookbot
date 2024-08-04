def count_characters(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def count_words(text):
    return len(text.split())


def get_book_content(path):
    with open(path) as f:
        return f.read()


def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_content(path)
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    print(f"There are {word_count} in this book")
    print("Character report:")
    print(char_count)


main()
