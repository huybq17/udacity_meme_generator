"""Define csv_ingestor Class."""
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import pandas


class csv_ingestor(IngestorInterface):
    """Parse separated value files using pandas."""

    added_extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a csv file and return a list of QuoteModel objects."""
        if not cls.do_ingest(path):
            raise ValueError(f"Unsupported file extension for {path}")

        comments = []

        try:
            temp = pandas.read_csv(path)
            comments = [QuoteModel(row['author'], row['body'])
                        for _, row in temp.iterrows()]
        except (FileNotFoundError, pandas.errors.ParserError) as e:
            raise ValueError(f"Unable to parse file {path}, {e}") from e

        return comments
