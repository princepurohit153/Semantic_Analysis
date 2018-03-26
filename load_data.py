import os
import nltk
from nltk.tokenize import *

from io import open

log_file='./logs.txt'
f_logs = open(log_file, 'w')


def strip_quotations_newline(text):
    text = text.rstrip()
    if text[0] == '"':
        text = text[1:]
    if text[-1] == '"':
        text = text[:-1]
    return text

def expand_around_chars(text, characters):
    for char in characters:
        text = text.replace(char, " "+char+" ")
    return text

def split_text(text):
    text = strip_quotations_newline(text)
    text = expand_around_chars(text, '".,()[]{}:;')
    splitted_text = text.split(" ")
    cleaned_text = [x for x in splitted_text if len(x)>1]
    text_lowercase = [x.lower() for x in cleaned_text]
    return text_lowercase


def amazon_reviews():
    datafolder = './amazon/'
    files = os.listdir(datafolder)
    Y_train, Y_test, X_train, X_test,  = [], [], [], []
    for file in files:
        # if(file!='pos'):
        if(1):
            f = open(datafolder + file, 'r', encoding="utf8")
            label = file
            lines = f.readlines()
            no_lines = len(lines)

            f_logs.write('filestar= ' + file+'\n')

            no_training_examples = int(0.7*no_lines)
            for index,line in enumerate(lines[:no_training_examples]):
                Y_train.append(label)
                if(index== 0):
                    print(line)
                    print(split_text(line))
                    assign_post_tags(line)
                f_logs.write('index= '+ str(index)+'\n')
                # X_train.append(split_text(line))

                X_train.append(assign_post_tags(' '.join(split_text(line))))
            for line in lines[no_training_examples:]:
                Y_test.append(label)
                # X_test.append(split_text(line))
                X_test.append(assign_post_tags(' '.join(split_text(line))))
            f.close()

            f_logs.write('fileend= '+ file+'\n')

    return X_train, Y_train, X_test, Y_test


def assign_post_tags(text):
    # text = word_tokenize("And now for something completely different")


    text = word_tokenize(text)
    p= nltk.pos_tag(text)
    ret = [i[1] for i in p]
    # print(text)
    # print(p)
    # print(ret)
    f_logs.write(' '.join(ret))
    f_logs.write('\n')
    # print(p)
    # [print(i[1],end=' ') for i in p]
    # print()
    return ret
    #
    # [('And', 'CC'), ('now', 'RB'), ('for', 'IN'), ('something', 'NN'),
    #  ('completely', 'RB'), ('different', 'JJ')]

