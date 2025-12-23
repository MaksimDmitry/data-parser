import logging
import argparse
from data_parser import parser

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    parser = argparse.ArgumentParser(description='Data Parser')
    parser.add_argument('-f', '--file', help='Input file path', required=True)
    parser.add_argument('-o', '--output', help='Output file path', required=True)
    args = parser.parse_args()
    data_parser = parser.DataParser(args.file, args.output)
    try:
        data_parser.parse()
        logging.info('Data parsing completed successfully')
    except Exception as e:
        logging.error(f'Error parsing data: {e}')

if __name__ == '__main__':
    main()