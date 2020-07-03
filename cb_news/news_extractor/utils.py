import re


def classify_post(post):
    print('Clasifiying ', post)
    tag = find_tag(post)
    print('Tag ', tag)
    resp = ''
    if '[Pᴜʙʟɪᴄɪᴅᴀᴅ]' in post:
        resp = 'publicidad'

    if tag == '#MásHistoriasQueContar':
        resp = 'historia'
    return resp


def find_urls(raw_input):
    regex_url = re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")
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
