"""CMD line tool for generating memes."""
import os
import random
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate the new meme given an path and a quote text."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(author, body)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # Use ArgumentParser to parse the CLI arguments

    parser_arg = argparse.ArgumentParser(description='MemeGenerator CLI')

    parser_arg.add_argument("--path",
                            help="Path to an image file", type=str)
    parser_arg.add_argument("--body",
                            help="Quote body to add to the image", type=str)
    parser_arg.add_argument("--author",
                            help="Quote author to add to the image", type=str)

    args = parser_arg.parse_args()
    print(generate_meme(args.path, args.body, args.author))
