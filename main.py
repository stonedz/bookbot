def main():
    book_name = 'frankenstein.txt'
    # open a book in text format and read all its content
    with open('books/'+book_name, 'r') as file: 
        text = file.read()  # read all the content of the file  and store it in the variable text

    print('Reading book:', book_name)
    print('Number of words:', count_words(text))
    count_letters(text)


def count_letters(text):
    text = text.lower()
    letters = {}
    for letter in text:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

    pretty_print_letters(letters)

def sort_on(value):
    return value[1]

def pretty_print_letters(letters):
    for key in sorted(letters, key=letters.get, reverse=True):
        print(f'Letter {key} found {letters[key]} times')

def count_words(text):
    words = text.split()
    return len(words)

main()
