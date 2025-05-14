from configparser import ConfigParser
import os

def get_config(category, key):
    config = ConfigParser()
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.ini'))
    config.read(config_path)
    return config.get(category, key)
