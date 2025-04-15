import pyodbc

class DBConnUtil:

    @staticmethod
    def get_connection():
        try:
            # Hardcoded connection string
            connection_string = (
                "DRIVER={your driver name};"
                "SERVER=your server name;"  
                "DATABASE=your db name;"        
                "Trusted_Connection=yes;"
            )

           
            conn = pyodbc.connect(connection_string)
            return conn
        except Exception as e:
            print(f"Error connecting to DB: {e}")
            return None

    @staticmethod
    def test_connection():
       
        conn = DBConnUtil.get_connection()
        if conn:
            print("Database connection successful!")
            conn.close()
        else:
            print("Failed to connect to the database.")

# Example usage
if __name__ == "__main__":
    DBConnUtil.test_connection()
