#!/usr/bin/env python3

from mysql.connector import connect, Error

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'password'
DB_NAME = 'ALX_prodev'

def connect_db():
        try:
                    return connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
                    except Error as e:
                                print(e)


                                def create_database(connection):
                                        query = f'CREATE DATABASE IF NOT EXISTS {DB_NAME}'
                                            try:
                                                        with connection.cursor() as cursor:
                                                                        cursor.execute(query)
                                                                            except Error as e:
                                                                                        print(e)


                                                                                        def connect_to_prodev():
                                                                                                try:
                                                                                                            return connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
                                                                                                            except Error as e:
                                                                                                                        print(e)


                                                                                                                        def create_table(connection):
                                                                                                                                query = '''CREATE TABLE IF NOT EXISTS user_data (
                                                                                                                                                user_id VARCHAR(255) PRIMARY KEY, 
                                                                                                                                                                name VARCHAR(255) NOT NULL, 
                                                                                                                                                                                email VARCHAR(255) NOT NULL,
                                                                                                                                                                                                age DECIMAL NOT NULL
                                                                                                                                                                                                            )'''
                                                                                                                                                                                                                try:
                                                                                                                                                                                                                            with connection.cursor() as cursor:
                                                                                                                                                                                                                                            cursor.execute(query)
                                                                                                                                                                                                                                                except Error as e:
                                                                                                                                                                                                                                                            print(e)


                                                                                                                                                                                                                                                            def insert_data(connection, data):
                                                                                                                                                                                                                                                                    query = f'''
                                                                                                                                                                                                                                                                                INSERT INTO user_data VALUES
                                                                                                                                                                                                                                                                                            ("{data['uuid']}", "{data['name']}", "{data['email']}", {data['age']})
                                                                                                                                                                                                                                                                                                        '''
                                                                                                                                                                                                                                                                                                            try:
                                                                                                                                                                                                                                                                                                                        with connection.cursor() as cursor:
                                                                                                                                                                                                                                                                                                                                        cursor.execute(query)
                                                                                                                                                                                                                                                                                                                                            except Error as e:
                                                                                                                                                                                                                                                                                                                                                        print(e)


                                                                                                                                                                                                                                                                                                                                                        if __name__ == '__main__':
                                                                                                                                                                                                                                                                                                                                                                conn1 = connect_db()
                                                                                                                                                                                                                                                                                                                                                                    create_database(conn1)
                                                                                                                                                                                                                                                                                                                                                                        conn2 = connect_to_prodev()
                                                                                                                                                                                                                                                                                                                                                                            create_table(conn2)
                                                                                                                                                                                                                                                                                                                                                                                insert_data(conn2,
                                                                                                                                                                                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                                                                                                                                                                                                "uuid": "2cb9e2c9-bc99-4ed0-b203-4c7f35733578",
                                                                                                                                                                                                                                                                                                                                                                                                                            "name": "Ernest Wambua",
                                                                                                                                                                                                                                                                                                                                                                                                                                        "email": "ernest@example.com",
                                                                                                                                                                                                                                                                                                                                                                                                                                                    "age": 24
                                                                                                                                                                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                                                                                                    )
                                                                                                                                                                                                                                                                                                                                                                                    conn1.close()
                                                                                                                                                                                                                                                                                                                                                                                        conn2.close()
