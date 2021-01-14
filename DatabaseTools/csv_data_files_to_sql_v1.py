import os
import csv
import pyodbc
import logging
import datetime

logFile= datetime.datetime.now().strftime("data_log_%H%M%S_%d_%m_%Y.log")
##print(logFile)

logging.basicConfig(
    filename=logFile,
    level=logging.INFO,
    format="%(asctime)s: %(levelname)s: \n%(message)s",
)

##path = "data"
path =  r'\\192.168.10.67\dataset\AQMS\Stations\Dhulikhel(50)'
#\\192.168.10.67\dataset\AQMS\Stations\Dhulikhel(50)
##192.168.10.67\dataset\AQMS\Stations\Chitwan(36)
ext = ".csv"

str_date = datetime.datetime.strptime('2016-10-19', '%Y-%m-%d').date()
last_date = datetime.datetime.strptime('2019-02-07', '%Y-%m-%d').date()

##conn = pyodbc.connect(
##    r"DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=Atmosphere;UID=sa;PWD=Password123"
##)

conn = pyodbc.connect(
        r"DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.67;DATABASE=dbAtmosphere;Trusted_Connection=yes;"
    )

cursor = conn.cursor()

##def csv_to_mssql():
##    conn = pyodbc.connect(
##        r"DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=Atmosphere;UID=sa;PWD=Password123"
##    )
##
##    cursor = conn.cursor()
##
##    sql = (
##        "insert into dataAQMS(stationID, acqDate, acqTime, paramName,\
##            paramCode, value) values \
##            ('"
##        + stationID
##        + "',\
##            '"
##        + acqdate
##        + "',\
##            '"
##        + acqtime
##        + "',\
##            '"
##        + paramname
##        + "',\
##            '"
##        + paramcode
##        + "',\
##            '"
##        + value
##        + "')"
##    )
##
##    try:
##        cursor.execute(sql)
##        conn.commit()
##
##    except pyodbc.Error as ex:
##        conn.rollback()
##        sqlstate = ex.args[1]
##        print(sqlstate)


def read_csv(file_name):
    with open(file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        folder_path = os.path.dirname(file_name)
        folder_name = folder_path.split("\\")
        
        f_name =  folder_name[-2].split("(")
        print(f_name[0])
        logging.info("\nFolder: {} \nProcessing file: {} :".format((folder_name[-2]), file_name))
##        print("\nFolder :{} \nProcessing file: {} :".format((folder_name[-1]), file_name))
        
        for line in csv_reader:
            stationID = str(f_name[0].lower()) + "_AQMS_00"
##            stationID = "chitwan_AQMS_00"
            acqdate = str(line[0])
            acqtime = str(line[1])
            paramname = str(line[2])
            paramcode = str(line[3])
            value = str(line[4])
##            print(stationID, acqdate, acqtime, paramname, paramcode, value)

            sql = (
                "insert into dataAQMS(stationID, acqDate, acqTime, paramName,\
                        paramCode, value) values \
                        ('"
                + stationID
                + "',\
                        '"
                + acqdate
                + "',\
                        '"
                + acqtime
                + "',\
                        '"
                + paramname
                + "',\
                        '"
                + paramcode
                + "',\
                        '"
                + value
                + "')"
            )
            try:
                cursor.execute(sql)
                conn.commit()
##                print("Successfull")
                
            except pyodbc.Error as ex:
                conn.rollback()
                sqlstate = ex.args[1]
                logging.info('\nError occured in file: {}: \nDated {} at time:{}\n: Param Name:{} :\n{}'.format(file_name,acqdate,acqtime,paramname,sqlstate))
                print('\nError occured in file: {}: \nDated {}: Param Name:{} :\n{}'.format(file_name,acqdate,paramname,sqlstate))
    print("Completed")
            
def get_files(path, ext):
    for r, d, f in os.walk(path):

        ##        for folder in d:
        ##            print(folder)
        for file in f:
            if ext in file:
                file_name = datetime.datetime.strptime(file[:-4], '%Y-%m-%d').date()
                if file_name>str_date and file_name<last_date:
                    read_file = os.path.join(r, file)
                    read_csv(read_file)


if __name__ == "__main__":
    get_files(path, ext)
