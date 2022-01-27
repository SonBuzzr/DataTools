import os
import sys
import csv
import pyodbc

#### Path to the folder ####
path = r'afg_glacier_glims'
ext = '.csv'

#### Database connection ####
server = 'SAMEERB10-PC'
database = 'db_afg_gl_lake'
table_name = 'db_afg_glakes_1990_2015'
username = 'user1'
password = 'password' ## Random Password ##

##### SQL QUERY #####
##### CHECK DUPLICATE QUERY #####
check_query = '''SELECT * FROM ''' + table_name + ''' WHERE GLIMS_ID = ?;'''

##### SELECT QUERY #####
select_query = '''SELECT top 5 * FROM ''' + table_name + ''';'''

##### INSERT QUERY #####
# insert_query = '''INSERT INTO ''' + table_name + '''(
#     [serial_number_nest_1], [test_time], [imax], [isc], [pmax], [rs],
#     [rsh], [vmax], [voc], [module_grade], [nest_1_test_pass],[nest_1_test_fail],
#     [pack_location], [part_in_nest_1], [part_type], [print_done], [print_manual], [print_reject],
#     [safety_zone_ok], [reconciled], " " [ff], [stemp], [psun], [hpv],
#     [hpa], [irr])
#     VALUES
#     (?, CAST(GETDATE()AS DateTime), ?, ?, ?, 0,
#     0, ?, ?, 380, 0, 0,
#     0, 0, 52, 0, 0, 0,
#     0, 0, NULL, NULL, NULL, NULL,
#     NULL, NULL)
#     '''

insert_query = '''INSERT INTO ''' + table_name + '''([GLIMS_ID])
                VALUES 
                (?);'''
### Sample query ###
insert_query_sample1 = '''INSERT INTO ''' + table_name + '''([id], [name], [lastname], [age], [email], [mobile])
                VALUES 
                (?, ?, 'Don', ?, 'test@mail.com', 9845634567);'''

insert_query_sample2 = '''INSERT INTO ''' + table_name + '''([id], [test_time])
                VALUES 
                (?, CAST(GETDATE()AS DateTime));'''

##### UPDATE QUERY #####
update_query = '''UPDATE ''' + table_name + ''' SET FirstName = ? WHERE id = ? and FirstName = ?;'''
update_query_gl = '''UPDATE ''' + table_name + ''' SET
                                                 [M_Basin_2015] = ?,
                                                 [Basin_2015]= ?,
                                                 [Sub_Basin_2015]= ?,
                                                 [GLIMS_ID_2015]= ?,
                                                 [Area_2015]= ?,
                                                 [Type_2015]= ?,
                                                 [Altitude_2015]= ?,
                                                 [ID_2015]= ?,
                                                 [Gfed_2015]= ?,
                                                 [Gdist_2015]= ?
                                                 WHERE [GLIMS_ID] = ?;'''

##### Database connection to SQL server #####
conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=' + server + ';'
                         'Database=' + database + ';'
                                                  'Trusted_Connection=yes;')
cursor = conn.cursor()


##### Check for Duplicate Rows #####
def check_duplicate(value):
    cursor.execute(check_query, value)
    row = cursor.fetchall()
    if len(row) == 0:
        return "False"
    else:
        return "True"


##### SELECT module definition #####
def db_select():
    print("Select from Table\n")
    cursor.execute(select_query)
    for row in cursor:
        print('row = {}'.format(row))


##### INSERT module definition #####
def db_insert(*args):
    # print("Insert into Table")
    # print(type(args[0]))
    try:
        if check_duplicate(args[0]) == "False":
            cursor.execute(insert_query, args)
            # print(args)
            print("Updating new row with id: {}".format(args[0]))
            conn.commit()
        else:
            print("Record Found in Database: {}".format(args[0]))
    except pyodbc.Error as ex:
        conn.rollback()
        print(ex.args[1])


##### UPDATE module definition #####
def db_update(*args):
    print("Updating row with id: {}".format(args[1]))
    # print(insert_query,args)
    try:
        # print(update_query_gl, args)
        cursor.execute(update_query_gl, args)
        conn.commit()


    except pyodbc.Error as ex:
        conn.rollback()
        print("Error Occured: ", ex.args[1])


##### Read files #####
def read_files(filename):
    count = 0
    with open(filename, 'r') as f:
        csv_data = csv.reader(f, delimiter=',')
        for row in csv_data:
            count += 1
            output = (', '.join(row))

            ##### LIST OUT ALL REQUIRE COLUMN FROM CSV #####
            mbasin = str(output.split(',')[1])
            basin = str(output.split(',')[2])
            subbasin = str(output.split(',')[3])
            glimsid = str(output.split(',')[5])
            area = str(output.split(',')[6])
            type = str(output.split(',')[8])
            altitude = str(output.split(',')[9])
            gid = str(output.split(',')[10])
            gfed = str(output.split(',')[11])
            gdis = str(output.split(',')[12])

            print(mbasin, basin, subbasin, glimsid, area, type, altitude, gid, gfed, gdis, glimsid)

        ##### CALL DATABASE QUERY MODULE #####
            # db_insert(sn)
        # db_insert(sn, impp, isc, pmpp, umpp, uoc)
        # db_insert(4, 'Rita', 29)
        #     db_update("Sameer",1, "Tim")
            db_update(mbasin, basin, subbasin, glimsid, area, type, altitude, gid, gfed, gdis, glimsid)
        #     db_select()
        # print("{}{}".format(col1, col2))
        print("{} \nRow Count = {}".format(filename, count))


#### Opening a directory and listing all files with provided extension ####
for r, d, f in os.walk(path):
    for file in f:
        if ext in file:
            csv_file = os.path.join(r, file)
            read_files(csv_file)
            # print(csv_file)

# db_select()

conn.close()
print("\nDatabase connection closed...")
