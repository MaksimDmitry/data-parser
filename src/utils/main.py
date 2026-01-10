import argparse
import json
import logging
from data_parser.parser import DataParser
from data_parser.utils import configure_logging

def main():
    parser = argparse.ArgumentParser(description='Data Parser')
    parser.add_argument('-c', '--config', help='Path to configuration file', required=True)
    parser.add_argument('-i', '--input', help='Path to input file', required=True)
    parser.add_argument('-o', '--output', help='Path to output file', required=True)
    args = parser.parse_args()

    configure_logging('data_parser.log')

    try:
        with open(args.config, 'r') as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f'Failed to parse configuration file: {e}')
        return

    data_parser = DataParser(config)
    try:
        with open(args.input, 'r') as f:
            data = f.read()
        parsed_data = data_parser.parse(data)
        with open(args.output, 'w') as f:
            f.write(parsed_data)
        logging.info('Data parsed and written to output file successfully')
    except Exception as e:
        logging.error(f'Error parsing data: {e}')

if __name__ == '__main__':
    main()