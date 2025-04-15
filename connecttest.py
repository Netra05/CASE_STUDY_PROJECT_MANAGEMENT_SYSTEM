import pyodbc

def test_db_connection():
    try:
        # Database connection details
        driver = '{your driver name}'
        server = 'your server name'
        database = 'your db name'
        trusted_connection = 'yes'

        # Create connection string
        conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}"

        # Try to establish a connection
        conn = pyodbc.connect(conn_str)
        print("Connection successful!")
        conn.close()
    except Exception as e:
        print("Error connecting to DB:", e)

if __name__ == "__main__":
    test_db_connection()
