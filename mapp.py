#import nltk
#nltk.download()
import pandas as pd
import os
import re
import csv
import numpy as np
from nltk.corpus import wordnet as wn
print("start")
listnames = []

for i,j in enumerate(wn.synsets('music')):
    listnames.append(j.lemma_names())
#print (listnames)
import pandas as pd 
df = pd.read_csv('third.csv', encoding='utf-8')
df1 = df.drop_duplicates(['v_title'])
#print(df1)
#print(df1.shape)
       