import sqlalchemy

class DBExtractor:
    def __init__(self, connection_string):
        self.engine = sqlalchemy.create_engine(connection_string)

    def extract(self, query):
        with self.engine.connect() as connection:
            result = connection.execute(sqlalchemy.text(query))
            columns = result.keys()
            return [dict(zip(columns, row)) for row in result]