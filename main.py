def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)


main()


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
        






