CREATE_TABLE = """CREATE TABLE IF NOT EXISTS metrics (
                name TEXT NOT NULL, value TEXT NOT NULL, 
                timestamp NUMERIC)"""

INSERT_METRIC = 'INSERT INTO metrics (name, value, timestamp) VALUES ("%s", "%s", "%s")'

SELECT_ALL = 'SELECT * FROM metrics'