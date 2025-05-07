import sqlite3

class DBLoader:
    def __init__(self, db_path):
        self.db_path = db_path

    def load(self, data, table_name):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Assuming all dictionaries in data have the same keys
            if data:
                columns = ', '.join(data[0].keys())
                placeholders = ', '.join(['?' for _ in data[0]])
                insert_query = f"INSERT OR REPLACE INTO {table_name} ({columns}) VALUES ({placeholders})"

                for item in data:
                    cursor.execute(insert_query, tuple(item.values()))

            conn.commit()
            print(f"Data successfully inserted into {table_name}")
        except Exception as e:
            print(f"Error inserting into database: {e}")
        finally:
            if conn:
                conn.close()