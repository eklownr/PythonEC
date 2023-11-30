# Jag har i förväg installerat postgress och fixat med pip fyi!

import psycopg2 
from psycopg2 import sql
from config2 import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

def main():
    db_params = {
        "host": DB_HOST,
        "port": DB_PORT,
        "database": DB_NAME,
        "user": DB_USER,
        "password": DB_PASSWORD
    }

    try:
        connection = psycopg2.connect(**db_params)
        print("Succesfully connected to database")

        with connection.cursor() as cursor:
            table_exist_query = """
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.tables
                WHERE table_name = 'dogs'
            );
            """
            cursor.execute(table_exist_query)
            table_exist = cursor.fetchone()[0]
            
            if not table_exist:
                create_table_query  = """
                CREATE TABLE dogs (
                    race text,
                    color text
                );
                """
                cursor.execute(create_table_query)
                print("Table has now been created")
            
            data_query = """
            INSERT INTO dogs (
                race, color
            ) VALUES (%s, %s)
            """

            data = ("Labrador", "Black")
            cursor.execute(data_query, data)

            connection.commit()
            print("Finished running all statements")


    except psycopg2.Error as e:
        print("This error was generated: ", e)
    finally:
        if connection:
            connection.close()
            print("Connection to database was terminated")

if __name__ == "__main__":
    main()