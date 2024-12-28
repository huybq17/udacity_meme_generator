"""Define IngestorInterface Class."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An abstract class for parsing file content."""

    added_extension = []

    @classmethod
    def do_ingest(cls, path: str) -> bool:
        """Check if the file has a supported extension."""
        ex = path.split('.')[-1]
        return ex in cls.added_extension

    # @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file content and return a list of QuoteModel objects."""
        pass
