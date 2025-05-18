#!/usr/bin/env python3

from mysql.connector import Error
from seed import connect_to_prodev

def stream_users():
        query = "SELECT * FROM user_data"
            connection = connect_to_prodev()
                
                    try:
                                with connection.cursor(dictionary=True) as cursor:
                                                cursor.execute(query)
                                                            result = cursor.fetchall()
                                                                        for row in result:
                                                                                            yield row
                                                                                                except Error as e:
                                                                                                            print(e)
                                                                                                                finally:
                                                                                                                            connection.close()


                                                                                                                            if __name__ == "__main__":
                                                                                                                                    stream_users()
