import time

class RateLimiter:

    def __init__(self):
        self.requests = []
        self.limit = 5
        self.window = 60

    def allow(self):

        now = time.time()

        self.requests = [
            req for req in self.requests
            if now - req < self.window
        ]

        if len(self.requests) >= self.limit:
            return False

        self.requests.append(now)

        return True
