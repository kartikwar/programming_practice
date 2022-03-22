"""
Given a string, count number of words in it. The words are separated by 
following characters: space (‘ ‘) or new line (‘\n’) or tab (‘\t’) or 
a combination of these.

Example:

input = "One two         three\n four\tfive "
output = 4
"""


def count_words(text):
    # text = text.strip()
    # return len(text)
    alphabet = False
    word = ''
    words = []
    for ele in text:
        if ele not in ['\n', '\t', " "]:
            word += ele
            alphabet = True
        else:
            if alphabet:
                words.append(word)
            word = ''
            alphabet = False
    return len(words)


if __name__ == '__main__':
    text = " \tOn\ne two         three\n four\tfive "
    print(count_words(text))