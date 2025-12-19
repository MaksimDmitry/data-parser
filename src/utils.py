import logging
import os
from typing import Dict, List, Tuple

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def get_config_file_path(file_name: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'config', file_name)

def load_config(file_name: str) -> Dict:
    import json
    file_path = get_config_file_path(file_name)
    with open(file_path, 'r') as file:
        return json.load(file)

def parse_data(data: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    parsed_data = []
    errors = []
    for item in data:
        try:
            # simulate parsing logic
            parsed_item = {'id': item['id'], 'value': item['value'] * 2}
            parsed_data.append(parsed_item)
        except KeyError as e:
            errors.append({'id': item['id'], 'error': str(e)})
    return parsed_data, errors

def write_to_file(file_name: str, data: List[Dict]) -> None:
    with open(file_name, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

def main():
    logger = setup_logger('data-parser')
    config = load_config('config.json')
    data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 20},
        {'id': 3}
    ]
    parsed_data, errors = parse_data(data)
    logger.info('Parsed data: %s', parsed_data)
    logger.info('Errors: %s', errors)
    write_to_file('output.txt', parsed_data)

if __name__ == '__main__':
    main()