"""An investor class that implements the IngesterInterface.

* It is abstract base class and encapsulates your helper classes.
* A file type-based logic should be implemented to select
    the appropriate helper for a given file.
"""
from typing import List
from .QuoteModel import QuoteModel
from .txt_ingestor import txt_ingestor
from .csv_ingestor import csv_ingestor
from .doc_ingestor import doc_ingestor
from .pdf_ingestor import pdf_ingestor
from .IngestorInterface import IngestorInterface


class Ingestor(IngestorInterface):
    """General Ingestor encapsulates all specific ingestors."""

    ingestors = [txt_ingestor, csv_ingestor, doc_ingestor, pdf_ingestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select a proper ingestor & parse contents."""
        for importer in cls.ingestors:
            if importer.do_ingest(path):
                return importer.parse(path)

        raise Exception(f'No suitable importer was found for the file: {path}')
