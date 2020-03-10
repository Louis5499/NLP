#!/usr/bin/env python
# coding: utf-8

import math, re
from collections import Counter


# tokenize text and get words list
def words(text): return re.findall(r'\w+', text.lower())


# get all bigrams
def bigrams(text):
    splitText = [b for b in zip(text.split(" ")[:-1], text.split(" ")[1:])]
    # print(splitText)
    return splitText


# these are word-level 1-grams(unigram) and 2-grams(bigram)
# count of the number of times they appeared
uni_count = Counter(words(open('big.txt').read()))
bi_count = Counter(bigrams(open('big.txt').read()))
uni_N = sum(uni_count.values())
bi_N = sum(bi_count.values())
def Bi_P(bigram): return bi_count[bigram] + 1 / bi_N + V # float

# ==Format==
# call add1_smooth("He is") or add1_smooth(("He", "is")) something like that...
# retrun 1.306 (probability with add one smooth)
V = len(list(uni_count.keys()))
def add1_smooth(bigram):
    print(bigram, Bi_P(bigram))
    return (bi_count[bigram] + 1) / (bi_N + V)
    # return Bi_P(bigram)

# ==Format==
# call sentence_prob("He is looking a new job.")
# retrun -33.306 (sentence probability)
def sentence_prob(sentence):
    probability = 0.0
    splitBigrams = [b for b in zip(sentence.split(" ")[:-1], sentence.split(" ")[1:])]
    for i in range(len(splitBigrams)):
        probability += math.log(add1_smooth(splitBigrams[i]))
    
    return probability


if __name__ == "__main__":
    lm1 = sentence_prob("Are you interested about your offer for Marketing Assistant.")
    lm2 = sentence_prob("Are you interested in your offer for Marketing Assistant.")
    lm3 = sentence_prob("He is looking to a new job.")
    lm4 = sentence_prob("He is looking for a new job.")
    print(lm1)
    print(lm2)
    print(lm3)
    print(lm4)