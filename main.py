def count_words(text_file):
    words = text_file.split()

    return len(words)

def count_chars(text_file):
    chars_dict = {}

    words = text_file.split()

    for word in words:
        lowered_word = word.lower()
        for char in lowered_word:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
    return chars_dict

def main():

    path_to_books = "books/"
    with open(path_to_books + "frankenstein.txt") as f:
        file_contents = f.read()

    book_words_count = count_words(file_contents)
    print(f"{book_words_count} words found in this book")

    book_chars_count = count_chars(file_contents)
    print("dictionary with counting chars:")
    for chars in book_chars_count:
        print(f"{chars}: {book_chars_count[chars]}")

if __name__ == '__main__':
    main()
