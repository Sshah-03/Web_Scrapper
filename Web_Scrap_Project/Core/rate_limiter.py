import asyncio
import time
from functools import wraps
from config import RATE_LIMIT

last_called = 0

def rate_limiter():
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            global last_called
            elapsed = time.time() - last_called
            wait_time = max(0, (1 / RATE_LIMIT) - elapsed)
            if wait_time > 0:
                await asyncio.sleep(wait_time)
            last_called = time.time()
            return await func(*args, **kwargs)
        return wrapper
    return decorator