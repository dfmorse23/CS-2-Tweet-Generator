import sys, random
from histogram import *


def return_word(histogram):
    '''function that takes a histogram (however youve structured yours)
    and returns a single word, at random. It should not yet take
    into account the distributions of the words
    takes a list of keys
    picks a random key, displays a key as a string
    return string'''
    result = []
    random_index = random.randint(0, len(histogram)- 1)
    # print(random_index)
    for i in histogram:
        result.append(i)
    # for key in result:
    #     return key
    return result[random_index]

def frequency_weight():
    weight_dictionary = {}
    sum_values = sum(histogram(word_list).values())
    for word in word_list:
        word_occurances = word_list.count(word)
        weighted_occurances = word_occurances / sum_values

    return

# def stochastic_array():
#     ''' '''
#def weighted_dict():
    # for word, count in dict.items():
    # weightedhist[word2 = float(count / len (histo))]

def stochastic_count(histogram):
    ''' takes histogram
    uses histogram to select a random word at probability
        weighted to it's frequency
    returns random word'''
    # result_word = []
    random_index = random.randint(1, sum(histogram.values())) #sum the histogram values
    #print(random_index)
    for key, value in histogram.items():
        random_index -= value
        if random_index > 0:
             #int(key[0])
            continue
        else:
            return key

def stoch_loop(histogram):
    test_dict = {}
    for word in range(10000):
        word =  stochastic_count(histogram)
        if word in test_dict:
            test_dict[word] += 1
        else:
            test_dict[word] = 1
    print(test_dict)
    #count reds
        #count blue

if __name__ == '__main__':
    lower_text_words = clean_source_txt("fishtext.txt")
    # print(lower_text_words)
    histo = histogram(lower_text_words)
    print(histo)
    word = return_word(histo)
    #print(word)
    stoch = stochastic_count(histo)
    stoch_loop(histo)
    print(stoch)
    #print(word)
    #print(len(histo))

# python is index inclusive based on the < or = or >
