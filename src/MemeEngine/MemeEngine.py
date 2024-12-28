"""The class generates memes from image urls and quotes."""

import os
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:
    """Class for creating the meme images out of a quote, author, and image."""

    def __init__(self, output_dir: str = './tmp') -> None:
        """Initialize MemeEngine."""
        self.outdir = output_dir

    def make_meme(self, pic_path, text, author, width=500) -> str:
        """Insert quotes/comments into the image."""
        if not isinstance(pic_path, str):
            raise TypeError(f'"pic_path" should be of type str')
        if not isinstance(text, str):
            raise TypeError(f'"text" should be of type str')
        if not isinstance(author, str):
            raise TypeError(f'"author" should be of type str')

        with Image.open(pic_path) as img:
            rat = img.width / img.height
            heig = int(width / rat)
            img = img.resize((width, heig))

            specific_font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                               size=24)
            draws = ImageDraw.Draw(img)
            above_text = random.randint(5, width // 2)
            below_text = random.randint(5, heig - heig//10)

            draws.text((above_text, below_text), text, fill='white',
                       font=specific_font, align='right')
            draws.text((above_text + 30, below_text + 30), f'- {author}',
                       font=specific_font, align='center', fill='white')

            new_pic_name = f'meme_{os.path.basename(pic_path)}'
            new_pic_path = MemeEngine.build_pic_path(self.outdir, new_pic_name)
            img.save(new_pic_path)

            return new_pic_path

    @staticmethod
    def build_pic_path(direct: str, image_name: str) -> str:
        """Build the path for the output images."""
        try:
            os.makedirs(direct, exist_ok=True)
            return os.path.join(direct, image_name)
        except OSError as e:
            raise IOError(f"Error creating directory: {str(e)}") from e
