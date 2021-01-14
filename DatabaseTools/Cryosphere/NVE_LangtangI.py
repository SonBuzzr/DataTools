import requests, openpyxl, pyodbc
from openpyxl import Workbook

params= ['Snow dpeth','Air temperatur','Relativ humidity','Ground temperatur','Precipitation - Tipping bucket (acc)','Battery voltage']
dParam= ['snowDpeth_cm','airTemperatur_C','relativeHumidity_per','groundTemperatur_C','precipitationTippingBucketAcc_mm','batteryVoltage_V']
IDs = ['1977.1.1.2002.1','1977.1.1.17.1','1977.1.1.2.1','1977.1.1.9153.1','1977.1.1.9301.1','1977.1.1.9100.1']
vDate=[]
vTime=[]
vData=[]
v0=[]
v1=[]
v2=[]
v3=[]
v4=[]
v5=[]
v6=[]
v7=[]
v8=[]
v9=[]
v10=[]
v11=[]
v12=[]
v13=[]
v14=[]
v15=[]
v16=[]


def writeXML():
    wb = openpyxl.load_workbook(r"E:\1.CODES\cryosphere\NVE.xlsx")
    sheet = wb.active
    sheet.append(['Date', 'Time', 'Air pressure','Ground temperatur','Wind speed (avg)','Wind speed (Max)','Wind direction','Shortware radiation in','Shortware radiation out','Longwave radiation in','Logwave radiation out','Relative humidity','Precipitaion - Collecting gauge (acc)','Snow dpeth','Air temperatur','Water equivalent (Potassiuma attenuation) ','Water equivalent (Thallium attenuation) ','Precipitation - Tipping bucket (acc)','Battery voltage'])
    for j in range(0, len(v0)):
        col1 = vDate[j]
        col2 = vTime[j]
        col3 = v0[j]
        col4 = v1[j]
        col5 = v2[j]
        col6 = v3[j]
        col7 = v4[j]
        col8 = v5[j]
        col9 = v6[j]
        col10 = v7[j]
        col11 = v8[j]
        col12 = v9[j]
        col13 = v10[j]
        col14 = v11[j]
        col15 = v12[j]
        col16 = v13[j]
        col17 = v14[j]
        col18 = v15[j]
        col19 = v16[j]
        sheet.append([col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19])
    wb.save(r"E:\1.CODES\cryosphere\NVE_GangaLa.xlsx")
    wb.close()

def myConn():
    #return pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=KIRANS10-PC\SQLEXPRESS;" "Database=dbCrosphere;" "Trusted_Connection=yes;")
    return pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=192.168.10.67;DATABASE=dbCryosphere;UID=cryo;PWD=Cryo123##.')

def updateData(data, index):
    try:
        onlyTime = ((data.split(',')[0]).split(' ')[1]).replace('.', ':')[:5]
        onlyDate1 = ((data.split(',')[0]).split(' ')[0]).split('.')
        onlyDate = onlyDate1[2] + "-" + onlyDate1[1] + "-" + onlyDate1[0]
    except:
        pass
    try:
        myData = str(data.split(',')[1]) + str(data.split(',')[2])
    except:
        myData = str(data.split(',')[1])
    # for i in range (0, len(vDate)):
    try:
        cnxn = myConn()
        cursor = cnxn.cursor()
        query = """ UPDATE NVE_SNOWAMP_LangtangLower_I SET """ + dParam[index] + """ = """ + myData \
                + """ where  dataDate ='""" + str(onlyDate)  + """' and  dataTime='""" + str(onlyTime) + """'"""

        cursor.execute(query)
        cursor.commit()
        cursor.close()
        cnxn.close()
    except:
        print ("Error at " + query)
        pass

def insertData():
    for i in range (0, len(vDate)):
        try:
            cnxn = myConn()
            cursor = cnxn.cursor()
            query = """ INSERT INTO NVE_SNOWAMP_LangtangLower_I(dataDate,dataTime) 
            VALUES ('""" + str(vDate[i]) + """','""" + str(vTime[i]) + """')"""
            cursor.execute(query)
            cursor.commit()
            cursor.close()
            cnxn.close()
        except:
        # except pyodbc.Error as err:
        #     print ("Error at " + err)
            print ("Error at : " + query)
            pass

def getDateTime(data):
    try:
        onlyTime = ((data.split(',')[0]).split(' ')[1]).replace('.', ':')[:5]
        onlyDate1 = ((data.split(',')[0]).split(' ')[0]).split('.')
        onlyDate = onlyDate1[2] + "-" + onlyDate1[1] + "-" + onlyDate1[0]

        vDate.append(onlyDate)
        vTime.append(onlyTime)
    except:
        pass

def getParamsVal(data, myArray):
    try:
        onlyTime = ((data.split(',')[0]).split(' ')[1]).replace('.', ':')[:5]
        onlyDate1 = ((data.split(',')[0]).split(' ')[0]).split('.')
        onlyDate = onlyDate1[2] + "-" + onlyDate1[1] + "-" + onlyDate1[0]
        try:
            myData = str(data.split(',')[1]) + str(data.split(',')[2])
        except:
            myData = str(data.split(',')[1])

        if myArray == 0:
            vDate.append(onlyDate)
            vTime.append(onlyTime)
        if myArray == 0:
            v0.append(myData)
            exit()
        if myArray == 1:
            v1.append(myData)
            exit()
        if myArray == 2:
            v2.append(myData)
            exit()
        if myArray == 3:
            v3.append(myData)
            exit()
        if myArray == 4:
            v4.append(myData)
            exit()
        if myArray == 5:
            v5.append(myData)
            exit()
        if myArray == 6:
            v6.append(myData)
            exit()
        if myArray == 7:
            v7.append(myData)
            exit()
        if myArray == 8:
            v8.append(myData)
            exit()
        if myArray == 9:
            v9.append(myData)
            exit()
        if myArray == 10:
            v10.append(myData)
            exit()
        if myArray == 11:
            v11.append(myData)
            exit()
        if myArray == 12:
            v12.append(myData)
            exit()
        if myArray == 13:
            v13.append(myData)
            exit()
        if myArray == 14:
            v14.append(myData)
            exit()
        if myArray == 15:
            v15.append(myData)
            exit()
        if myArray == 16:
            v16.append(myData)
            exit()
    except:
        pass

for i in range(0, len(IDs)):
    response = requests.get("http://h-web01.nve.no/chartserver/ShowData.aspx?req=getchart&ver=1.0&time=-1;0&chd=ds=htsr,da=29,id=" + IDs[i] + ",rt=0&mth=inst&vfmt=text")
    if response.status_code == 200:
        data = (response.text).split('<br />')
        if len(str(data[i]).strip()) > 3:
            for k in range(1, len(data)):
                print (data[k])
                if len(str(data[k])) > 0:
                    getDateTime(data[k])
            insertData()
            for k in range(1, len(data)):
                print (data[k])
                if len(str(data[k])) > 0:
                    updateData(data[k], i)







