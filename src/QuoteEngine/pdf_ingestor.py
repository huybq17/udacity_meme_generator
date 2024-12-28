"""Define pdf_ingestor Class."""

from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
from .txt_ingestor import txt_ingestor
import random
import subprocess
import os
import tempfile


class pdf_ingestor(IngestorInterface):
    """Class to ingest pdf files."""

    added_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse pdf file and return list of QuoteModel objects."""
        if not cls.do_ingest(path):
            raise ValueError(f"Unsupported file extension for {path}")

        comments = []
        tmp_file = []

        tmp_file = './tmp/{}.txt'.format(random.randint(0, 1000000))

        subprocess.run(['pdftotext', path, tmp_file], shell=True)

        try:
            comments = txt_ingestor.parse(tmp_file)
        finally:
            os.remove(tmp_file)
            return comments
