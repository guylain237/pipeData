import json

class JSONLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self, data):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Data successfully written to {self.file_path}")
        except Exception as e:
            print(f"Error writing to JSON file: {e}")