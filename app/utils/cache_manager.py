import time

class CacheManager:

    def __init__(self):
        self.cache = {}
        self.expiry = 60   # seconds

    def get(self, key):

        if key in self.cache:

            data, timestamp = self.cache[key]

            if time.time() - timestamp < self.expiry:
                return data

        return None

    def set(self, key, value):

        self.cache[key] = (value, time.time())
