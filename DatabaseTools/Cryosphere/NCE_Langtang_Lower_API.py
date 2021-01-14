import requests, openpyxl
from openpyxl import Workbook

params= ['Snow dpeth','Air temperatur','Relativ humidity','Ground temperatur','Precipitation - Tipping bucket (acc)','Battery voltage']
# IDs = ['1977.1.1.2002.1','1977.1.1.17.1','1977.1.1.2.1','1977.1.1.9153.1','1977.1.1.9301.1','1977.1.1.9100.1']
IDs = ['1977.1.3.2002.1','1977.1.3.17.1','1977.1.3.2.1','1977.1.3.9153.1','1977.1.3.9301.1','1977.1.3.9100.1']
vDate=[]
vTime=[]
vData=[]
v0=[]
v1=[]
v2=[]
v3=[]
v4=[]
v5=[]

def writeXML():
    wb = openpyxl.load_workbook(r"E:\1.CODES\cryosphere\NVE.xlsx")
    sheet = wb.active
    sheet.append(['Date', 'Time', 'Snow dpeth','Air temperatur','Relativ humidity','Ground temperatur','Precipitation - Tipping bucket (acc)','Battery voltage'])
    for j in range(0, len(v0)):
        col1 = vDate[j]
        col2 = vTime[j]
        col3 = v0[j]
        col4 = v1[j]
        col5 = v2[j]
        col6 = v3[j]
        col7 = v4[j]
        col8 = v5[j]
        sheet.append([col1,col2,col3,col4,col5,col6,col7,col8])
    wb.save(r"E:\1.CODES\cryosphere\NVE_LangtangLower_2.xlsx")
    wb.close()

def getParamsVal(data, myArray):
    try:
        onlyTime = ((data.split(',')[0]).split(' ')[1]).replace('.', ':')[:5]
        onlyDate = ((data.split(',')[0]).split(' ')[0]).replace('.', '-')
        try:
            myData = str(data.split(',')[1]) + ',' + str(data.split(',')[2])
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
    except:
        pass

for i in range(0, len(IDs)):
    response = requests.get("http://h-web01.nve.no/chartserver/ShowData.aspx?req=getchart&ver=1.0&time=-9;0&chd=ds=htsr,da=29,id=" + IDs[i] + ",rt=0&mth=inst&vfmt=text")
    if response.status_code == 200:
        data = (response.text).split('<br />')
        if len(str(data[i]).strip()) > 3:
            for k in range(1, len(data)):
                print(data[k])
                if i == 11:
                    print("Here")
                getParamsVal(data[k], i)
writeXML()
print ("Next")






