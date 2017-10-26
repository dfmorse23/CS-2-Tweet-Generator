import random
import sys
import time
''' first need to read the data type, see how it's formatted so we can call it properly '''

''' pass in parameter for number of works, that's it
print the number of words of the parameter that is passed
HOW DO YOU GET A PARAMETER OF AN ENTIRE SCRIPT"
'''

#COMPLETE
#print(dict_words)
def random_word(): #method
    #creates a random number for each index
    random_index = random.randint(0, len(dict_words) - 1)
    return dict_words[random_index].rstrip('\n')

def multiple_rand_words(number_of_words):
    list_of_words = ''
    for i in range(0, number_of_words):
        list_of_words += (random_word() + ' ')
    return list_of_words
#multiple_rand_words(number_of_words)

timestamp1 = time.time()
print(timestamp1)


if __name__ == '__main__': # command line argument that will run the script; this makes this file an importable module and independently executable
    dict_words = open("/usr/share/dict/words").readlines()
    input = int(sys.argv[1]) #this is the command line input
#    import pdb; pdb.set_trace()
    print(multiple_rand_words(input))
    timestamp2 = time.time()
    print(timestamp2)
    print(timestamp2 - timestamp1)

#need a sys.argv is how you do a system argument which is basically passing in a parameter into the command line


#NOTES
#.strip() removes all special character
# list comprehension
    #striped_words = [items.strip() for item in words_list]
#[1:] slice
# time.time() reads how long it takes to get to a particular place in the program
