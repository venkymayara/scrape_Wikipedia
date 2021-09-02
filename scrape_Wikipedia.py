# pip install wikipedia


import wikipedia as wiki


print(wiki.search("Robert Downey Jr"))


print(wiki.suggest("Robert"))


print(wiki.summary("Robert Downey Jr"))


wiki.set_lang("fr")
print(wiki.summary("Robert Downey Jr"))


wiki.set_lang("en")
p = wiki.page("Robert Downey Jr")


print(dir(p))



# To get the Title:
print("Title:", p.title)


# To get the url of the article:
print("URL:", p.url)


# To scrape the full article:
print("Content:", p.content)


#To get all the images in the article:
print(p.images)


# And to get all the referals used by Wikipedia in the article:
print(p.links)
