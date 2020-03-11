from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, ForeignKey, select, bindparam, \
    func
import dbconfig as dbc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_user = dbc.LOCALHOST['user']
db_password = dbc.LOCALHOST['password']
db_host = dbc.LOCALHOST['host']
db_port = dbc.LOCALHOST['port']
db_database = dbc.LOCALHOST['database']
driver = dbc.LOCALHOST['driver']

db_engine = create_engine(driver)

connection = db_engine.connect()
stmt = select([users])
