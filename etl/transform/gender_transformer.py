class GenderTransformer:
    def __init__(self):
        self.gender_map = {
            'f': 'féminin',
            'm': 'masculin'
        }

    def transform(self, data):
        transformed_data = []
        for item in data:
            new_item = item.copy()
            if 'genre' in new_item:
                new_item['genre'] = self.gender_map.get(new_item['genre'].lower(), new_item['genre'])
            transformed_data.append(new_item)
        return transformed_data