import sys

def clean_source_txt(file_name):
    '''This cleans the text into individual words at each index
    without spaces '''
    with open(file_name, "r") as f:
        text = f.readlines()
        f.close()
        # strips special characters from each index
        # splits each index into single words: https://stackoverflow.com/questions/13808592/splitting-each-string-in-a-list-at-spaces-in-python
        text = [words for segments in text for words in segments.split()]
        text = [line.strip() for line in text] #list comprehension and you are saving it in a list
        text = [y.strip(',!()[]:_;!"+-./!?') for y in text]
        text = [word.lower() for word in text]
    return text
    #histogram(lower_text_words)

#
def histogram(clean_text):
    ''' function which takes a source_text argument
    (can be either a filename or the contents of the
    file as a string, your choice) and return a histogram
    data structure that stores each unique word along with the
    number of times the word appears in the source text.'''
    #clean_text = clean_source_txt()
    histogram = {}
    for word in clean_text:
        if word not in histogram:
            histogram[word] = 1
            continue
        else:
            histogram[word] += 1
    # return(histogram)
    return histogram
    pass


def unique_words(histogram):
    '''A unique_words() function that takes a histogram argument and
    returns the total count of unique words in the histogram. For
    example, when given the histogram for The Adventures of
    Sherlock Holmes, it returns the integer 8475'''
    return len(histogram.keys())
    pass

def frequency(word, histogram):
    '''function that takes a word and histogram argument and returns
    the number of times that word appears in a text. For example,
    when given the word "mystery" and the Holmes histogram, it
    will return the integer 20.'''
    if word not in histogram:
        return("Word not in histogram") # don't need an else?

    return histogram[word]
#     #c = Counter https://docs.python.org/3.6/library/collections.html#collections.Counter
#
if __name__ == '__main__':
    lower_text_words = clean_source_txt("alice.txt")
    # print(lower_text_words)
    histo = histogram(lower_text_words)
    print(unique_words(histo))
    print(frequency("dog", histo))

# instead of making multiple variables for the same manipulation of text, you can keep the same one
# ^ in this case, use comments; you can keep conistent to have the order not break
# to carry variables from functions to other functions you need to save the values
# ^ in the command line
# can only return from a function once - it wll happen
# Nonetype may be because you didn't return what you needed to
