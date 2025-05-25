import time
import sqlite3
import functools

def with_db_connection(func):
        """Decorator to open and close database connection automatically."""
            @functools.wraps(func)
                def wrapper(*args, **kwargs):
                            conn = sqlite3.connect('users.db')  # Open connection
                                    try:
                                                    result = func(conn, *args, **kwargs)  # Pass connection to function
                                                            finally:
                                                                            conn.close()  # Ensure connection is closed
                                                                                    return result
                                                                                    return wrapper

                                                                                def retry_on_failure(retries=3, delay=2):
                                                                                        """Decorator to retry a function if it raises an exception."""
                                                                                            def decorator(func):
                                                                                                        @functools.wraps(func)
                                                                                                                def wrapper(*args, **kwargs):
                                                                                                                                for attempt in range(retries):
                                                                                                                                                    try:
                                                                                                                                                                            return func(*args, **kwargs)  # Execute function
                                                                                                                                                                                        except (sqlite3.OperationalError, sqlite3.DatabaseError) as e:
                                                                                                                                                                                                                print(f"Attempt {attempt + 1} failed due to {e}. Retrying in {delay} seconds...")
                                                                                                                                                                                                                                    time.sleep(delay)  # Wait before retrying
                                                                                                                                                                                                                                                raise Exception(f"Function failed after {retries} attempts")
                                                                                                                                                                                                                                                    return wrapper
                                                                                                                                                                                                                                                    return decorator

                                                                                                                                                                                                                                                @with_db_connection
                                                                                                                                                                                                                                                @retry_on_failure(retries=3, delay=1)
                                                                                                                                                                                                                                                def fetch_users_with_retry(conn):
                                                                                                                                                                                                                                                        cursor = conn.cursor()
                                                                                                                                                                                                                                                            cursor.execute("SELECT * FROM users")
                                                                                                                                                                                                                                                                return cursor.fetchall()

                                                                                                                                                                                                                                                            # Attempt to fetch users with automatic retry on failure
                                                                                                                                                                                                                                                            users = fetch_users_with_retry()
                                                                                                                                                                                                                                                            print(users)

