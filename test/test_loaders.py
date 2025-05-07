import sys
import os
import json
import sqlite3

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etl.load.json_loader import JSONLoader
from etl.load.db_loader import DBLoader

import json

def test_json_loader():
    test_data = [
        {"id": 1, "nom": "Alice", "age": 30, "genre": "féminin"},
        {"id": 2, "nom": "Bob", "age": 25, "genre": "masculin"},
        {"id": 3, "nom": "Charlie", "age": 35, "genre": "féminin"}
    ]

    json_loader = JSONLoader('test_output.json')
    json_loader.load(test_data)

    # Verify the data was written correctly
    with open('test_output.json', 'r') as f:
        loaded_data = json.load(f)
    
    # Compare each item individually
    assert len(loaded_data) == len(test_data), "Number of items doesn't match"
    for loaded_item, test_item in zip(loaded_data, test_data):
        assert loaded_item == test_item, f"Mismatch: {loaded_item} != {test_item}"
    
    print("JSONLoader test passed!")
    print("JSONLoader test passed!")

def test_db_loader():
    test_data = [
        {"id": 1, "nom": "Alice", "age": 30, "genre": "féminin"},
        {"id": 2, "nom": "Bob", "age": 25, "genre": "masculin"},
        {"id": 3, "nom": "Charlie", "age": 35, "genre": "féminin"}
    ]

    # Create a test database and table
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS test_table
                      (id INTEGER PRIMARY KEY, nom TEXT, age INTEGER, genre TEXT)''')
    conn.commit()
    conn.close()

    db_loader = DBLoader('test.db')
    db_loader.load(test_data, 'test_table')

    # Verify the data was inserted correctly
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_table")
    rows = cursor.fetchall()
    conn.close()

    assert len(rows) == len(test_data)
    for i, row in enumerate(rows):
        assert row == tuple(test_data[i].values())
    
    print("DBLoader test passed!")

    # Clean up
    os.remove('test.db')

if __name__ == "__main__":
    test_json_loader()
    test_db_loader()
    # Clean up JSON file
    os.remove('test_output.json')