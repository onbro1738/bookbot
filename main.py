def open_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

open_text()

text = open("books/frankenstein.txt").read()

def word_count(text):
    number_of_words = len(text.split())
    return number_of_words

print(word_count(text))

text = open("books/frankenstein.txt").read()

def count_characters():
    char_dict = {}
    my_text = text
    lower_case = my_text.lower()

    for i in lower_case:
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1

    return char_dict

print(count_characters())

def print_report():
    char_dict = count_characters()

    char_list = list(char_dict.items())

    def get_count(item):
        return item[1]
    
    char_list.sort(reverse=True, key=get_count)

    for char, count in char_list:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

print_report()