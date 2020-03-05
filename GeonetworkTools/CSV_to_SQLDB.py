import dbconfig as dbc
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, ForeignKey, select, bindparam

db_user = dbc.LOCALHOST['user']
db_password = dbc.LOCALHOST['password']
db_host = dbc.LOCALHOST['host']
db_port = dbc.LOCALHOST['port']
db_database = dbc.LOCALHOST['database']
driver = dbc.LOCALHOST['driver']


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

        metadata = MetaData()
        users = Table('users', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String(50)),
                      Column('fullname', String(100))
                      )

        addresses = Table('addresses', metadata,
                          Column('id', Integer, primary_key=True),
                          Column('user_id', None, ForeignKey('users.id')),
                          Column('email_address', String(50), nullable=False)
                          )
        metadata.create_all(self.db_connect)

        # Insert into Table
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

        # Select statement
        # select_table = select([users])
        select_table = select([users, addresses]).where(users.c.id == addresses.c.user_id)
        result = self.db_connect.execute(select_table)

        for row in result:
            print("name:", row[users.c.name], "; fullname:", row[users.c.fullname])

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

        update_table = select([addresses.c.email_address]). \
            where(addresses.c.user_id == users.c.id). \
            limit(1)
        self.db_connect.execute(users.update().values(fullname=update_table))

        # Delete satement
        # self.db_connect.execute(users.delete().where(users.c.name > 'm'))

        try:
            print('Your connection is Ok \nConnection object is: {}'.format(self.db_connect))
        except IOError:
            print('Connection problem')

    def read_table(self):
        inspector = inspect(self.db_driver)
        for table in inspector.get_table_names():
            for column in inspector.get_column(table):
                print("Column: %s" % column['name'])


D1 = Database()
