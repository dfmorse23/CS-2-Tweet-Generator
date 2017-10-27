import sys

def clean_source_txt():
    '''This cleans the text into individual words at each index
    without spaces '''
    with open("alice.txt", "r") as f:
        text = f.readlines()
        f.close()
        # strips special characters from each index
        stripped = [line.strip() for line in text]
        stripped_characters = [y.strip(',!()[];!"+-./!?') for y in stripped]
        # splits each index into single words: https://stackoverflow.com/questions/13808592/splitting-each-string-in-a-list-at-spaces-in-python
        text_words = [words for segments in stripped_characters for words in segments.split()]
        lower_text_words = [word.lower() for word in text_words]
        print(lower_text_words)



clean_source_txt()
#
# def histogram(text):
#     ''' function which takes a source_text argument
#     (can be either a filename or the contents of the
#     file as a string, your choice) and return a histogram
#     data structure that stores each unique word along with the
#     number of times the word appears in the source text.'''
#     pass
#
# def unique_words(histogram):
#     '''A unique_words() function that takes a histogram argument and
#     returns the total count of unique words in the histogram. For
#     example, when given the histogram for The Adventures of
#     Sherlock Holmes, it returns the integer 8475'''
#     pass
#
# def frequency(word, historgram):
#     '''function that takes a word and histogram argument and returns
#     the number of times that word appears in a text. For example,
#     when given the word "mystery" and the Holmes histogram, it
#     will return the integer 20.'''
#     c = Counter
#
# if __name__ == '__main__':
#     print(__name__)
