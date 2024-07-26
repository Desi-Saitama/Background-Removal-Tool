import argparse
import os
from PIL import Image
import PIL
from rembg import remove
from pathlib import Path  

def create_parser():
    parser = argparse.ArgumentParser(description="Command-line Image Removal App")
    parser.add_argument("-rbg", "--removebg", metavar="", help="Remove Image Background, give path of Image")
    return parser

def remove_bg(image_path):
    if(os.path.exists(image_path)):
        try:
            p = Path(image_path)
            input_img = Image.open(image_path)
            output = remove(input_img)
            output_path = str(p.parent)+"/devrembg.png"
            output.save(output_path)
        except (FileNotFoundError, Image.UnidentifiedImageError) as e:
            print(f"Error processing image: {e}")
    else:
        print("File Path does not found")

def main():
    parser = create_parser()
    argument = parser.parse_args()

    if argument.removebg:
        remove_bg(argument.removebg)
    else:
        print("No argument found")

if __name__ == "__main__":
    main()