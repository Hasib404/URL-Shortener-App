class URLShortenerService:
    def __init__(self, url, key):
        self.url = url
        self.unique_key = key
    
    def shorten_url(self):
        base_url = 'tier.app'
        return base_url + '/' + self.unique_key

