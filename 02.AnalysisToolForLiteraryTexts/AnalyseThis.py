#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\nPerforms a textual analysis of any given text, giving a summary of
the frequencies of words used, grouping the words by frequency (the
default) or listing them alphabetically with their individual frequencies (-f).
Calculates the size of the vocabulary used.
 
Additionally, the following optional analyses may be performed: a spellcheck
against a default (-d) or user-specified dictionary (-D), plus lists of any or
all of the following gramatical features used by the author/translator:
archaisms, contractions, gerunds, compound words, adverbs and proper nouns.
 
If called from the command line, the output is printed as an unformatted
continuous string to the std output, with paragraph breaks but no line- or
page-breaks. If redirected, it will therefore self-format to your own page
size. If called as a module by another program, it will return the output to
the calling program as a continuous string.
 
Regarding the dictionary, the code requires a dictionary called
EnglishDictionary.txt in the same folder as this source code, unless you
specify an alternative path to your own named dictionary using the -D flag.
 
Regarding file paths in the command line: Relative paths such as
'../../The_Odyssey.txt' notation are understood. If you're using Windows, make
sure you use the Unix forward slash '/', not the windows backslash '\' in your
dictionary paths.
 
 Usage: from the command line type:
    AnalyseThis_v4.py -i <input_file> [-s <start_string>] [-e <end_string>]
    [-D <your_dict_filepath>] [-R <N>] [-acdfghyHPt] [> output_file]
 
    -i rel_path/input_file
        Mandatory flag: instructs the program to analyse the text in the file
        with name input_file. This can be filename, or a complete or relative
        path name.
 
Optional flags (in order of typical usage):
    -s "start trigger text"
        Don't start analysing the text in the input_file until after you've
        found the start trigger string in the input text file. Defaults to the
        start of the input file.
 
    -e "end trigger text"
        Stop analysing when you have found the end trigger text in the input
        file. This string is not analysed. Defaults to the EOF of the input
        file.
 
    -d
        Check all words against the program's built-in dictionary, listing
        those not in the dictionary. Default is not to spellcheck.
 
    -D rel_path/dictionary
        Use the user-specified dictionary in rel_path/dictionary to check the
        validity of all words found. Default is not to check any words.
        Any word not in the dictionary is listed, in addition to its listing
        in the frequency analysis. Overrides '-d'.
 
    -P
        Omit proper nouns from the word frequency analysis and dictionary
        check and summarise them in a separate list.
 
    -H
        List separately all hyphenated compound words used. Leaves them out of
        the word frequency analysis and dictionary check (if selected) by
        splitting them into their component words.
 
    -a
        list all simple archaisms uses. Uses a regex to search for words
        not found in the dictionary ending in: "eth", "dst", "est", "urst"
        and "ert".
 
    -c
        List all contractions used. Seaches the list words found for any
        containing an apostrophe. Ignores singular possessives, which are
        removed them from the word frequency analysis.
 
    -g
        List all gerunds and present tense continuous words ending in '-ing',
        removing them from the word frequency analysis.
 
    -y
        List all adverbs ending in '-ly'.
        Note 1: does not find all adverbs. Misses those adverbs that do not
        end in '-ly', e.g. fast, well.
        Note 2: Also counts words that end in '-ly' that are not always adverbs,
        e.g. early, fly, really, kingly.
        Note 3: Still counts the words in the main list in their own right.
        Reason: working out the base words is not always obvious. Many -ly
        adverbs are not formed simply by adding '-ly', e.g. laughably, daily,
        wearily.
 
    -R <N>
        Ignore Roman numerals up to maximum N., e.g. i, ii/II, iii/III, iv/IV.
        Note 1: with capital Romans, only those from II and up are ignored.
        If this flag is not set, they will be counted as words. Even if set,
        all instances of the Roman number I will be counted as occurrences of
        the first person singular 'I'.
 
    -f
        Print the analysis section as an alphabetically sorted list with the
        associated word frequencies, eg: apple(4) as(345) ... zebra(1).
        Replaces the normal list grouped by frequency.
 
    -t
        Time the running of the program, time stamping the output file/stream
        with how long the analysis took.
 
    -h
        Help: prints this long version of the usage.
  
Example command line, using the Gutenberg edition of the 1879
Butcher and Lang translation of Homer's Odyssey:
 
    AnalyseThis.py -i "The Odyssey.txt" -s "investigation" -e "Homer, thy song"
    -R 1000 -cadfgyHP > OdysseyAnalysis.txt
 
@author: matta_idlecoder@protonmail.com
"""
import timeit
import string
import re
import os
import sys
import getopt
 
result_string = ''
 
 
def output(*args):
    """Assembles output result as a returned continuous string, or prints it
 
    Action depends on how the module has been called. By assembling the result
    as an output string, it allows the result to be returned to the calling
    program, if that's how the module is called. Allows a calling GUI wrapper
    to display it however it wants to. If it has been invoked from the
    commmand line, it returns the result to the std output, separated by
    spaces, rather than the default '\n' between items. Works for single items,
    or any iterable object.
    """
    global result_string
    if __name__ == '__main__':
        for count, thing in enumerate(args):
            print(thing, end=' ')
    else:  # code has been imported by another program. Augment the return string:
        for count, thing in enumerate(args):
            result_string += thing
            result_string += ' '
    return
 
 
def print_list_items(input_list):
    """ Prints out any list, separating the items by spaces
 
    Output is one long text string onto multiple lines, to allow the output
    to be formatted to the page size of the display.
    """
    for i in range(len(input_list)):
        output(input_list[i])
    return
 
 
def to_romancaps(x):
    """ Returns the uppercase Roman numerals equivalent of an Arabic number.
 
    modified from http://rosettacode.org/wiki/Roman_numerals/Encode#Python
    """
    ret = []
    anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rnumscaps = "M CM D CD C XC L XL X IX V IV I".split()
    for a,r in zip(anums, rnumscaps):
        n,x = divmod(x,a)
        ret.append(r*n)
    return ''.join(ret)
 
 
def to_romanlower(x):
    """ Returns the lowercase Roman numerals equivalent of an Arabic number.
 
    modified from http://rosettacode.org/wiki/Roman_numerals/Encode#Python
    """
    ret = []
    anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rnumslower = "m cm d cd c xc l xl x ix v iv i".split()
    for a,r in zip(anums, rnumslower):
        n,x = divmod(x,a)
        ret.append(r*n)
    return ''.join(ret)
 
 
def GetRomanNumerals(UptoMaxNumeral=100, lowercase=True,
                     uppercase=True):
    """ Returns a list of Roman numerals, in both upper or lower case, or both.
 
    modified from http://rosettacode.org/wiki/Roman_numerals/Encode#Python
    """
    roman_num_caps, roman_num_lower = [], []
    romannums = []
 
    for val in range(1,UptoMaxNumeral+1):
        if lowercase:
            roman_num_lower.append(to_romanlower(val))
        if uppercase:
            roman_num_caps.append(to_romancaps(val))
 
    romannums = roman_num_caps + roman_num_lower
    return romannums
 
 
def tidy_ends(letter_list):
    """strips non-alpha ends from a character list, leaving letters at each end
    """
    while letter_list[0] not in string.ascii_letters:
        del letter_list[0]
        if len(letter_list) == 0:
            return ''
    while letter_list[-1] not in string.ascii_letters:
        del letter_list[-1]
        if len(letter_list) == 0:
            return ''
    return letter_list
 
 
def clean_up(word):
    """ Cleans a word of any punctuation & numbers, returning it as lower case
 
    Algorithm is to remove surrounding special chars, then trailing <'s>
    then everything else that isn't an alpha or an apostrophe.
    """
    clean_text_str = ''
    new_text = []
 
    if not word:
        return(word)
 
    # word is a string, which is immutable in Python, we need a list:
    char_list = list(word)
    CharsToKeep = list(string.ascii_letters) + ["'"] + ['-']
 
    """ A more comprehensive list is obviously possible. Net has been omitted
    as it is also a valid word:  """
    if re.match(r'\b(http|www|com|org|edu|gov)\b', word, flags=0):
        return ''
 
    char_list = tidy_ends(char_list)
 
    if char_list[-2:] == ["'", "s"]:
        # remove obvious possessives and contractions that use <'s>
        char_list = char_list[:-2]
 
    # if we got this far, whatever it it, it must have a letter on each end:
    for char in char_list:
        if char in CharsToKeep:
            # get rid of everything except letters and apostrophes:
            new_text.append(char)
 
    if len(new_text) == 0:
        # Should never be true, but just in case:
        return ''
    else:
        # convert mutable list of chars back to immutable string:
        clean_text_str = ''.join(new_text)
 
    return clean_text_str
 
 
def CreateDictionarySet(DictionaryPath):
    """ Fetches a dictionary file, returning a dictionary word set.
    """
    dictionary_wordset, KnownProperNouns = set(), set()
 
    dict_file = open(DictionaryPath)
    for line in dict_file:
        word = line.strip()            # assumes one word per line
        dictionary_wordset.add(word)
    dict_file.close()
 
    """ NOTE: This is necessary for the simple reason that you can't modify an
    iterable while indexing it:
    """
    wordset_copy = dictionary_wordset.copy()
 
    """This bit cleans up the dictionary_set by removing single letters other
    than 'a' and 'I'. It then creates a second set of KnownProperNouns after
    removing them from the dictionary:
    """
    for word in wordset_copy:
        if len(word) == 1 and word != 'a' and word != 'I':
             dictionary_wordset.discard(word)
        if len(word) > 1 and word.istitle():
            dictionary_wordset.discard(word)
            KnownProperNouns.add(word)
 
    return (dictionary_wordset, KnownProperNouns)  # 2 sets with no intersections
 
 
def create_word_hist_for(text_file_path, dict_word_set, proper_nouns_in_dict,
                         start_trigger='', stop_trigger='',
                         split_n_list_compounds=True,
                         listing_proper_nouns=True,
                         listing_contractions=True,
                         removing_romans=True,  roman_maximux=1000):
    """ Creates a word frequency histogram from the input file
 
    Returns a dictionary with unique words as keys and their frequencies as
    found in the text as the value for that key. Removes all unwanted
    characters from the words. Only scans between the lines containing
    start_trigger and stop_trigger. If stop_trigger="" it scans to the EOF.
    """
    current_line_words = []
    word_freq_hist, in_text = dict(), False
    RomanNumList = []
    compounds_found, ContractionsUsed, proper_nouns_found = set(), set(), set()
 
    # checks for the most likely punctuation marks ',' and '.' first:
    punc_marks_to_split_with = list(string.punctuation[11:] +
                                    string.punctuation[:11])
    punc_marks_to_split_with.remove("'") # leave in apostrophes for contractions
    punc_marks_to_split_with.remove("-") # leave in hyphens for compounds
 
    with open(text_file_path, newline='') as File:
 
        if removing_romans:
            RomanNumList = GetRomanNumerals(roman_maximux)
 
        # start the analysis from beginning, without looking for a start string:`
        if not start_trigger:
            in_text = True
 
        for line in File:
            # this bit is skipped if the start_string is a null string:
            if not in_text:
                # YET - can only be here if start_trigger is set to something:
                if start_trigger not in line:
                    # then you still haven't found what you're looking for, Bono:
                    continue   # go to the next line of the text
                elif start_trigger in line:
                    # then you've found the first line of the body text:
                    in_text = True
                    # go to the next line of the text. Don't process this one:
                    continue
 
            if stop_trigger != "" and stop_trigger in line:
                # breaks out the current for-loop.
                # Stops reading the lines from the file:
                break
 
            elif not stop_trigger or stop_trigger not in line:  # Analyse the line
                #  Assumes the space char is the delimiter:
                current_line_words = line.split()
 
                for char_cluster in current_line_words:
                    multiple_words = []
                    char_cluster = ''.join(tidy_ends(list(char_cluster)))
 
                    if len(char_cluster) == 0:
                        continue
 
                    elif char_cluster.isalpha():
                        multiple_words.append(char_cluster)  # a list of one word
 
                    else:
                        if '--' in char_cluster:
                            # often found in  19th century English texts.
                            multiple_words = char_cluster.split('--')
 
                        elif '—' in char_cluster:
                            # a longer hyphen some printers use
                            # Not listed in string.punctuation for some reason:
                            multiple_words = char_cluster.split('—')
 
                        elif '-' in char_cluster:
                            char_cluster = char_cluster.lower()
                            char_cluster = clean_up(char_cluster)
                            if split_n_list_compounds:
                                compounds_found.add(char_cluster)
                                multiple_words = char_cluster.split('-')
                            else:
                                multiple_words.append(char_cluster) # a list of one word
 
                        elif "'" in char_cluster:
                            multiple_words.append(char_cluster) # a list of one word
 
                        else:
                            # algorithm is simply to split on the first punctuation
                            # mark found and delete the rest in clean_up():
                            for punc_mark in punc_marks_to_split_with:
                                if punc_mark in char_cluster:
                                    multiple_words = char_cluster.split(punc_mark)
                                    break
 
 
                    for word in multiple_words:
                        #  treat case as a list of words, even if it's just one,
                        # or one hyphenated word:
                        word = clean_up(word)
                        if len(word) == 0:
                            continue
 
                        """
                        This section decides whether to allow the word to
                        be added to the word frequency histogram. Words are
                        rejected with 'continue' based on simple criteria
                        of what makes a word. Word types the user has listed
                        separately, such as gerunds, are still counted in
                        the word frequency histogram:
                        """
                        if (len(word) == 1) and (word != 'I') and (word.lower() != 'a'):
                            """
                            Eliminates single letters other than <I>, <A>
                            and <a>, such as letters used in bullet points,
                            etc. This will also remove the Roman numerals
                            v/V and x/X:
                            """
                            continue   # don't count it in word_freq_hist below
 
    # Find all contractions:
                        if (word[:2] == "O'") or (word[:2] == "M'")  :
                            # you've found O'Neil, O'CONNOR, O'Brien, etc:
                            if word.isupper():
                                # takes care of O'CONNOR:
                                word = word[:3] + word[3:].lower()
                            proper_nouns_found.add(word)
                            if listing_proper_nouns:
                                continue # don't count it in word_freq_hist below
 
                        elif "'" in word and word[0] != 'I' :
                            # finds Didn't, DON'T, o'clock, Wouldn't, wouldn't:
                            # but not I've, I'd, I'm, I'll:
                            word = word.lower()
                            if listing_contractions:
                                # add it to the contraction count, but keep it in the analysis:
                                ContractionsUsed.add(word)
                                # continue
 
                        elif len(word) > 1 and word[0].lower() =='i' and word[1] == "'":
                            # You've found I've, I'd, I'm, I'll, even if the first
                            # letter is found in lowercase:
                            word = word.capitalize()
                            if listing_contractions:
                                # add it to the contraction count, but keep it in the analysis:
                                ContractionsUsed.add(word)
                                # continue
 
                        elif listing_contractions and "'" in word:
                            # cleanup() means it must be inside the word:
                            word = word.lower()
                            # add it to the contraction count, but keep it in the analysis:
                            if listing_contractions:
                                # add it to the contraction count, but keep it in the analysis:
                                ContractionsUsed.add(word)
                                # continue
 
     # Find all proper nouns:
                        elif removing_romans and (word.lower() in RomanNumList) and (word != 'I'):
                            # Need to check this before we do proper nouns:
                            continue # don't count it in word_freq_hist below
 
                        elif word in proper_nouns_in_dict: # among those found in the dictionary
                            #  picks up dictionary entries like <Grant> & <Abba> :
                            proper_nouns_found.add(word)
                            if listing_proper_nouns:
                                continue # don't count it in word_freq_hist below
 
                        elif word.isupper():
                            if word.lower() in dict_word_set:
                                word = word.lower()
                            else:
                                word = word.title()
                                # Must assume word is a proper noun
                                proper_nouns_found.add(word)
                                if listing_proper_nouns:
                                    continue # don't count it in word_freq_hist below
 
                        elif word.istitle() :
                            if word.lower() in dict_word_set:
                                word = word.lower()
                            else:  # Catches capitalized words unknown in lower case
                                # don't ignore <I>, even if you're listing_proper_nouns:
                                if listing_proper_nouns and len(word) > 1:
                                    proper_nouns_found.add(word)
                                    continue # don't count it in word_freq_hist below
 
                        elif word[0].isupper() and not word.istitle():
                            # Catches camelcase Scots surnames such as MacDonald, McNeil:
                            proper_nouns_found.add(word)
                            if listing_proper_nouns:
                                continue # don't count it in word_freq_hist below
 
                        # count all the words not filtered out:
                        word_freq_hist[word] = word_freq_hist.get(word, 0) + 1
 
    not_in_dict, compounds_found = CreateNotInList(word_freq_hist,
                    dict_word_set, split_n_list_compounds, compounds_found)
    File.close()
 
    return (word_freq_hist, not_in_dict, proper_nouns_found, compounds_found,
            ContractionsUsed)
 
 
def reverse_dict(input_dict):
    """ Takes an input dictionary and lists how many values had each key.
 
    """
    output_dict = dict()
    for key in input_dict:
        value = input_dict[key]
        if value not in output_dict:
            # output_dict[value] = key  # This should work, but it doesn't
            output_dict[value] = [key]
        else:
            output_dict[value].append(key)
    return output_dict
 
 
def PrintInitialSummary(text_name, SplitNListingCompounds,
                        ignore_n_list_propers, IgnoreNListContractions,
                        listing_archaisms, listing_adverbs, listing_gerunds,
                        CheckingSpelling, removing_Romans, RomanMaximus,
                        SortByAlpha):
    """Prints the summary of the analysis, listing all the options chosen.
 
    """
    output('\n\n\nANALYSIS of {}\n\nIn the following analysis of the above text:\n'.
           format(text_name))
 
    if ignore_n_list_propers:
        ProperNounInfo = "\n- Proper nouns have been listed separately and not "
        ProperNounInfo += "counted in the word frequency analysis or checked "
        ProperNounInfo += "against the dictionary. (-P)\n"
        output(ProperNounInfo)
    else:
        output("\n- Proper nouns have been counted in the word frequency analysis.\n")
 
    if listing_archaisms:
        ArchaismInfo = "\n- A list of possible linguistic archaisms the "
        ArchaismInfo += "author/translator may have used has been listed, but "
        ArchaismInfo += "also counted in the word frequency analysis. (-a)\n"
        output(ArchaismInfo)
 
    if IgnoreNListContractions:
        IgnoringContInfo = "\n- All contractions used by the author/translator "
        IgnoringContInfo += "have been listed, but also counted in the word "
        IgnoringContInfo += "frequency analysis. (-c)\n"
        output(IgnoringContInfo)
    else:
        IgnoringContInfo = "\n- All contractions used by the author/translator"
        IgnoringContInfo += " have been counted as words in the word frequency"
        IgnoringContInfo += " analysis.\n"
        output()
 
    if SplitNListingCompounds:
        CompoundInfo = "\n- All hyphenated compound words the author/translator"
        CompoundInfo += " has used have been listed but then split into their "
        CompoundInfo += "component parts for the word frequency analysis. (-H)\n"
        output(CompoundInfo)
    else:
        CompoundInfo = "\n- All hyphenated compound words the author/translator"
        CompoundInfo += " has used have been left unbroken and included in the "
        CompoundInfo += "word frequency analysis.\n"
        output(CompoundInfo)
 
    if listing_adverbs:
        AdverbInfo = "\n- Most adverbs the author/translator has used (those "
        AdverbInfo += "ending in 'ly') have been listed, as well as being "
        AdverbInfo += "counted in the word frequency analysis. (-y)\n"
        output(AdverbInfo)
 
    if listing_gerunds:
        GerundInfo = "\n- All gerunds and present tense continuous '-ing' "
        GerundInfo += "words used by the author/translator have been listed, "
        GerundInfo += "and also counted in the word frequency analysis. (-g)\n"
        output(GerundInfo)
 
    if removing_Romans:
        RomanInfo = "\n- All upper- and lower-case Roman numerals up to "
        RomanInfo += "{} have been ignored as words. (-R)\n".format(RomanMaximus)
        output(RomanInfo)
    else:
        output("\n- All upper- and lower-case Roman numerals have been counted as words.\n")
 
    if CheckingSpelling:
        CheckSpellInfo = "\n- A spell check will be performed on all the words"
        CheckSpellInfo += " used (except proper nouns and compound words if "
        CheckSpellInfo += "listed separately) against the dictionary of your "
        CheckSpellInfo += "choice.\n"
        output(CheckSpellInfo)
 
    if SortByAlpha:
        SortInfo = "\nThe word frequency analysis will take the form of an "
        SortInfo += "alphabetical list of the words used in the text, against "
        SortInfo += "the usage frequency of each. (-f)\n\n"
        output(SortInfo)
    else:
        SortInfo = "\nThe word frequency analysis will take the form of a list"
        SortInfo += " of the words used sorted by frequency, starting with the"
        SortInfo += " least frequent words.\n\n"
        output(SortInfo)
 
    output(65*'*')
    return
 
 
def PrintResultsFor(ThisList, SubsetName, WithChars=['']):
    """ Returns any elements of ThisList containing a regex listed in WithChars
 
    If the kwarg WithChars[] is not reassigned during the function call,
    the Regex defaults to '', which will always give a positive match in
    re.search(Regex, this_word), and print all of ThisList[]
    """
    ListSubset = set()
 
    for Regex in WithChars:
        for this_word in ThisList:
            if re.search(Regex, this_word):  # always gives a match for  Regex = ''
                ListSubset.add(this_word)
 
    if len(ListSubset) == 0:
        output('\n\nNo {}s were used.'.format(SubsetName))
    elif len(ListSubset) == 1:
        output('\n\nOnly one {} was used:   '.format(SubsetName))
        print_list_items(sorted(list(ListSubset)))
    else:
        output('\n\nThe following {:,} {}s were used:   '.
               format(len(ListSubset), SubsetName))
        print_list_items(sorted(list(ListSubset)))
    return
 
 
def PrintResultLists(text_name, vocab_list, not_in_dict, dict_wordset,
                     proper_nouns_found, compounds_used, contractions_found,
                     listing_proper_nouns=False, listing_archaisms=False,
                     ignore_n_list_contractions=False,
                     listing_and_splitting_compounds=False,
                     listing_adverbs=False, listing_gerunds=False,
                     checking_spelling=False, remove_romans=True,
                     greatest_roman=100, sorting_by_alpha=True):
    """Prints out the various lists of results, based on user options
    """
    PrintInitialSummary(text_name, listing_and_splitting_compounds,
                     listing_proper_nouns, ignore_n_list_contractions,
                     listing_archaisms, listing_adverbs, listing_gerunds,
                     checking_spelling,remove_romans, greatest_roman,
                     sorting_by_alpha)
 
    if listing_proper_nouns:
        PrintResultsFor(list(proper_nouns_found), '(probable) proper noun')
 
    if listing_archaisms:
        """ Checketh for early 17th century Bible English that English
        translators loveth to pepper their works with and giveth it that
        Olde Feele:
        """
        ArchaismList = [r"eth\b", r"dst\b", r"rst\b", r"ert\b", r"est\b"]
        PrintResultsFor(set(not_in_dict), '(probable) linguistic archaism',
                        WithChars=ArchaismList)
 
    if ignore_n_list_contractions:
        PrintResultsFor(contractions_found, 'contraction') # print the whole list
 
    if listing_and_splitting_compounds:
        PrintResultsFor(compounds_used, 'compound word') # print the whole list
 
    if listing_adverbs:
        # RE counts words ending in -ly that may also be contractions and compounds:
        PrintResultsFor(vocab_list, '(mostly) adverb', WithChars=[r"[a-z'-]{3,}ly\b"])
 
    if listing_gerunds:
        PrintResultsFor(vocab_list, '(probable) present tense continuous verbs and gerund',
                        WithChars=[r'[a-z]{3,}ings?\b'])
 
    if checking_spelling:
        if ignore_n_list_contractions:
            not_in_dict -= contractions_found   # set subtraction
        output('\n\nThe following {:,} words were not found in a dictionary of {:,} entries:  '.
               format(len(not_in_dict), len(dict_wordset)))
        print_list_items(sorted(not_in_dict))
    return
 
 
def CreateNotInList(word_histogram, DictWordSet, SplitAndListCompounds, CompoundsFound):
    """ Sort the words not found in the dictionary
    """
    NotInDict = set()
    histo_copy = word_histogram.copy()
    for word, freq in histo_copy.items():
        if word not in DictWordSet:
            # create list of words not in dictionary:
            if SplitAndListCompounds and '-' in word:
               # one that got away earlier if '--' or '—' was in the line
               CompoundsFound.add(word)
               del word_histogram[word]  # remove compound word from word hist
            else:
                NotInDict.add(word)
    return NotInDict, CompoundsFound
 
 
def PrintWordHistogram(TextName, WordHistogram, AlphaSort):
    """ Print the output of the analysis
 
    """
    RevWordHistogram, FreqList = dict(), []
    output('\n\n\nWord Frequency Analysis\n')
 
    if AlphaSort:  # condensed frequency histogram output
        output("\nBelow is a sorted list of the author/translator's lexicon, with word frequencies, of their work {}:\n".
               format(TextName))
        sorted_hist = sorted(WordHistogram)
        for word in sorted_hist:
            output('{0}({1}) '.format(word, WordHistogram[word]))
 
    else:  # long verbose output, sorting words into frequencies:
        RevWordHistogram = reverse_dict(WordHistogram)  # frequencies are now the keys
        FreqList = list(RevWordHistogram) # a list of the keys (freqs), discarding the values (words)
        FreqList.sort(reverse=True)  # a list of the freqs, in ascending order.
 
        output('\nBelow is a word frequency analysis of {}. '.format(TextName))
        output('Starting from the least common words in the text:')
 
        for i in range(len(FreqList)-1, -1, -1):  # count backwards from the last item:
            if FreqList[i] == 1:  # words that appear only once
                output('\n\nThe following {:,} words appear only once: '.format(
                len(RevWordHistogram[FreqList[i]])))
 
            elif FreqList[i] == 2:  # words that appear only twice:
                output('\n\nThe following {:,} words appear only twice:   '.format(
                len(RevWordHistogram[FreqList[i]])))
 
            elif len(RevWordHistogram[FreqList[i]]) == 1:
                # common words that don't share their count with other words:
                output('\n\nThis word appears a total of {:,} times:   '.format(
                FreqList[i]))
 
            else:   #  multiple words sharing their count with other words
                output('\n\nThe following {:,} words each appear {:,} times:  '.format(
                len(RevWordHistogram[FreqList[i]]), FreqList[i]))
 
            print_list_items(sorted(RevWordHistogram[FreqList[i]]))
 
    TotalWordsUsed = sum(WordHistogram.values())
    vocab_size = len(WordHistogram)
    output('\n\n\nIn this text of {:,} words, the author/translator of {} used a total vocabulary of {:,} words.\n\n'.
           format(TotalWordsUsed, TextName, vocab_size))
    return
 
 
def analyse_this(TextFilePath, DictPath, SortByAlpha=True,
                 StartTrigger="", StopTrigger="", CheckingSpelling=True,
                 SplitAndListCompounds=True, ListingArchaisms=True,
                 IgnoreNListProperNouns=True, ListingContractions=True,
                 ListingAdverbs=True, ListingGerunds=True,
                 RemovingRomans=True, RomanMaximus=1000):
    """ Perform a textual analysis, as defined by the user.
    """
    word_histogram, VocabList = dict(), []
    DictWordSet, ProperNounsInDict, ProperNounsFound = set(), set(), set()
    CompoundsFound, ContractionsFound, NotInDict = set(), set(), set()
 
    """Need to reset this explicitly as a workaround for data persistence
    between calls to this function from an external module, such as a GUI
    front end:
    """
    global result_string
    result_string = ''
 
    """ These return sets, not dicts. These 2 sets have no intersections.
    Would benefit from pickling for data persistence, instead of recreating it
    every time: """
    DictWordSet, ProperNounsInDict = CreateDictionarySet(DictPath)
 
 
    (word_histogram, NotInDict, ProperNounsFound, CompoundsFound, ContractionsFound) = \
    create_word_hist_for(TextFilePath, DictWordSet, ProperNounsInDict,
                    start_trigger=StartTrigger, stop_trigger=StopTrigger,
                    split_n_list_compounds=SplitAndListCompounds,
                    listing_proper_nouns=IgnoreNListProperNouns,
                    listing_contractions=ListingContractions,
                    removing_romans=RemovingRomans,
                    roman_maximux=RomanMaximus)
 
 
    VocabList = list(word_histogram.keys())
    text_path, TextName = os.path.split(TextFilePath)
 
    PrintResultLists(TextName, VocabList, NotInDict, DictWordSet,
                     ProperNounsFound, CompoundsFound, ContractionsFound,
                     listing_proper_nouns=IgnoreNListProperNouns,
                     listing_archaisms=ListingArchaisms,
                     ignore_n_list_contractions=ListingContractions,
                     listing_and_splitting_compounds=SplitAndListCompounds,
                     listing_adverbs=ListingAdverbs,
                     listing_gerunds=ListingGerunds,
                     checking_spelling=CheckingSpelling,
                     remove_romans=RemovingRomans,
                     greatest_roman=RomanMaximus,
                     sorting_by_alpha=SortByAlpha)
 
    PrintWordHistogram(TextName, word_histogram, SortByAlpha)
 
    if __name__ == "__main__":
        # Output already printed:
        return
    else:
        # code was imported by another program:
        return result_string
 
 
def usage(progname):
    """Prints a short command line guide.
    """
    output("""\nUsage: from the command line type:
    {} -i <input_file> [-s <start_string>] [-e <end_string>] [-D <your_dict_filepath>]
    [-R <N>] [-cadfghyHPt] [> output_file]
 
    -i rel_path/input_file
        Mandatory flag
 
Optional flags (in order of typical usage):
    -s "start trigger text"
 
    -e "end trigger text"
 
    -d  Check all words against the program's built-in dictionary, listing
        those not in the dictionary. Default is not to spellcheck.
 
    -D rel_path/Dictionary
        Use a different dictionary. Overrides '-d'.
 
    -P  summarise proper nouns in a separate list from the analysis.
 
    -H  List separately all hyphenated compound words used.
 
    -a  list archaisms uses.
 
    -c  List all contractions used.
 
    -g  List all gerunds and present tense continuous words used.
 
    -y  List all adverbs ending in '-ly'.
 
    -R <N>
        Ignore Roman numerals up to maximum N
 
    -f  Print alphabetically sorted word list with frequencies.
 
    -t  Time the running of the program, time stamping the output file/stream
        with how long the analysis took.
 
    -h  Help: prints a long version of this guide.\n\n""".format(progname))
 
    return
 
 
def main(argv):
    """Interprets the command line, turning flags into variables
    """
    # The flags you want to pass to your program:
    timing, spellcheck = False, False
    ignore_n_list_propers, split_and_list_hyphenates = False, False
    list_contractions, list_archaisms = False, False
    listing_adverbs, listing_gerunds = False, False
    alpha_sort_output = False
    remove_romans, roman_maximus = False, 0
    input_file_path = ''
    analysis_start_trig = analysis_stop_trig = ""
    dictionary_path = './EnglishDictionary.txt'
 
    # Nice trick to get the name of this program:
    path, ProgName = os.path.split(argv[0])
 
    try:
        """ This is where you tell Python about all the valid flags for your
        program. If the flag isn't here, your code should handle it as a
        command line error. A colon after the letter tells it to look for an
        associated value with the flag, e.g.
            -L French
        If there's no associated value, again, your main() code is where you
        handle it. Letters not followed by colons do not need values, and can
        either be listed individually, as in
 
            Analyse this -a -f -g -H
 
        or together, as in
 
            Analyse this -afgH
 
        and getopt() will work it out. It can also handle --linux flags, but
        these have not been implemented here:
        """
        opts, args = getopt.getopt(argv[1:], "i:s:e:D:R:acdfghyHPt")
 
    except getopt.GetoptError as err:
        print('\n', str(err))
        usage(ProgName)
        sys.exit(2)
 
    for opt, arg in opts:
        if opt == '-i':
            input_file_path = arg
        elif opt == '-s':
            analysis_start_trig = arg
        elif opt == '-e':
            analysis_stop_trig = arg
        elif opt == '-f':
            alpha_sort_output = True
        elif opt == '-D':  # use the user's own named dictionary file
            spellcheck = True
            dictionary_path = str(arg)
        elif opt == '-a':
            list_archaisms = True
        elif opt == '-c':
            list_contractions = True
        elif opt == '-d':  # use the program's internal dictionary
            spellcheck = True
        elif opt == '-g':
            listing_gerunds = True
        elif opt == '-h':
            print('\n\n' + ProgName, '\n', __doc__)
            sys.exit(2)
        elif opt == '-H':
            split_and_list_hyphenates = True
        elif opt == '-P':
            ignore_n_list_propers = True
        elif opt == '-y':
            listing_adverbs = True
        elif opt == '-R':
            remove_romans = True  # what did they ever do for us?
            roman_maximus = int(arg)
        elif opt == '-t':
            timing = True
            start = timeit.default_timer()
        else:
            assert False, "unhandled option"
 
    if not input_file_path:
        output("\nCommand line error: requires '-i' flag with the input file name & path.\n")
        usage(ProgName)
        sys.exit(2)
 
    input_files = [input_file_path, dictionary_path]
    for file in input_files:
        try:  # check the user's input files are there before proceeding:
            f = open(file, 'r')
        except IOError:
            print ('\nFilename error: no such file: {}\n'.format(file))
            sys.exit(2)  # (Unix convention: 0=no problem, 1=error, 2=cmdline)
        else:
            f.close()
 
    analyse_this(input_file_path, dictionary_path, SortByAlpha=alpha_sort_output,
                 StartTrigger=analysis_start_trig,
                 StopTrigger=analysis_stop_trig, CheckingSpelling=spellcheck,
                 SplitAndListCompounds=split_and_list_hyphenates,
                 ListingArchaisms=list_archaisms,
                 IgnoreNListProperNouns=ignore_n_list_propers,
                 ListingContractions=list_contractions,
                 ListingAdverbs=listing_adverbs,
                 ListingGerunds=listing_gerunds,
                 RemovingRomans=remove_romans, RomanMaximus=roman_maximus)
    if timing:
        stop = timeit.default_timer()
        output('\nThis textual analysis took {} seconds.\n'.format(round(stop - start, 2)))
    return
 
 
def print_cmd_line(args):
    """recreates the command line and prints it out
 
    This recreates the command line as a reference header in the output file,
    to allow the user to reproduce his/her results at a later date. Note that
    since this is called from within __main__, it will not be called if this
    program has been imported as a module from another program, such as a GUI
    front end, which is OK since avoiding a command line is one of the main
    reasons for using a GUI.
    """
    arg_list = []
    path, progname = os.path.split(args[0])
    arg_list += [progname]
    for item in args[1:]:
        if '-' not in item:     # item is therefore either a string or a positive number
            try:
                int(item)   # eliminates integer flags (can easily be changed to floats)
            except ValueError:
                item = '"' + item + '"' # put quotes around anything that isn't a flag or a number
        arg_list.append(item)
    command_line = ' '.join(arg_list) # recreates the command line
    print ('\nThe following results were obtained using the command line:\n' + command_line)
    return
 
 
if __name__ == "__main__":
    print_cmd_line(sys.argv)
    main(sys.argv)

