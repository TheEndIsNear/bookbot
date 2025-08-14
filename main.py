from stats import get_book_text, get_word_count
def main():
    book_text = get_book_text('./books/frankenstein.txt')
    wc = get_word_count(book_text)
    print(f"{wc} words found in the document")

main()
