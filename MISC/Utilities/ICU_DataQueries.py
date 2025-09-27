import yaml
import sys

from dataclasses import dataclass, field

ICU_MV_Asyncronies: str = field(default_factory=str)
ICU_MV_PRESSURE : str = field(default_factory=str)


query_tags: list = field(default_factory=list)
query_tags = ["-i", "-r"]

class Default_Queries:
    Query_Dict= {}

    def __init__(self, SQL_req: str):
        self.SQL_req = SQL_req
        self.Load_MySQL_Queries()

    def Load_MySQL_Queries(self):
        try:    
            with open('MySQL_config.yaml', 'r') as file:
                self.RawQueries = yaml.safe_load(file)
            
            for index in query_tags:   
                self.Query_Dict.update(
                    {index : self.RawQueries[index]})
        except Exception as err:
            print("MySQL_config.yaml file is corrupted\n")
            exit(0)        

    def GetSQL(self):

        if self.SQL_req in query_tags:
            if(self.SQL_req == query_tags[0]):
                ICU_MV_Asyncronies = self.Query_Dict[self.SQL_req]
                return ICU_MV_Asyncronies
            
            elif(self.SQL_req == query_tags[1]):
                ICU_MV_PRESSURE= self.Query_Dict[self.SQL_req]
                return ICU_MV_PRESSURE
            else:
                print("MySQL query with tag:",self.SQL_req," is still under development\n")
                exit(0)
        else: 
            print("Your tag: ",self.SQL_req," has no associated MySQL query\n")
            exit(0)