import os
import json
import logging
import logging.config

def create_logger(default_path='config/config.json',default_level=logging.ERROR):
    """Setup logging configuration
    """
    path = default_path

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    logger = logging.getLogger(__name__)
    return logger

logger = create_logger()