import requests
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
from markov_python.cc_markov import MarkovChain

#Grabbing some taylor lyrics from the web
taytay_urls = ["http://www.metrolyrics.com/you-belong-with-me-lyrics-taylor-swift.html",
        "http://www.metrolyrics.com/out-of-the-woods-lyrics-taylor-swift.html",
        "http://www.metrolyrics.com/wildest-dreams-lyrics-taylor-swift.html",
        "http://www.metrolyrics.com/everything-has-changed-lyrics-taylor-swift.html",
        "http: // www.metrolyrics.com / mean - lyrics - taylor - swift.html",
        "http://www.metrolyrics.com/i-knew-you-were-trouble-lyrics-taylor-swift.html",
        "http://www.metrolyrics.com/back-to-december-lyrics-taylor-swift.html"]

#Grabbing some lovely Hitler quotes
hitler_urls = ["http://www.brainyquote.com/quotes/authors/a/adolf_hitler.html"]

mc = MarkovChain()

def grab_taytay(url):
    request = requests.get(url)
    content = request.text
    soup = BeautifulSoup(content, "html.parser")
    comments = soup.find_all(id="mid-song-discussion")
    for comment in comments:
        comment.extract()
    return soup.find_all(id="lyrics-body-text")[0].get_text()

def grab_hitler(url):
    request = requests.get(url)
    content = request.text
    soup = BeautifulSoup(content, "html.parser")
    results = soup.find_all('span','bqQuoteLink')
    for result in results:
        yield result.get_text()

for url in taytay_urls:
    mc.add_string(grab_taytay(url))

output =  mc.generate_text(max_length=20)
print "PRE HITLER LYRICS: "
print " ".join(output)

hitlers = grab_hitler(hitler_urls[0])
for hitler in hitlers:
    mc.add_string(hitler)

h_output =  mc.generate_text(max_length=20)
print "POST HITLER LYRICS: "
print " ".join(h_output)

