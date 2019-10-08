import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def removePunks(fileArray):
    """ This not only gets rid of punctuation but as well as STOP_WORDS """
    newArray = []
    for word in fileArray:
        # get rid of that punk!
        for letter in word:
            if letter in string.punctuation:
                word = word.replace(letter, ' ')
        # Ideally returns an array that is then added to the big array
        # Hopefully when we iterate over those words at the end, those will be added into the QA
        word = word.strip()
        fileArray += word.split()

        if word in STOP_WORDS:
            fileArray.remove(word)
        else:
            newArray.append(word)

    return newArray


def gatherMyWords(fileArray):
    wordsAndAmount = {}

    for word in fileArray:
        # do some counting
        if word in wordsAndAmount:
            wordsAndAmount[word] += '*'
        else:
            wordsAndAmount[word] = '*'

    return wordsAndAmount


def sortWords(dict):
    """ Take the dictionary and sort it by which key occurs the most """
    newDict = sorted(dict.items(
    ), key=lambda x: x[1], reverse=True)  # we need to look at the values attached to the keys to then
    # Could do an array with the .items()
    print('This is inside the Sort Words function: ', newDict)
    return newDict


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as variable:
        fileStr = variable.read().lower()

    print(fileStr)
    fileText = fileStr[:]

    fileArray = fileText.split()

    # Clean that array up
    unpunkedFileArray = removePunks(fileArray)

    # Now lets work with that array
    wordsAndAmount = gatherMyWords(unpunkedFileArray)

    # Sort the dictionary
    sortedWordsAndAmount = sortWords(
        wordsAndAmount)  # sort this by highest amount

    # Print that dict
    for word in sortedWordsAndAmount:
        # Should output the same as Clinton shows in the example (spacing not included)
        print(
            f"{word[0]} | {len(word[1])} {word[1]}")
    # It works as intended √√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√√


print_word_freq('emancipation_proclamation.txt')
print_word_freq('seneca_falls.txt')

if __name__ == "__main__":

    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
