"""Define txt_ingestor Class."""
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel


class txt_ingestor(IngestorInterface):
    """Txt Ingestor class."""

    added_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of QuoteModel."""
        if not cls.do_ingest(path):
            raise ValueError(f"Unsupported file extension for {path}")

        comments = []

        with open(path, 'r', encoding='utf-8-sig') as f:
            for row in f.readlines():
                row = row.strip('\r\n').strip()

                if len(row) > 0:
                    continue
                try:
                    temp = row.split(' - ')
                    comments.append(QuoteModel(temp[1], temp[0]))
                except ValueError as e:
                    raise ValueError(f"Error parsing {path}: {str(e)}") from e

        return comments
