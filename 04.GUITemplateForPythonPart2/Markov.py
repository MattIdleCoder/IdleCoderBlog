#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Creates random, often grammatically correct, but ultimately meaningless text
using Markov word chains created from sample text files provided by the user.
 
A fun utility for creating random text using the word chains found in the user-
specified input files. It uses Markov prediction on a word level, choosing at
random the next word from those found to follow each chain of 1, 2, 3 or 4
words. It then drops the first word and adds the new one to create a new word
chain, and chooses randomly from the list of possible words in the input texts.
 
It does this by creating a dictionary of word chains, , and the words that can
follow them. The size of the sliding word window depends on the Markov order
the user has set. The highest Markov Order allowed has been limited to 4 words,
as higher tends merely to lift chunks of text from only one of the input files.
 
In programming terms, it performs a user-specified Nth order Markov sequential
word analysis upon the named files, creating a paragraph of nonsense text using
words in the same short sequences found in the input files, printing the result
to the standard output. The order of the analysis defines the length of the
word sequences used (default 2). This implementation leaves punctuation and
capitalization of proper nouns as found.
 
The following options are available:
    -w ParaWordLength
        Create a paragraph of pseudo text of WordLength words long.
        Default is 200 words.
 
    -o Order
        Set Markov order to Order. Default is 2 words. Orders of 2 and 3 give
        good results. Order = 1 creates text that is not quite grammatically
        correct but still readable. Orders of 4 tend to lift large chunks of
        text from each source in turn. Orders of 5 or more give a command line
        error since they simply lift a random block of text from one input
        file. If the flag is used but an order not found a command line
        error will be given.
 
    -s "starting phrase"
        Start the pseudo text with the user-provided starting phrase. The phrase
        must appear exactly as entered in one of the input files, and its length
        must equal the length chosen as the Markov order with the -o flag, or
        the default 2. If the flag is used but a phrase not found a command line
        error will be given.
 
    -t
        Time the running of the program
 
    -h
        Print this usage guide ignoring all other flags
 
Examples:
        python3 Markov.py -o3 -w400 'The Odyssey.txt' 'Ulysses.txt'
 
        ./Markov.py -w300 -o2 -s 'Mr Bloom' 'Ulysses.txt' > output_file.txt
 
The user should not have to delete the header and footer text from the input
files - their words rarely pop up in the resulting text. Web and email
addresses are automatically filtered out of headers and footers.
 
 
Possible future improvements:
- add Linux double dash -- verbose command line flags.
- continue the text until a full stop (period) is encountered.
-
 
Known bugs:
-
 
@author: matta_idlecoder@protonmail.com
"""
 
import timeit
import string
import random
import sys
import getopt
import os
 
timing = False
result_string = ''
 
 
def cleanup(word):
    """  Cleans a word of punctuation, numbers, and web & email addresses.
    """
    clean_text_str, new_text = '', []
    char_and_punct_list = list(word)
    CharsToKeep = string.ascii_letters + string.punctuation
 
    if ('@' or 'http' or 'www' or '\.com' or '\.edu' or '\.org' or '\.gov') in word:
        return ''
    for char in char_and_punct_list:
        # first pass - remove digits & unwanted punctuation:
        if (char in CharsToKeep):
            new_text.append(char)
    if len(new_text) == 0:
        return ''
    if len(new_text) > 0:
        # convert mutable list of chars back to immutable string:
        clean_text_str = ''.join(new_text)
    return clean_text_str
 
 
def get_Markov_chains(markov_order, input_file):
    """Creates a Markov dict from the input file words, of the order specified
 
    The Markov order defines the key length. The values are all single words.
    """
    current_line_words = []
    word_suffix_list = dict()
    phrase = []
    phrase_key = tuple()
 
    """The code has already checked that the file exists, so it doesn't needs
    a try,,,,except loop around it:
    """
    fin = open(input_file)
 
    for line in fin:
        # turn the line into a list of words:
        line = line.replace('--', ' ') # found in some English literature
        current_line_words = line.split()
        if len(current_line_words) == 0:
            continue
 
        # Create the Markov dictionary from the list:
        for next_word in current_line_words:
            next_word = cleanup(next_word)
            if len(next_word) == 0:
               continue
            if len(phrase) == markov_order:
                if phrase_key not in word_suffix_list:
                    word_suffix_list[phrase_key] = set()
                word_suffix_list[phrase_key].update([next_word])
                del phrase[0]
            phrase.append(next_word)
            phrase_key = tuple(phrase)
    fin.close()
    return word_suffix_list
 
 
def usage():
    usage_str = "markov, version 1.0\n\nusage: ./Markov.py [-ht] [-o order] "
    usage_str += "[-w paragraph wordlength] [-s start phrase] input_files\n"
    print (usage_str)
    return
 
 
def pick_item(some_sequence):
    """Pick a random item from the sequence provided.
 
    Python duck typing means it can any of list(), dict(), set() or even string
    """
    num_words = len(some_sequence)
    list_of_items = list(some_sequence)   # works on lists
    item_index = random.randint(0, num_words-1)
    random_item = list_of_items[item_index]
    return random_item
 
 
def augment_result_string(*args):
    """Assembles output result as a returned continuous string
    """
    global result_string
    for thing in args:
        result_string += str(thing)
        result_string += ' '
    return
 
 
def left_shift(markov_prefix, word):
    """Shift the markov_prefix left once, add word on the end, return new tuple.
    """
    return markov_prefix[1:] + (word,)
 
 
def Ordinal(integer):
    """Converts an integer from 1-4 into an ordinal string
    """
    if integer == 1:
        return 'first'
    elif integer == 2:
        return 'second'
    elif integer == 3:
        return 'third'
    elif integer == 4:
        return 'fourth'
    else:
        return 'some unknown'
 
 
def create_markov_text_from(pathnames, markov_order=2, word_len=200, 
                            starting_words=''):
    """ Create random text from files in pathnames list, using Markov
 
    Works at word level, not letters.
    """
    global result_string
    result_string = ''
    markov_dict = dict()
 
    order_as_text = Ordinal(markov_order)
    first_file = True
 
    goal = '\nThe following text(s) will now be analysed to create a {} order '
    goal += 'Markov word-chain dictionary:\n\n'
    augment_result_string(goal.format(order_as_text))
 
    for pathname in pathnames:
        path, filename = os.path.split(pathname)
        augment_result_string('* ', filename, '\n')
 
    augment_result_string('\n')
 
    if timing:
        zerotime = timeit.default_timer()
 
    for pathname in pathnames:
        path, filename = os.path.split(pathname)
        augment_result_string('Getting {} order word chains from: {}\n'.
                              format(order_as_text, filename))
 
        if first_file == True:
            if timing:
                now = timeit.default_timer()
                augment_result_string('\tElapsed time: ', 
                                      round(now - zerotime, 2), 'seconds.\n')
            markov_dict = get_Markov_chains(markov_order, pathname)
            first_file = False
 
        else:
            if timing:
                now = timeit.default_timer()
                augment_result_string('\tElapsed time: ', 
                                      round(now - zerotime, 2), 'seconds.\n')
            next_markov_dict = get_Markov_chains(markov_order, pathname)
 
            for key in next_markov_dict:
                if key in markov_dict:
                    markov_dict[key] = markov_dict[key] | next_markov_dict[key]
 
                else:
                    markov_dict[key] = next_markov_dict[key]
 
    output_intro = '\nBelow is a random block of {} words of pseudo text '
    output_intro += 'that was created using the {} order Markov word-chain '
    output_intro += 'dictionary derived from the above text(s). '
    if starting_words == '':
        output_intro += '\n\nThe opening words were chosen at random.\n\n'
    else:
        output_intro += '\n\nThe opening words were chosen as "{}"...\n\n'.format(starting_words)
 
    augment_result_string(output_intro.format(word_len, order_as_text))
    if starting_words == '':
        markov_key_words = pick_item(markov_dict)
    else:
        markov_key_words = tuple(starting_words.split())
        assert len(markov_key_words) == markov_order
        if markov_key_words not in markov_dict:
            cmd_line_error = '\nCheck your opening words - those you have chosen '
            cmd_line_error += 'cannot be found in any of the input texts.'
            if __name__ == '__main__':
                print(cmd_line_error)
                sys.exit(2)
            else:
                return '', cmd_line_error
 
    augment_result_string(*markov_key_words)  # Start the paragraph with the starting_words
    for i in range(word_len):
        next_word_set = markov_dict[markov_key_words]
        next_word = pick_item(next_word_set)
        augment_result_string(next_word)
        markov_key_words = left_shift(markov_key_words, next_word)
    augment_result_string('\n\n')
 
    return (result_string, 'OK')
 
 
def main(argv):
 
    global timing
    timing = False
    MarkovOrder = 2
    ParaLength = 200
    StartText = ''
    PathList = []
    output_paragraph = ''
 
    try:
        opts, args = getopt.getopt(argv, "o:w:s:th")
 
    except getopt.GetoptError as cmd_err:
        print (str(cmd_err))
        usage()
        sys.exit(2)  # (Unix convention: 0=no problem, 1=error, 2=cmdline)
 
    for opt, value in opts:
        if opt == '-o':
            try:
                MarkovOrder = int(value)
                if MarkovOrder > 4:
                    high_markov_error = "\nWhat's the point? All this order "
                    high_markov_error += "will do is lift a block of verbatim "
                    high_markov_error += "text from one of your input files!\n"
                    print (high_markov_error)
                    sys.exit(2)
            except ValueError:
                print ('\nCommand line error: missing integer with -o flag.\n')
                sys.exit(2)
 
        elif opt == '-s':
            StartText = value
            if len(StartText.split()) != MarkovOrder:
                Markov_error = '\nUser error on command line: the number of '
                Markov_error += 'starting words must equal the Markov order.\n'
                print (Markov_error)
                sys.exit(2)
 
        elif opt == '-w':
            try:
                ParaLength = int(value)
                if (ParaLength < 50) or (ParaLength > 1000):
                    print ("Try a paragraph length between 50 and 1,000 words")
                    sys.exit(2)
            except ValueError:
                print ('\nCommand line error: missing integer with -w flag.\n')
                sys.exit(2)
 
        elif opt == '-t':
            timing = True
            start = timeit.default_timer()
 
        elif opt == '-h':
            usage()
            print (__doc__, '\n')
            sys.exit(0)
 
        else:
            print ('\nopt = {}\n'.format(opt))
            assert False, "Programming error: main() has an unhandled option"
 
    if len(args) == 0:
        print ('\nCommand line error: requires at least one input file.\n')
        usage()
        sys.exit(2)
 
    # check the input files are there before proceeding:
    for arg in args:
        try:
            f = open(arg, 'r')
        except IOError:
            print ('\nFilename error: no such file: {}\n'.format(arg))
            sys.exit(2)
        else:
            f.close()
            PathList.append(arg)
 
    output_paragraph, error = create_markov_text_from(PathList,
                            markov_order=MarkovOrder, word_len=ParaLength,
                            starting_words=StartText)
    if error != 'OK':
        print('Error returned from create_markov_text_from(): {}'.format(error))
        sys.exit(1)
    else:
        print(output_paragraph)
 
    if timing:
        stop = timeit.default_timer()
        print ('\nThe creation of this Markov text took', 
               round(stop - start, 2), 'seconds.\n')
    return
 
 
 
if __name__ == "__main__":
    main(sys.argv[1:])

