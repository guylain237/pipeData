import csv
import json
import pandas as pd
import os

class FileExtractor:
    def __init__(self, file_path):
        self.file_path = os.path.join('dir', file_path)

    def extract(self):
        file_extension = self.file_path.split('.')[-1].lower()
        
        extractors = {
            'csv': self.extract_csv,
            'json': self.extract_json,
            'txt': self.extract_text
        }
        
        extractor = extractors.get(file_extension)
        if extractor:
            return extractor()
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")

    def extract_csv(self):
        return pd.read_csv(self.file_path).to_dict('records')

    def extract_json(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def extract_text(self):
        with open(self.file_path, 'r') as file:
            return file.readlines()