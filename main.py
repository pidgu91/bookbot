def count_words():
    total = 0
    with open('/home/xetekk/Documents/Python/bookbot/books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            if word in words:
                total += 1
        return total, words

def count_letters(words):
    dict = {}
    keys = []
    for letter in words:
        for a in letter.lower():
            if a.isalpha():
                keys.append(a)

    for letter in keys:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

def report(total, letters):
    print(letters)
    print(f"{total} words found in the document")
    #print(list_words)


total, words = count_words()
letters = count_letters(words)
report(total, letters)
