import pyodbc, datetime

def myConn():
    return pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=KIRANS10-PC\SQLEXPRESS;" "Database=dbCrosphere;" "Trusted_Connection=yes;")

def insertDate():
    cnxn = myConn()
    cursor = cnxn.cursor()
    # query = "INSERT INTO NVE_SNOWAMP_GangaLa(dataDate,dataTime,airPressure_hPa,groundTemperatur_C,wndSpeedAvg_m__s,windSpeedMax_m__s,windSirection_degree," \
    #         "shortwareRadiationIn_W__m2,shortwareRadiationOut_W__m2,longwaveRadiationIn_W__m2,logwaveRadiationOut_W__m2,relativeHumidity_per," \
    #         "precipitaionCollectingGaugeAcc_mm,snowDpeth_cm,airTemperatur_C,waterEquivalentPotassiumaAttenuation__m,waterEquivalentThalliumAttenuation_m," \
    #         "precipitationTippingBucketAcc_mm,batteryVoltage_V) VALUES " \
    #         "()"
    # query = "INSERT INTO NVE_SNOWAMP_GangaLa(dataDate,dataTime,airPressure_hPa) " \
    #         "VALUES ('" + str(datetime.datetime.now()) + "','" + str(datetime.datetime.now().time()) + "',55.55)"
    query = """ INSERT INTO NVE_SNOWAMP_GangaLa(dataDate,dataTime,airPressure_hPa) VALUES ('2020-11-11 12:14:42.851622','12:14',55.55)"""
    cursor.execute(query)
    cursor.commit()
    cursor.close()
    cnxn.close()



insertDate()