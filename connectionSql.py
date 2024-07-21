import pypyodbc as odbc

def connection():

    # This function create the connection Python - Sql Server.
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'RobisonTorres\SQLEXPRESS'
    DATABASE_NAME = 'Stock'
    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
        """
        # uid=<your_username>; In this project, as Sql Server don't requires password
        # pwd=<your_password> there's no need to 'add' uid and 'pwd'.
    
    return odbc.connect(connection_string)