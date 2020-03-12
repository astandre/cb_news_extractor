import re


def classify_post(post):
    return True


def find_urls(raw_input):
    regex_url = re.compile("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")
    url = regex_url.findall(raw_input)
    return url


def find_tag(raw_input):
    tag = None
    if "|" in raw_input:
        tag, raw_input = raw_input.split("|")
    return tag


def clean_input(raw_input):
    raw_input = re.sub(' +', ' ', raw_input)
    raw_input = raw_input.lstrip()
    raw_input = raw_input.rstrip()
    return raw_input
