import os
import logging
import json
from typing import Dict, List
from urllib.parse import urlparse

def get_logger(name: str) -> logging.Logger:
    """Create a logger with the given name."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

def load_json(file_path: str) -> Dict:
    """Load a JSON file and return its contents as a dictionary."""
    with open(file_path, 'r') as f:
        return json.load(f)

def extract_domain(url: str) -> str:
    """Extract the domain from a URL."""
    return urlparse(url).netloc

def get_file_extension(file_path: str) -> str:
    """Get the file extension from a file path."""
    return os.path.splitext(file_path)[1]