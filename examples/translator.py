import googletrans
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file_name', help="give the filename")

args = parser.parse_args()

translator = googletrans.Translator()

with open(args.file_name, 'r') as input_file:
    output_file = open('tamil_file.txt', 'w')
    for line in input_file:
        output_file.write(f"{translator.translate(line, dest='ta').text}\n")
