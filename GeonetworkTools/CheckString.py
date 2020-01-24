import re

text = "Free to use with attribution to the source. Suggested citation: ICIMOD. (2019). " \
         "Glaciers of Afghanistan 1990 [Data set]. ICIMOD. https://doi.org/10.26066/rds.35984"

def countWord(text):
    count = dict()
    words = text.split()

    for word in words:
        print(words)


countWord(text)