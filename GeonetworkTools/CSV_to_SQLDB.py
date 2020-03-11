import dbconfig as dbc
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, ForeignKey, select, bindparam, \
    text
import CSV_Read_Write as reader

csvFile = 'glacier_doi_update.csv'
server = dbc.SERVER

db_user = server['user']
db_password = server['password']
db_host = server['host']
db_port = server['port']
db_database = server['database']
driver = server['driver']


# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
# DB_CONNECT = 'mssql+pyodbc://sa:P@ssw0rd@localhost:1433/Testdb?driver=ODBC+Driver+17+for+SQL+Server'
# db_connect = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver={}'.format(
#     db_user, db_password, db_host, db_port, db_database, driver)
#
# # connecting to MSSQL server at localhost
# ENGINE = create_engine(db_connect, echo=True)
#
# conn = ENGINE.connect()
#
# try:
#     print('Your connection is Ok \nConnection object is: {}'.format(conn))
# except:
#     print('Connection problem')


class Database:
    def __init__(self):
        self.db_driver = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver={}'.format(
            db_user, db_password, db_host, db_port, db_database, driver)
        self.db_engine = create_engine(self.db_driver)
        self.db_connect = self.db_engine.connect()

        self.metadata = MetaData()

        try:
            print('Connected to Database')
        except IOError:
            print('Connection Error', IOError)

    # Select statement
    def select_table(self, args):
        tbl_name = Table(args, self.metadata, autoload=True, autoload_with=self.db_engine)
        stmt = select([tbl_name])
        print(stmt)

        results = self.db_connect.execute(stmt).fetchmany(size=100)
        for row in results:
            print(row)

            # select_table = select([users])
        # result = self.db_connect.execute(select_table)
        # for row in result:
        #     print(row)
        # select_table = select([users, addresses]).where(users.c.id == addresses.c.user_id)
        # result = self.db_connect.execute(select_table)
        #
        # for row in result:
        #     print("name:", row[users.c.name], "; fullname:", row[users.c.fullname])

        # Update statement
        # update_table = users.update(). \
        #     values(fullname="Fullname:" + users.c.name)

        # update_table = users.update(). \
        #     where(users.c.name == 'jack'). \
        #     values(name='ed')

        # self.db_connect.execute(update_table)

        # update_table = users.update().\
        #     where(users.c.name == bindparam('oldname')).\
        #     values(name=bindparam('newname'))
        #
        # self.db_connect.execute(update_table,[
        #     {'oldname':'jack', 'newname': 'ed'},
        #     {'oldname': 'wendy', 'newname': 'mary'},
        #     {'oldname': 'jim', 'newname': 'jake'}
        # ])

        # update_table = select([addresses.c.email_address]). \
        #     where(addresses.c.user_id == users.c.id). \
        #     limit(1)
        # self.db_connect.execute(users.update().values(fullname=update_table))

        # Delete satement
        # self.db_connect.execute(users.delete().where(users.c.name > 'm'))

    # List all table from Database
    def list_table(self):
        inspect_database = inspect(self.db_engine)
        db_list = inspect_database.get_table_names()
        return db_list

    # Insert into Table
    def insert_table(self, args, **kwargs):
        tbl_name = Table(args, self.metadata, autoload=True, autoload_with=self.db_engine)
        # Insert into Table
        ins = tbl_name.insert().values(kwargs)
        self.db_connect.execute(ins)

        # ins = users.insert()
        # self.db_connect.execute(ins, id=2, name='wendy', fullname='Wendy Williams')

        # self.db_connect.execute(addresses.insert(),[
        #     {'user_id': 1, 'email_address': 'jack@yahoo.com'},
        #     {'user_id': 1, 'email_address': 'jack@msn.com'},
        #     {'user_id': 2, 'email_address': 'www@www.org'},
        #     {'user_id': 2, 'email_address': 'wendy@aol.com'},
        # ])

        # ins = users.insert().values(name='jack', fullname='Jack Jones')
        # self.db_connect.execute(ins)

        # ins = users.insert()
        # self.db_connect.execute(ins, id=2, name='wendy', fullname='Wendy Williams')

        # self.db_connect.execute(addresses.insert(),[
        #     {'user_id': 1, 'email_address': 'jack@yahoo.com'},
        #     {'user_id': 1, 'email_address': 'jack@msn.com'},
        #     {'user_id': 2, 'email_address': 'www@www.org'},
        #     {'user_id': 2, 'email_address': 'wendy@aol.com'},
        # ])

    def create_table(self, args):

        Table(args, self.metadata,
              Column('id', Integer, primary_key=True),
              Column('metadata_id', Integer, nullable=False, unique=True),
              Column('metadata_uuid', String(100))
              )
        # users = Table('users', metadata,
        #               Column('id', Integer, primary_key=True),
        #               Column('name', String(50)),
        #               Column('fullname', String(100))
        #               )
        #
        # addresses = Table('addresses', metadata,
        #                   Column('id', Integer, primary_key=True),
        #                   Column('user_id', None, ForeignKey('users.id')),
        #                   Column('email_address', String(50), nullable=False)
        #                   )

        self.metadata.create_all(self.db_connect)


db = Database()
table_name = 'DatasetDOI'
tables = db.list_table()
# db.create_table(table_name)
# db.insert_table(table_name)
# db.select_table(table_name)

csvData = reader.readCSV_pd(csvFile)

# for chunk in csvData:

# m_uuid = chunk['UUID']

# db.insert_table(table_name, metadata_id=m_id, metadata_uuid=m_uuid)


for index, row in csvData.iterrows():
    m_id = row['Metadata ID']
    m_uuid = row['UUID']
    # print(m_id, m_uuid)
    db.insert_table(table_name, MetadataID=m_id)
