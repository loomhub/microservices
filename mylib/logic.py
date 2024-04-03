import wikipedia  # type: ignore


def wiki(name="Biology", length=1):
    myWiki = wikipedia.summary(name, length)
    return myWiki
