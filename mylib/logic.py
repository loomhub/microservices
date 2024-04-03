import wikipedia  # type: ignore


def wiki(name="Biology", length=1):
    my_wiki = wikipedia.summary(name, length)
    return my_wiki
