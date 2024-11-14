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

    path_to_book = "books/frankenstein.txt"
    with open(path_to_book) as f:
        file_contents = f.read()

    book_words_count = count_words(file_contents)
    print(f"--- Begins report of {path_to_book} ---")
    print(f"{book_words_count} words found in this book")

    book_chars_count = count_chars(file_contents)
    sorted_dict = dict(sorted(book_chars_count.items(), key=lambda item: item[1], reverse=True))

    print("dictionary with counting chars:")
    for chars in sorted_dict:
        if chars.isalpha():
            print(f"The '{chars}' charachter was found {book_chars_count[chars]} times")
    print("--- End report ---")

if __name__ == '__main__':
    main()
