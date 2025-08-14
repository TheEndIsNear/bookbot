from stats import get_book_text, get_word_count, get_char_frequency, sorted_char_frequency
def main():
    book_filepath = './books/frankenstein.txt'
    book_text = get_book_text(book_filepath)
    wc = get_word_count(book_text)
    char_dict = get_char_frequency(book_text)
    sorted_char_dict = sorted_char_frequency(char_dict)
    print_report(book_filepath, wc, sorted_char_dict)

def print_report(book_filepath, wc, char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for key, value in char_dict.items():
        if key.isalpha():
            print(f"{key}: {value}")

main()
