import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Grabbing some lovely Hitler quotes
hitler_urls = [f"https://libquotes.com/adolf-hitler/{i}" for i in range(1, 13)]

def grab_hitler(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    # Find all <a> tags with class 'quote_link'
    quote_links = soup.find_all("a", {"class": "quote_link"})

    # Iterate over each <a> tag
    for quote_link in quote_links:
        if quote_span := quote_link.find("span", {"class": "quote_span"}):
            yield quote_span.get_text().strip().replace("\"", "")

if os.path.exists('hitler_quotes.csv'):
    df_hitlers = pd.read_csv('hitler_quotes.csv')
    hitlers = df_hitlers['Quotes'].tolist()
else:
    hitlers = []
    for url in hitler_urls:
        new_hitlers = list(grab_hitler(url))
        hitlers.extend(new_hitlers)
    df_hitlers = pd.DataFrame(hitlers, columns=['Quotes'])
    df_hitlers = df_hitlers.drop_duplicates()
    hitlers = df_hitlers['Quotes'].tolist()
    df_hitlers.to_csv('hitler_quotes.csv', index=False)
