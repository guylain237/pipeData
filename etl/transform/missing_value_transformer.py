class MissingValueTransformer:
    def __init__(self, columns, replacement_value):
        self.columns = columns if isinstance(columns, list) else [columns]
        self.replacement_value = replacement_value

    def transform(self, data):
        if not data:
            return []
        
        transformed_data = []
        for row in data:
            if isinstance(row, dict):
                new_row = row.copy()
                for col in self.columns:
                    if col in new_row and (new_row[col] is None or new_row[col] == ''):
                        new_row[col] = self.replacement_value
                transformed_data.append(new_row)
            else:
                transformed_data.append(row)  # If not dict, we can't handle it, so we just pass it through
        return transformed_data