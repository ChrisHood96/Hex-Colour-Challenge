import json

def create_smaller_dict():
    # One time use function to create a smaller dictionary of applicable comparison words
    valid_length_word = {}
    for i in dict:
        if 2 < len(i) <= 6:
            valid_length_word[i] = 1
    with open("smaller_dictionary", 'w') as f:
        f.write(json.dumps(valid_length_word))

# Global var, a mapper and opening the dictionary file for comparison
existing_words = {}
# Mapper is very basic with 1:1 value checks, with more time we could add more, and write code to handle iterations
mapper = {
    0: "o",
    1: "l",
    2: "z",
    3: "e",
    4: "a",
    5: "s",
    6: "c",
    7: "t",
    8: "b",
    9: "g"
}
with open("smaller_dictionary") as f:
    dict = json.loads(f.read())
    f.close

def create_doc(word_doc):
    # Once we've gathered all of our hexwords, write to these to file
    with open("hex_words_dict.json", 'w') as f:
        f.write(json.dumps(word_doc))
        f.close
            

def check_word_exists(word, hex_colour):
    # Check the word exists, if not strip any 0's as I'm considering these null values if on the end and check again if the new value is a word
    if word[1:] in dict:
        existing_words[hex_colour.upper()] = word.upper()
    else:
        if word.endswith('o'):
            check_word_exists(word[:-1], hex_colour)


def map_hex_colour_to_word(hex_colour):
    # Use the above mapper to change any int characters to letters, hex_colour briefly made to a list for easy replacement
    word_colour_list = list(hex_colour)
    for i, j in enumerate(word_colour_list):
        if j.isnumeric():
            word_colour_list[i] = mapper[int(j)]
    check_word_exists("".join(word_colour_list), hex_colour)


def iterate_hex_colours():
    # Function to iterate through all possible combinations of hexadecimal colours and flow through other functions
    for r in range(256):
        for g in range(256):
            for b in range(256):
                hex_colour = "#{:02x}{:02x}{:02x}".format(r,g,b)
                map_hex_colour_to_word(hex_colour)
    create_doc(existing_words)

iterate_hex_colours()



