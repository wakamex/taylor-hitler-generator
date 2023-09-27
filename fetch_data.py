import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from cc_markov import MarkovChain

#Grabbing some taylor lyrics from the taylor-swift-lyrics repo
df = pd.read_csv('taylor-swift-lyrics/songs.csv')
lyrics_list = df['Lyrics'].tolist()

#Grabbing some lovely Hitler quotes
hitler_urls = ["http://www.brainyquote.com/quotes/authors/a/adolf_hitler.html"]

mc = MarkovChain()

def grab_hitler(url):
    request = requests.get(url)
    content = request.text
    soup = BeautifulSoup(content, "html.parser")
    results = soup.find_all('span','bqQuoteLink')
    for result in results:
        yield result.get_text()

for lyric in lyrics_list:
    mc.add_string(lyric)

output =  mc.generate_text(max_length=20)
print("PRE HITLER LYRICS: ")
print(" ".join(output))

if os.path.exists('hitler_quotes.csv'):
    df_hitlers = pd.read_csv('hitler_quotes.csv')
    hitlers = df_hitlers['Quotes'].tolist()
else:
    hitlers = list(grab_hitler(hitler_urls[0]))
    df_hitlers = pd.DataFrame(hitlers, columns=['Quotes'])
    hitlers = df_hitlers['Quotes'].tolist()
    df_hitlers.to_csv('hitlers_quotes.csv', index=False)

for hitler in hitlers:
    mc.add_string(hitler)
    

h_output =  mc.generate_text(max_length=20)
print("POST HITLER LYRICS: ")
print(" ".join(h_output))