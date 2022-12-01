from pathlib import Path
import json
from logging.config import fileConfig
import os

class MyConfig:
    """
    offers project relevant folder
    """
    def __init__(self) -> None:
        with open(json_path) as infile:
            content = infile.read()
        self.cfg = json.loads(content)
        self.model_folder_name = self.cfg['model_folder']
        self.data_folder_name = self.cfg['data_folder']

    @staticmethod
    def get_app_folder() -> Path:
        return Path(__file__).parent

    def get_model_folder(self) -> str:
        return self.model_folder_name
    
    def get_data_folder(self) -> str:
        return self.data_folder_name
    
    def get_table(self) -> str:
        return self.cfg['table']


ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
fileConfig(os.path.join(ROOT_DIR, 'config', 'logging.ini'), disable_existing_loggers=False)
json_path = os.path.join(ROOT_DIR, 'config', 'config.json')


