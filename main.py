import sys
from stats import total_words, total_characters_dict, report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    total = total_words(book_text)
    sorted_items = total_characters_dict(book_text)
    # print functions
    print(book_text)
    print(total)
    print(sorted_items)
    report(total, sorted_items)

main()