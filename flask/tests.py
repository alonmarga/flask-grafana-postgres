import psycopg2
from psycopg2 import OperationalError
from urllib.parse import urlparse
import os
from dotenv import load_dotenv



load_dotenv()


# Parse the DATABASE_URL from environment variables
database_url = os.getenv('DATABASE_URL')
url = urlparse(database_url)
print(url)
# Extract connection parameters
database_name = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

def test_postgresql_connection():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            database=database_name,
            user=user,
            password=password,
            host=host,
            port=port
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a simple query
        cursor.execute("SELECT version();")

        # Fetch the result
        result = cursor.fetchone()
        print("PostgreSQL version:", result[0])

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except OperationalError as e:
        print("Error: Could not connect to the PostgreSQL database.")
        print(e)

if __name__ == "__main__":
    test_postgresql_connection()
