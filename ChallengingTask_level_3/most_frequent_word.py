#! /usr/bin/env python

import sys
import os
import re

word_dict = {}  #main dict to store words, {word:{frequency, files, sentences}}
max_freq = 0
most_common_words = []

usage_message = '''
        Usage: frequency.py -d dir_names or -f file_names
        Examples:
            python frequency.py -d .      - read all files form the current directory
            python frequency.py -d  d1 d2 - read all files from directory d1 and d2
            python frequency.py -f  f1 f2 - read file f1 and file f2
            '''


def split_file_to_sentences(file_content):
    file_content = ' '.join(file_content.splitlines())
    return re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s",file_content)



def split_sentence_to_words(sentence):
    return re.findall(r"\b[a-zA-Z\-']+\b", sentence)


def update_word_dict(word, file, sentence):
    word = word.lower()
    if word not in word_dict:
        word_dict[word] = {'frequency': 1, 'file_names': {file}, 'sentences': {sentence}}
    else:
        word_dict[word]['frequency'] += 1
        word_dict[word]['file_names'].add(file)
        word_dict[word]['sentences'].add(sentence)
    find_highest_frequency(word)


def find_highest_frequency(word):
    global max_freq, most_common_words
    if word_dict[word]['frequency'] > max_freq:
        max_freq = word_dict[word]['frequency']
        most_common_words = [word]
    elif word_dict[word]['frequency'] == max_freq:
        most_common_words.append(word)


def get_data_from_file(file_name):
    try:
        with open(file_name, 'r', errors='backslashreplace', encoding='utf-8') as document:
            sentences = split_file_to_sentences(document.read())
            for sentence in sentences:
                word_table = split_sentence_to_words(sentence)
                for word in word_table:
                    update_word_dict(word, file_name, sentence)
        document.close()
    except IOError as e:
        print(e)


def print_highest_frequency():
    for word in most_common_words:
        print("\nThe most common word is: " + word)
        print("---------------------------------------")
        print("Files containing the word: ")
        for file in word_dict[word]['file_names']:
            print(os.path.basename(file))
        print("---------------------------------------")
        print("Sentences containing the word: ")
        for sentence in word_dict[word]['sentences']:
            print(sentence.strip())
        print("\n")


def main():
    if len(sys.argv) < 3:
        print(usage_message)
    else:
        if sys.argv[1] == '-d':
            for dir_path in sys.argv[2:]:
                dir_path = os.path.abspath(dir_path)
                for file_name in os.listdir(dir_path):
                    get_data_from_file(os.path.join(dir_path, file_name))
        elif sys.argv[1] == '-f':
            for file_path in sys.argv[2:]:
                get_data_from_file(file_path)
        else:
            print(usage_message)
    print_highest_frequency()


main()