import wikipedia  # type: ignore
from textblob import TextBlob

def wiki(name="Biology", length=1):
    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    result=wikipedia.search(name)
    return result

def phrases(name):
    page=wiki(name)
    blob=TextBlob(page)
    result=blob.noun_phrases
    return result