import yaml
import logging.config
import logging


def setup_logging():
    try:
        with open('config/logging.yaml', 'rt') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
    except Exception as e:
        print(f"Error loading logging config. Reason: {e}")
        exit(1)
