def total_words(book):
    count = len(book.split())
    return count

def total_characters_dict(book):
    total = {}
    for char in book:
        character = char.lower()
        if character not in total:
            total[character] = 1
        else:
            total[character] += 1
    return total

def sort_on(total_characters):
    return total_characters["num"]

def report(total, total_char_dict):
    items = []
    for ch, count in total_char_dict.items():
        items.append({"char": ch, "num": count})
    items.sort(key=sort_on, reverse=True)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    for char in items:
        print(char["char"] + ":" + " " + str(char["num"]))