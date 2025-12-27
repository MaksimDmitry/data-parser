import os
import argparse
from data_parser.parser import DataParser
from data_parser.config import Config

def main():
    parser = argparse.ArgumentParser(description='Data Parser')
    parser.add_argument('-c', '--config', help='Path to configuration file', required=True)
    parser.add_argument('-i', '--input', help='Path to input file', required=True)
    parser.add_argument('-o', '--output', help='Path to output file', required=True)
    args = parser.parse_args()

    config = Config(args.config)
    data_parser = DataParser(config)

    try:
        data_parser.parse(args.input, args.output)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())