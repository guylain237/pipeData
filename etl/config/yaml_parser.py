import yaml

class YAMLParser:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def parse(self):
        with open(self.yaml_file, 'r') as file:
            return yaml.safe_load(file)