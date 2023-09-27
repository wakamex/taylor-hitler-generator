import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from cc_markov import MarkovChain
from hitler import hitlers

#Grabbing some taylor lyrics from the taylor-swift-lyrics repo
df = pd.read_csv('taylor-swift-lyrics/songs.csv')
lyrics_list = df['Lyrics'].tolist()

mc = MarkovChain()

for lyric in lyrics_list:
    mc.add_string(lyric)

output =  mc.generate_text(max_length=20)
print("PRE HITLER LYRICS: ")
print(" ".join(output))

for hitler in hitlers:
    mc.add_string(hitler)

h_output =  mc.generate_text(max_length=20)
print("POST HITLER LYRICS: ")
print(" ".join(h_output))