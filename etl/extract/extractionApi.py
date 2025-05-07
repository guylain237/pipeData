import requests

class APIExtractor:
    def __init__(self, base_url):
        self.base_url = base_url

    def extract(self,  params=None):
        response = requests.get(f"{self.base_url}", params=params)
        response.raise_for_status()
        return response.json()