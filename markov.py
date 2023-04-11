"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    open_file = open(file_path)
    contents = open_file.read()
    open_file.close()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    words = text_string.split() 

    for i in range(len(words) - 2):
        word1 = words[i]
        word2 = words[i + 1]
        word3 = words[i + 2]
        
        key = (word1, word2)
        value = word3

        if key not in list(chains.keys()):
            chains[key] = []
        chains[key].append(value)
        
    return chains


def make_text(chains):
    """Return text from chains."""

    key_list = list(chains.keys())
    key = (choice(key_list))
    word = choice(chains[key])
    output_string = [word]

    while True:
        key = (key[1], word)

        if key in key_list:
            word = choice(chains[key])
            output_string.append(word)
        else:
            break
    
    
    return ' '.join(output_string)

# import sys first
# reassign second index argument into input_path variable
input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# print(chains)

# Produce random text
random_text = make_text(chains)
print(random_text)