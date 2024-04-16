class Codec:
    def __init__(self):
        self.short_long = {}
        self.long_short = {}
        self.pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        import random
        while longUrl not in self.long_short:
            code = "".join(random.choices(self.pool, k = 6))
            if code not in self.short_long:
                self.long_short[longUrl] = code
                self.short_long[code] = longUrl
        return f'http://tinyurl.com/{self.long_short[longUrl]}'
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_long[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
