import argparse
import json
import logging
from data_parser import parser

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    parser = argparse.ArgumentParser(description='Data Parser')
    parser.add_argument('--input', type=str, required=True, help='Input file path')
    parser.add_argument('--output', type=str, required=True, help='Output file path')
    args = parser.parse_args()
    try:
        with open(args.input, 'r') as file:
            data = json.load(file)
        parsed_data = parser.parse(data)
        with open(args.output, 'w') as file:
            json.dump(parsed_data, file, indent=4)
        logging.info('Data parsed and written to output file')
    except FileNotFoundError:
        logging.error('Input file not found')
    except json.JSONDecodeError:
        logging.error('Invalid JSON in input file')
    except Exception as e:
        logging.error('An error occurred: %s', str(e))

if __name__ == '__main__':
    main()