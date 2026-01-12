import argparse
import json
import logging
from data_parser.parser import DataParser
from data_parser.utils import configure_logging

def parse_arguments():
    parser = argparse.ArgumentParser(description='Data Parser')
    parser.add_argument('-c', '--config', help='Path to configuration file', required=True)
    parser.add_argument('-i', '--input', help='Path to input file', required=True)
    parser.add_argument('-o', '--output', help='Path to output file', required=True)
    return parser.parse_args()

def load_config(config_path):
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f'Failed to parse configuration file: {e}')
        return None

def parse_and_write_data(data_parser, input_path, output_path):
    try:
        with open(input_path, 'r') as f:
            data = f.read()
        parsed_data = data_parser.parse(data)
        with open(output_path, 'w') as f:
            f.write(parsed_data)
        logging.info('Data parsed and written to output file successfully')
    except Exception as e:
        logging.error(f'Error parsing data: {e}')

def main():
    args = parse_arguments()
    configure_logging('data_parser.log')
    config = load_config(args.config)
    if config is None:
        return

    data_parser = DataParser(config)
    parse_and_write_data(data_parser, args.input, args.output)

if __name__ == '__main__':
    main()