class FilterTransformer:
    def __init__(self, condition):
        self.condition = condition

    def transform(self, data):
        if not data:
            return []
        
        filtered_data = []
        for row in data:
            try:
                if eval(self.condition, globals(), row):
                    filtered_data.append(row)
            except Exception as e:
                print(f"Error evaluating condition for row: {e}")
        
        return filtered_data