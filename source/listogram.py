#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        self.tokens += count
        for index, pair in enumerate(self): #seperate the list of tuples to it's index and tuple pair
            if pair[0] == word:
                pair_update_prep = self.pop(index) #remove tuple at index and return it
                self.insert(index, (word, pair_update_prep[1] + count)) #insert at this index, this tuple
                # close function if we find the word
                return True

        self.append((word, count))
        # add a new type if word is not already present
        self.types += 1

            # for list_word, freq in big_list:
            #     if list_word == word:
            #         freq += count
            #     else:
            #         self.append([word, 1])


    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        for big_list in self:
            if big_list[0] == word:
                return big_list[1]

        return 0
        # for list_word, freq in self:
        #     if list_word == word:
        #         return freq
        #     else:
        #         return 0
        #if self.__contains__(word):

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        for big_list in self:
            if big_list[0] == word:
                return True
            else:
                continue

        # for list_word, freq in self:
        #     if list_word == word:
        #         return True
        #     else:
        #         return False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        index = None

        for word_index in range(len(self)):
            if self[word_index][0] == target:
                index = word_index

        return index



def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
