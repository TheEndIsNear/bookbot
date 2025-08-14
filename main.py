def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_word_count(book):
    return len(book.split())

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    wc = get_word_count(book_text)
    print(f"{wc} words found in the document")

main()
