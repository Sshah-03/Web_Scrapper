import redis
import json
import os
from config import CACHE_TYPE, REDIS_HOST, REDIS_PORT, CACHE_TTL

class CacheManager:

    def __init__(self):
        if CACHE_TYPE == "redis":
            self.client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        else:
            self.cache_file = "cache.json"
            if not os.path.exists(self.cache_file):
                with open(self.cache_file, "w") as f:
                    json.dump({}, f)

    def get(self, key):
        if CACHE_TYPE == "redis":
            return self.client.get(key)
        else:
            with open(self.cache_file, "r") as f:
                data = json.load(f)
            return data.get(key)

    def set(self, key, value):
        if CACHE_TYPE == "redis":
            self.client.setex(key, CACHE_TTL, value)
        else:
            with open(self.cache_file, "r") as f:
                data = json.load(f)
            data[key] = value
            with open(self.cache_file, "w") as f:
                json.dump(data, f)
