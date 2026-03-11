from abc import ABC, abstractmethod


class BaseScraper(ABC):

    @abstractmethod
    async def fetch(self):
        pass
