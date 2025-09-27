from enum import Enum

#Database Imports
import mysql.connector
from mysql.connector import errorcode
import yaml
import pandas as pd
from pathlib import Path
#Environmental  Libraries

import os
import sys

# MySQL Queries
sys.path.append('ICU_DataQueries.py')
import ICU_DataQueries


# -----Primitive Configuration---@
class Cridentials(Enum):        #\
     host = "host"              #|
     user = "user"              #/
     passwd = "passwd"          #\
     DataBase = "database"      #|
     charset = "char type"      #\
     collation = "type"         #/
#--------------------------------@


DB_Socket = mysql.connector
DB_credentials =  {"host": Cridentials.host, 
                  "user": Cridentials.user, 
                  "passwd": Cridentials.passwd, 
                  "Data_Base": Cridentials.DataBase,
		  "charset" : Cridentials.charset,
		  "collation": Cridentials.collation}



def Create_CSV(data):
    folder_name= Path("Datasets")
    Panda_DataFrame = pd.DataFrame(data)
    try:
        folder_name.mkdir(parents=True, exist_ok=True)
        os.chdir(folder_name)
        if sys.argv[1] == '-i':
            Panda_DataFrame.to_csv("ICU_Asnyncronies_MV.csv", index=False)
        elif sys.argv[1] == '-r':
            Panda_DataFrame.to_csv("ICU_PRESSURE_MV.csv", index=False)
        else:
            Panda_DataFrame.to_csv("unspecified_dataset.csv", index=False)

    except Exception as e:
        print("OS::Forbids creation of folders at:", 
              os.getcwd())



def Load_Cridentials():
    try:
        with open("MySQL_config.yaml", "r") as file:
            config = yaml.safe_load(file)
            config = config["mysql"]
    except Exception as err:
        print("Error: Credential File not found\n {err}\n")
        return False
    
    DB_credentials["host"] = config["host"]
    DB_credentials["user"] = config["user"]
    DB_credentials["database"] = config["database"]
    DB_credentials["passwd"] = config["passwd"]
    DB_credentials["charset"] = config["charset"]
    DB_credentials["collation"] = config["collation"]

    return True



def Create_Connectoin(DB_Socket: mysql.connector.connection.MySQLConnection):
    conn = DB_Socket.connect(
            user=DB_credentials["user"],
            password=DB_credentials["passwd"],  
            host=DB_credentials["host"],
            database=DB_credentials["database"],
            charset = DB_credentials["charset"],
            collation = DB_credentials["collation"] 
            # this bugger caused 2 days of debbuging :):):)
        )
    return conn



def Establish_Connection(DB_credentials: dict,
    DB_Socket: mysql.connector.connection.MySQLConnection):

    on_connection = True
    try:
        DB_Socket = Create_Connectoin(DB_Socket=DB_Socket)

    except mysql.connector.Error as err:
        on_connection = False
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("\tInvalid Password or Username")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Provided database: {DB_credentials['database']}- Does not exist\n")
        else:
            print(err)        
    return on_connection



def Run_Query(MySQL_query:str,
    DB_Socket:  mysql.connector.connection.MySQLConnection):

    DB_Socket = Create_Connectoin(DB_Socket=DB_Socket)
    Cursor = DB_Socket.cursor()

    try:
        Cursor.execute(MySQL_query)
        data = Cursor.fetchall()
        Create_CSV(data= data)
    except mysql.connector.Error as err:
        print(f"PythonSQL connector Error")
        exit()
    finally:
        Cursor.close()
    



def main(DB_Socket: mysql.connector.connection.MySQLConnection):
    if(not Load_Cridentials()
    or not Establish_Connection(DB_credentials, DB_Socket)): 
        exit()
   
    MySQL_QUERY = ICU_DataQueries.Default_Queries(sys.argv[1])
    Run_Query(MySQL_QUERY.GetSQL(), DB_Socket=DB_Socket)
    


def sanity_check(command_arg_size):
    Usage = """Usage is: \n
    /~ python3 DataExtration.py -i \n or 
    /~ python3 DataExtration.py -r""" 
    #-r for Rali's dataset, -i for Ivelin's Dataset

    if ((command_arg_size != 2 ) or 
    ((str(sys.argv[1]) not in ICU_DataQueries.query_tags))):
        print(Usage)
        exit(0)


if __name__ == "__main__":
    command_arg_size = len(sys.argv)
    sanity_check(command_arg_size)
    main(DB_Socket)