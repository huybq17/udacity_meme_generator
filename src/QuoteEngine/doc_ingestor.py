"""Define doc_ingestor Class."""
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
from docx import Document


class doc_ingestor(IngestorInterface):
    """Parse DOC file format using 'python-docx'."""

    added_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file format."""
        if not cls.do_ingest(path):
            raise ValueError(f"Unsupported file extension for {path}")
        comments = []

        # Open docx file & parse author and body
        docx = Document(path)
        for para in docx.paragraphs:
            row = para.text.strip().strip('\r\n')
            if len(row) != 0:
                splited_row = row.split(' - ')
                comments.append(QuoteModel(splited_row[1], splited_row[0]))

        return comments
