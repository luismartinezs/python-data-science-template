import logging

logging.basicConfig(level=logging.ERROR)


class EmptyQueryError(ValueError):
    pass


class DatabaseConnection:
    def __enter__(self):
        print("Connecting to database")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnecting from database")
        if exc_type:
            logging.error(f"An error occurred: {exc_value}")
        return False  # propagate exceptions
        # return True # supress exceptions

    def query(self, query=None):
        if not query:
            raise EmptyQueryError("Query cannot be empty")
        print(f"Executing query: {query}")


with DatabaseConnection() as db:
    try:
        db.query("SELECT * FROM users")
        db.query()  # This will raise a ValueError
    except ValueError as e:
        print(f"Caught an error: {e}")
    # The connection will be closed even if an exception occurs
