# python-meme-generator
Udacity Degree: A simple meme image generator created for the Udacity Nanodegree program

# Instructions

To run the applications, please follow the setup steps outlined below:

- Under the root folder, create and activate a new virtual environment.
    ```bash
    $ python -m venv venv
    $ source ./venv/bin/activate
    $ deactivate
    ```
- To install dependencies in the "requirements.txt"
    ```bash
    $ pip install -r requirements.txt
    ```
- To install xpdf CLI.
    ```bash
    $ sudo apt-get install -y xpdf
    ```

After that, run the below command:

On CLI tests:

```bash
$ cd src
$ python3 meme.py
```
Web App
```bash
$ python3 app.py
```
# Descriptions of Modules

# QuoteEngine:
   - Role & Responsilibity: Parse quotes from various input file formats, including PDF, CSV, DOCX, and TXT, and return a list of `QuoteModel` objects that encapsulate the body text and the author.
   - Use cases: We have implemented a class called `Ingestor`. To use it, simply pass the desired file path to `Ingestor.parse(f)`, and it will automatically select the appropriate module based on the file extension.
   - Dependencies:Requires `xpdf`, which is called through a subprocess to convert PDF files to text; `docx` for processing DOCX files; and `pandas` for handling CSV files.

# MemeEngine:
   - Role & Responsibility: Load an image, resize it, insert a quote with the author's name, and save the processed image to the disk.
   - Use cases:
     - Create an MemeEngine instance with desired folder for storing processed image: ```meme = MemeEngine('./tmp')```
     - Generate a meme using the specified path to the input image, along with the quote text and author: ```path = meme.make_meme(img, quote.body, quote.author)```
   - Dependencies: PIL
# udacity_meme_generator
