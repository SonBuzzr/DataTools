# EXCEL to RDS data transfer
# This code will read file from Excel and loads
# data to RDS, make it public and re-names the zip file


import openpyxl, pprint, os
import pyodbc, time, uuid, datetime

wb = openpyxl.load_workbook(r'To_RDS_Database_Jan_2020.xlsx')
sheet = wb['Sheet3']


def updateDataMaster(ID, Name):
    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.51;DATABASE=RDI;UID=kiransa;PWD=Password123')

    cursor = conn.cursor()
    sql = "update DatasetMaster set DataFileName = '" + Name + "' where ID =" + str(ID) + " and  CreatedBy = 'Sameer'"

    cursor.execute(sql)
    conn.commit()
    conn.close()


def getID(metadataID):
    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.51;DATABASE=RDI;UID=kiransa;PWD=Password123')
    cursor = conn.cursor()
    sql = "SELECT ID from DatasetMaster where MetadataID = " + str(metadataID)
    cursor.execute(sql)
    myResult = cursor.fetchone()
    conn.commit()
    conn.close()
    return myResult[0]


def makePublic(ID):
    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.51;DATABASE=RDI;UID=kiransa;PWD=Password123')

    cursor = conn.cursor()
    #  GroupID = 1 for public
    #  GroupID = 2 for within icimod internal
    #  GroupID = 14 for Atmoshpere

    sql = "INSERT INTO ShareInGroups (DatasetID, GroupID, Status, SharedBy, ApprovedBy) VALUES (" + str(
        ID) + ",2, 1, Null, Null)"

    cursor.execute(sql)
    conn.commit()
    conn.close()


def getUUID(metadataID):
    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.51;DATABASE=RDI;UID=kiransa;PWD=Password123')
    cursor = conn.cursor()
    sql = "SELECT GUID from DatasetMaster where MetadataID = " + str(metadataID)
    cursor.execute(sql)
    myResult = cursor.fetchone()
    conn.commit()
    conn.close()
    return myResult[0]


def checkDuplicate(metadataID):
    # conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.67;DATABASE=RDI;UID=kiransa;PWD=Password123')

    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.51;DATABASE=RDI;UID=kiransa;PWD=Password123')
    cursor = conn.cursor()
    sql = "select * from DatasetMaster where MetadataID = " + str(metadataID)
    cursor.execute(sql)
    data = cursor.fetchall()
    if len(data) == 0:
        return "False"
    else:
        return "True"


def putFileName(fName, myID):
    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.51;DATABASE=RDI;UID=kiransa;PWD=Password123')
    cursor = conn.cursor()
    sql = "UPDATE DatasetMaster set DataFileName ='" + str(fName) + "',DataFileExt = 'zip' where ID = " + str(myID)
    cursor.execute(sql)
    # myResult = cursor.fetchone()
    conn.commit()
    conn.close()


def metadata_insert_mssql(title, metadataid, metdatauuid, datafile, mydate, uuid, themeid, ownergroupid):
    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.51;DATABASE=RDI;UID=kiransa;PWD=Password123')
    cursor = conn.cursor()
    # sql = "update DatasetMaster set themeID = 7 where MetadataID = " + str(title)
    sql = ""
    try:
        # sql = "Apple"
        sql = "insert into DatasetMaster "
        sql = sql + "(Title, DataFileName, DataFileExt, GUID, OwnerGroupID, MetadataFileName, MetadataID, MetadataUUID,"
        sql = sql + "MetadataSchema, FilePath, GeodataPath, DisplayPath, DataTable, isMetadataPublic, ThemeID, CreatedDate,"
        sql = sql + "CreatedBy,isDeleted) VALUES "
        sql = sql + "('" + title + "',"
        sql = sql + "'" + datafile + "',"
        sql = sql + "'" + 'zip' + "',"
        sql = sql + "'" + uuid + "',"
        sql = sql + str(ownergroupid) + ","
        sql = sql + 'NULL' + ","
        sql = sql + str(metadataid)
        sql = sql + ",'" + metdatauuid + "',"
        sql = sql + "'" + 'iso19139' + "',"
        sql = sql + 'NULL' + ","
        sql = sql + 'NULL' + ","
        sql = sql + 'NULL' + ","
        sql = sql + 'NULL' + ","
        sql = sql + "'" + str(1) + "',"
        sql = sql + str(themeid) + ","
        sql = sql + "'" + mydate + "',"
        sql = sql + "'" + 'Sameer' + "',"
        sql = sql + 'NULL' + ")"
    except:
        print(sql)

    cursor.execute(sql)
    conn.commit()
    conn.close()


def renameMove(fName, uuid):
    newName = str(fName) + str(uuid)
    old = "D:\\temp\\data\\" + fName + ".zip"
    new = "D:\\temp\\newdata\\" + newName + ".zip"
    os.rename(old, new)
    print("Success")


def forExcel():
    for row in range(2, sheet.max_row + 1):
        dataTitle = sheet['A' + str(row)].value
        metadataId = sheet['C' + str(row)].value
        metadataUUID = sheet['B' + str(row)].value
        FileName = sheet['D' + str(row)].value
        getDate = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        # print str(dataId) + " : " + str(FileName)
        # datafile = sheet['C' + str(row)].value
        # datafileext = 'zip' #sheet['D' + str(row)].value
        # guid = sheet['E' + str(row)].value
        ownergroupid = sheet['E' + str(row)].value
        # metadatafilename = sheet['G' + str(row)].value
        # metadataid = sheet['H' + str(row)].value
        # metdatauuid = sheet['I' + str(row)].value
        # metadataschema = 'eml-gbif' #sheet['J' + str(row)].value
        # filepath = sheet['K' + str(row)].value
        # geodatapath = sheet['L' + str(row)].value
        # displaypath = sheet['M' + str(row)].value
        # datatable = sheet['N' + str(row)].value
        # ismetadatapublic = 1 #sheet['O' + str(row)].value
        themeid = sheet['F' + str(row)].value
        # createddate = sheet['Q' + str(row)].value
        # createdby = sheet['R' + str(row)].value
        # isdeleted = sheet['S' + str(row)].value

        ##    test()
        # metadata_insert_mssql(title)
        # updateDataMaster(dataId, FileName)
        # makePublic(dataId)

        # myID = getID(int(metadataId))
        # makePublic(myID)

        if (checkDuplicate(metadataId) == "False"):
            myUUID = str(uuid.uuid4())
            metadata_insert_mssql(dataTitle, metadataId, metadataUUID, FileName, str(getDate), myUUID, themeid,
                                  ownergroupid)
        else:
            myUUID = getUUID(int(metadataId))
        myID = getID(int(metadataId))
        # makePublic(myID)
        renameMove(FileName, myUUID)
        putFileName(FileName, myID)

    ##    print(title, datafile, datafileext, guid, ownergroupid, metadatafilename, metadataid,
    ##          metdatauuid, metadataschema, filepath, geodatapath, displaypath, datatable, ismetadatapublic,
    ##          themeid, createddate, createdby, isdeleted)
    ##    print("======================")


forExcel()
# makePublic(36015)