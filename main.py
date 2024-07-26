import argparse
import os
from PIL import Image
from rembg import remove
from pathlib import Path  

def create_parser():
    parser = argparse.ArgumentParser(description="Command-line Image Removal App")
    parser.add_argument("-rbg", "--removebg", metavar="", help="Remove Image Background, give path of Image")
    return parser

def remove_bg(image_path):
    try:
            if(os.exist.path(image_path)):
                p = Path(image_path)
                input_img = Image.open(image_path)
                output = remove(input_img)
                output_path = str(p.parent)+"/devrembg"+str(p.suffix)
                output.save(output_path)
            else:
                print("File Path does not found")
    except:
        print("Check the Argument")

def main():
    parser = create_parser()
    argument = parser.parse_args()

    if argument.removebg:
        remove_bg(argument.removebg)
    else:
        print("No argument found")

if __name__ == "__main__":
    main()