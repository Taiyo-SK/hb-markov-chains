"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    # 1. open file input_path
    # 2. read a file as one string of context
        # save the file-string as a new variable
    # 3. close file
    # 4. return one string

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

    # your code goes here
    # 1. split the string so each word is its own string
    # 2. making a loop and a new list variable as bigram, 
    #    pick two words as a tuple from a line and put into a new variable
    #   have to identify possible words as values, too?
    
    words = text_string.split()

    # possible_words = []
    # while..?
    # chains.get()
    ## From the hint
        # 1. Make empty dict
        # 2. Loop over the words in the list of words, making sure can access
            # at i, i+1, and i+2 without returning IndexError
        # 3. Modify loop so the words at i and i+1 become a tuple
            # use the tuple as the key in our dictionary
        # 4. create a list as the pair value and append words into it
        # 5. When do we make the empty list and append into it?
            # a. check if they key is in the dict already
            # b. if not, initialize that list and add word to it
            # c. if key is in dict, append word to the list that already exists
    # chains[(word1, word2)] = []
    # word1 = words[i]
    # word2 = words[i + 1]

    for i in range(len(words) - 3):

        links = chains.get((words[i], words[i + 1]), [])
        print(links.append(words[i + 2]))
        chains[(words[i], words[i + 1])] = links
        
        # if chains[(words[i], words[i + 1])] == []:
        #     chains[(words[i], words[i + 1])].append(words[i + 2])
        
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(input_text)
print(chains)
