from flask import Flask, render_template

import pickle

import numpy as np
import pandas as pd

import pickle

import numpy as np
import pandas as pd

import random
from collections import defaultdict
from textblob import TextBlob

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier


pd.options.display.max_colwidth = 1000
lyric = pd.read_csv('radiohead.csv', engine = 'python')
lyric.fillna('', inplace=True)

def markov_chain(text):

    words = text.split(' ')
    
    m_dict = defaultdict(list)
    
    for current_word, next_word in zip(words[0:-1], words[1:]):
        m_dict[current_word].append(next_word)

    m_dict = dict(m_dict)
    return m_dict


def text_gen(chain, count = 40):
    
    w1 = random.choice(list(chain.keys()))
    sentence = w1.capitalize()
    
    for i in range(count - 1):
        w2 = random.choice(chain[w1])
        w1 = w2
        sentence += ' ' + w2 
        
    return(sentence)

def rh_song_gen(album_name):

    text = str(lyric[lyric['album_name'] == album_name].lyrics)

    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    text_filtered = ''.join(filter(whitelist.__contains__, text))
    text_filtered = " ".join(text_filtered.split())

    text_dict = markov_chain(text_filtered)
    
    return text_gen(text_dict)


