import sqlite3
import functools

#### decorator to lof SQL queries
def log_queries(func):
        """Decorator to log SQL queries before execution."""
            @functools.wraps(func)
                def wrapper(*args, **kwargs):
                            # Assuming the first argument is the SQL query
                                    query = args[0] if args else kwargs.get("query", "")
                                            print(f"Executing SQL Query: {query}")
                                                    return func(*args, **kwargs)
                                                    
                                                    return wrapper

                                                @log_queries
                                                def fetch_all_users(query):
                                                        conn = sqlite3.connect('users.db')
                                                            cursor = conn.cursor()
                                                                cursor.execute(query)
                                                                    results = cursor.fetchall()
                                                                        conn.close()
                                                                            return results

                                                                        # Fetch users while logging the query
                                                                        users = fetch_all_users(query="SELECT * FROM users")
                                                                        print(users)
