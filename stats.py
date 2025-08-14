def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_word_count(book):
    return len(book.split())
