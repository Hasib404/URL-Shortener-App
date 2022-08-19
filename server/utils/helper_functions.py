import re

def is_valid_url(url):
    ''' Regex to check if URL is valid '''

    pattern = ("((http|https)://)(www.)?" +
            "[a-zA-Z0-9@:%._\\+~#?&//=]" +
            "{2,256}\\.[a-z]" +
            "{2,6}\\b([-a-zA-Z0-9@:%" +
            "._\\+~#?&//=]*)")
    
    regex_compiler = re.compile(pattern)

    if (url == None):
        return False

    if(re.search(regex_compiler, url)):
        return True
    else:
        return False