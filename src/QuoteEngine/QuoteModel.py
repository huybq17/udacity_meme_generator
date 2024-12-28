"""The QuoteModel class is designed to encapsulate 2 things.

Both the body of each quotes and the name of each authors.

"""


class QuoteModel:
    """This class is used to above encapsulate."""

    def __init__(self, author: str, body: str):
        """Initialize the QuoteModel class."""
        if not isinstance(body, str):
            raise TypeError(f'"body" is not a type str')
        else:
            self.body = body

        if not isinstance(author, str):
            raise TypeError(f'"author" is not a type str')
        else:
            self.author = author.strip('""')

    def __str__(self) -> str:
        """Return a string representation of the QuoteModel class."""
        return f'{self.body} - {self.author}'

    def __repr__(self) -> str:
        """Return a string representation of the QuoteModel class."""
        return f'{self.body} - {self.author}'
