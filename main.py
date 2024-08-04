def sort_on(dict):
    keys = list(dict)
    return dict[keys[0]]


def reformat_char_dict(char_dict):
    char_list = []
    for k in char_dict:
        if k.isalpha():
            ch_sep_dict = {k: char_dict[k]}
            char_list.append(ch_sep_dict)

    char_list.sort(key=sort_on, reverse=True)
    return char_list


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
    reformatted = reformat_char_dict(char_count)
    print("----------- REPORT FOR THIS BOOK ------------\n")
    print(f"There are {word_count} in this book\n")
    for d in reformatted:
        for key in d:
            print(f"There are {d[key]} {key} in this book")

    print("\nREPORT FOR THIS BOOK ----------- END REPORT ------------\n")


main()
