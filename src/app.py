"""The main application performs the processes with all the modules."""

import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
from os import listdir
from os.path import isfile, join
import tempfile

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Combine all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for single_file in quote_files:
        quotes.extend(Ingestor.parse(single_file))

    images_path = "./_data/photos/dog/"
    imgs = [join(images_path, f)
            for f in listdir(images_path) if isfile(join(images_path, f))]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """To generate a random meme image."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """.Create a user's meme."""
    try:
        image_url = request.form.get('image_url')
        if image_url == "":
            raise Exception("Empty URL!")
        body = request.form.get('body')
        author = request.form.get('author')
    except Exception as e:
        return render_template('meme_form.html',
                               message=f"Invalid URL or empty fields: {e}")

    try:
        print(f'image_url = {image_url}')
        print(f'Author = {author} -- Body = {body}')
        url_respone = requests.get(image_url)
        random_file = f'{random.randint(0, 100000)}_download_img.jpg'
        temp_file = MemeEngine.build_pic_path('./tmp', random_file)

        with open(temp_file, 'wb') as file:
            file.write(url_respone.content)
    except Exception as e:
        print(f"Error when handling the image url!")

    try:
        path = meme.make_meme(temp_file, body, author)
        os.remove(temp_file)
        return render_template('meme.html', path=path)
    except Exception as e:
        raise ValueError(f'Invalid URL: {e}')


if __name__ == "__main__":
    app.run()
