import sqlite3
import os

orderedDataPath = "../../Data/orderedData"
rawDataPath = "../../Data/rawData"

# tName: table name
# tType: software name
# tHeaders: table headers
# tData: table data
# tHeadersType: table headers data type
def createNewTable(tName, tType, tHeaders, tHeadersType, tData):
    orderedDataContents = os.listdir(orderedDataPath)
    
    # checks to see if database for tech item exists
    # if no: create folder 
    tableExist = False
    for techItem in orderedDataContents:
        if(techItem == tType):
            tableExist = True
            break
    
    newFolderPath = orderedDataPath + "/" + tType
    
    if(tableExist == False):
        os.makedirs(newFolderPath, exist_ok=True)
    
    # dbConnection = ""../../Data/orderedData/{{techItem}}/{{techItem}}.db"
    # ps: if db file doesn't exist, it will create a new one.
    dbConnection = sqlite3.connect(newFolderPath + "/" + techItem + ".db")
    dbCursor = dbConnection.cursor()
    
    # get all of the headers and data type into an sql string
    sqlHeaderString = ""
    for i in range(len(tHeaders)):
        if(i == len(tHeaders)):
            sqlHeaderString += tHeaders[i] + " " + tHeadersType
        else:
            sqlHeaderString += tHeaders[i] + " " + tHeadersType + ","
            
    # execute the sql create table using table name and header string
    dbCursor.execute("CREATE TABLE " + tName + "(" + sqlHeaderString + ");")
    
    # get all of the data into an sql string
    sqlDataString = ""
    for i in range(len(tData)):
        
        sqlDataString += "("
        
        for h in range(len(tData[i])):
            if(h == len(tData[i])):
                sqlDataString += tData[i][h]
                break
            sqlDataString += tData[i][h] + ","
            
        sqlDataString += ")"                        
        
        if(i == len(tData)):
            print("hello world")
    

def startUpDataValidation():
    print("hello world")