class SimpleHash:
    def hash(self, text):
        h = 0
        for ch in text:
            h = (h * 31 + ord(ch)) % 1000000007
        return str(h)
