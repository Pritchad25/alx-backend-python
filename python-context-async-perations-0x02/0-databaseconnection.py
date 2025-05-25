import sqlite3

class DatabaseConnection:
        """Class-based context manager to handle SQLite database connections."""
            
                def __init__(self, db_name):
                            self.db_name = db_name
                                    self.conn = None

                                        def __enter__(self):
                                                    """Opens the database connection and returns the connection object."""
                                                            self.conn = sqlite3.connect(self.db_name)
                                                                    return self.conn

                                                                    def __exit__(self, exc_type, exc_value, traceback):
                                                                                """Closes the database connection, rolling back if an exception occurs."""
                                                                                        if exc_type is not None:
                                                                                                        self.conn.rollback()  # Rollback changes if an error occurs
                                                                                                                self.conn.close()  # Ensure connection is closed

                                                                                                                # Use the context manager to execute a query and print results
                                                                                                                with DatabaseConnection("users.db") as conn:
                                                                                                                        cursor = conn.cursor()
                                                                                                                            cursor.execute("SELECT * FROM users")
                                                                                                                                users = cursor.fetchall()

                                                                                                                                print(users)  # Print query results~
