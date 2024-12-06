# A minimal example. No error handling. No docstring.
import sqlite3
from importlib import resources

# See pyproject.toml which states that the package is coursework2 and that .db files are in that package
db_path = str(resources.files("coursework2").joinpath("paralympics.db"))


def select_all(table_name, columns):
    # You can't parameterise table and column names in SQLite, so string formatting used here
    qry = f"SELECT {columns} FROM {table_name};"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(qry)
    rows = cursor.fetchall()
    connection.close()
    return rows
