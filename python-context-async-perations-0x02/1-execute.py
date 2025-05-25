import sqlite3

class ExecuteQuery:
        """Class-based context manager to handle database connection and query execution."""
            
                def __init__(self, db_name, query, params):
                            self.db_name = db_name
                                    self.query = query
                                            self.params = params
                                                    self.conn = None
                                                            self.cursor = None

                                                                def __enter__(self):
                                                                            """Opens the database connection and executes the query."""
                                                                                    self.conn = sqlite3.connect(self.db_name)
                                                                                            self.cursor = self.conn.cursor()
                                                                                                    self.cursor.execute(self.query, self.params)
                                                                                                            return self.cursor.fetchall()  # Returns the results of the query

                                                                                                            def __exit__(self, exc_type, exc_value, traceback):
                                                                                                                        """Ensures the connection is properly closed."""
                                                                                                                                if exc_type is not None:
                                                                                                                                                self.conn.rollback()  # Rollback changes if an error occurs
                                                                                                                                                        self.conn.close()  # Always close connection

                                                                                                                                                        # Query setup
                                                                                                                                                        query = "SELECT * FROM users WHERE age > ?"
                                                                                                                                                        params = (25,)

                                                                                                                                                        # Use the context manager to execute the query and retrieve results
                                                                                                                                                        with ExecuteQuery("users.db", query, params) as results:
                                                                                                                                                                print(results)  # Print query results
