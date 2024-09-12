class interact_db:
    def __init__(self) -> None:
        pass

    def connect_mssql(self, server, database, username, paswword):
        """
            Function for connect to Microsoft SQL Server

            Args:
                server: Server connect
                database: Database inside the server
                username: Username log in to SQL Server
                password: password connect
            
            Return:
                Connection to Microsoft SQL Server
        """

        import pyodbc

        SERVER = server
        DATABASE = database
        USERNAME = username
        PASSWORD = paswword

        connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

        conn = pyodbc.connect(connectionString)

        return conn


    def insert_staging_date(connect_sql):
        
        """
            Function for Insert table inside STG schema

            Args:
                connect_sql: Connection to Microsoft SQL Server

            Return: None
        
        """


        pass