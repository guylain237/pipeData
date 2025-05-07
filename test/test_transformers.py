import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl.transform.filter_transformer import FilterTransformer
from etl.transform.missing_value_transformer import MissingValueTransformer

def test_filter_transformer():
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    
    filter_transformer = FilterTransformer("age > 28")
    result = filter_transformer.transform(data)
    
    assert len(result) == 2
    assert result[0]['name'] == 'Alice'
    assert result[1]['name'] == 'Charlie'
    
    print("FilterTransformer test passed!")

def test_missing_value_transformer():
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': None},
        {'name': 'Charlie', 'age': ''}
    ]
    
    missing_value_transformer = MissingValueTransformer('age', 0)
    result = missing_value_transformer.transform(data)
    
    assert result[0]['age'] == 30
    assert result[1]['age'] == 0
    assert result[2]['age'] == 0
    
    print("MissingValueTransformer test passed!")

if __name__ == "__main__":
    test_filter_transformer()
    test_missing_value_transformer()