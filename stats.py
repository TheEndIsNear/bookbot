def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_words(book):
    return book.split()

def get_word_count(book):
    return len(get_words(book))

def get_char_frequency(book):
    dict = {}
    for word in get_words(book):
        chars = list(word)
        for char in chars:
            lower= char.lower()
            count = dict.get(lower, 0)
            count+= 1
            dict[lower] = count
    return dict

def sorted_char_frequency(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1],reverse=True))
