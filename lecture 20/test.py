# !! Läs README filen innan du börjar jobba med koden!!
import psycopg2
from psycopg2 import sql
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


# Database connection parameters
db_params = {
    "host": DB_HOST,
    "port": DB_PORT,
    "database": DB_NAME,
    "user": DB_USER,
    "password": DB_PASSWORD,
}


try:
    conn = psycopg2.connect(**db_params)
    print("Connected to the database!")

    with conn.cursor() as cursor:
        # Check if the table exists
        check_table_query = """
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'test_table'
        );
        """
        cursor.execute(check_table_query)
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            # If the table doesn't exist, create it
            create_table_query = """
            CREATE TABLE test_table (
                year integer,
                month integer
            );
            """
            cursor.execute(create_table_query)
            print("Table created!")

        insert_query = """
        INSERT INTO test_table (
            year, month
        ) VALUES (%s, %s);
        """

        data_to_insert = (
            2023,
            12,
        )

        cursor.execute(insert_query, data_to_insert)

        # Commit the transaction
        conn.commit()
        print("Data inserted successfully!")

except psycopg2.Error as e:
    print(f"Error: {e}")

finally:
    # Close the database connection outside the try-except block
    if conn:
        conn.close()
        print("Connection closed.")
