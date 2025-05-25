import time
import sqlite3
import functools

query_cache = {}

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

                                                                                def cache_query(func):
                                                                                        """Decorator to cache database query results."""
                                                                                            @functools.wraps(func)
                                                                                                def wrapper(conn, query, *args, **kwargs):
                                                                                                            if query in query_cache:
                                                                                                                            print("Using cached result for query:", query)
                                                                                                                                        return query_cache[query]  # Return cached result
                                                                                                                                            
                                                                                                                                            result = func(conn, query, *args, **kwargs)  # Execute function
                                                                                                                                                    query_cache[query] = result  # Cache the result
                                                                                                                                                            return result
                                                                                                                                                            
                                                                                                                                                            return wrapper

                                                                                                                                                        @with_db_connection
                                                                                                                                                        @cache_query
                                                                                                                                                        def fetch_users_with_cache(conn, query):
                                                                                                                                                                cursor = conn.cursor()
                                                                                                                                                                    cursor.execute(query)
                                                                                                                                                                        return cursor.fetchall()

                                                                                                                                                                    # First call will cache the result
                                                                                                                                                                    users = fetch_users_with_cache(query="SELECT * FROM users")

                                                                                                                                                                    # Second call will use the cached result
                                                                                                                                                                    users_again = fetch_users_with_cache(query="SELECT * FROM users")

                                                                                                                                                                    print(users_again)  # This will retrieve the cached result instead of querying the database again

