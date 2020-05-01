import pyodbc


# select query from moduledata table
def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select top 5 * from moduledata")
    for row in cursor:
        print(f'row = {row}')
    print()


# insert query
def insert(conn):
    # print("Read")
    cursor = conn.cursor()
    query = "INSERT INTO [dbo].[moduledata]\
           ([SN],[ModuleNumber],[Manufacturer],[Product],[CalModule],[CalibrationTime],[CalFactor],[Voc],[Isc],[Pmp],[Vmp],[Imp],[FF],[Irradiance]\
           ,[Vload],[IAtVload],[PowerAtVload],[CellEff],[ModuleEff],[Tamb],[Tref],[Classification],[SlopeAtVoc],[SlopeAtIsc],[Time],[Operator]\
           ,[Notes],[LotName],[LotNotes],[Idiff],[Irec],[Rshunt],[Rser],[Isun],[TempCorrAlpha],[TempCorrBeta],[TempCorrCurve],[TempCorrSeriesR]\
           ,[ModuleLength],[ModuleWidth],[CellArea],[CellsParallel],[CellsSerial],[ProductVoc],[ProductIsc],[ProductFF],[ProductPmax],[ProductPpass]\
           ,[TargetTemperature],[Bin],[CalMethod])\
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);,\
            (N'2002277671C',NULL,N'SILFAB',N'SIL380NT5EWM4C',N'Silfab 60SLA300-SEC-1701260140O',CAST(GETDATE()AS  DateTime)\
            ,1,48.8,10.1,383.6,40.0,9.6,74.43712556,1000,NULL,NULL,NULL,21.26698639,19.19301582,28.18935484,27.63032258,N'SIL380NT5EWM4C',\
            0.55074489,78.45927965,CAST(GETDATE()AS DateTime),N'SOLVIS PANEL',NULL, N'MASS DECLARATION',NULL,0,0,0,0,0,15.73,-1.57,\
            -0.1,-0.001,1.65,0.99,0.02457,1,60,38.58,9.4,76.61,305,270,25,NULL,NULL)"
    cursor.execute(query)
    conn.commit()


# Database connection to SQL server
conn = pyodbc.connect(
    "Driver={SQL Server Native client 11.0};"
    "Server=nav64;"
    "Database=QuickSun;"
    "Trusted_Connection=yes;"
)

print("Database Connected...")
read(conn)
