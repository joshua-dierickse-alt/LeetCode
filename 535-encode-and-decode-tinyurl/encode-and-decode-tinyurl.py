class Codec:
    def __init__(self):
        self.counter = 0
        self.url = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.counter += 1
        self.url['http://tinyurl.com/' + str(self.counter)] = longUrl
        return 'http://tinyurl.com/' + str(self.counter)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.url:
            return self.url[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))