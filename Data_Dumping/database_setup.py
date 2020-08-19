import cx_Oracle
import pymysql
from sqlalchemy import create_engine


# # Connection to oracle db
def connect_oracle(credentials):
    dsn = cx_Oracle.makedsn(credentials['host'], credentials['port'], sid=credentials['sid'])
    connection = cx_Oracle.connect(credentials['username'], credentials['password'], dsn)
    return connection


def ask_oracle():
    host = input('\nPlease enter the host number: like: 127.0.0.1\n')
    port = input('\nPlease enter the port: like: 1521\n')
    sid = input('\nPlease enter the sid: like: ORACLCDB\n')
    user = input('\nPlease enter the username: like: test_user\n')
    password = input('\nPlease enter the password: like: password\n')

    oracle_connection = {'host': host, 'port': port, 'sid': sid,
                         'username': user,
                         'password': password}
    connection = connect_oracle(oracle_connection)
    return connection


def ask_mysql():
    db_name = input('\nPlease enter the db name: like: master\n')
    host = input('\nPlease enter the host number: like: 127.0.0.1\n')
    user = input('\nPlease enter the username: like: test_user\n')
    port = input('\nPlease enter the port: like: 1521\n')
    password = input('\nPlease enter the password: like: password\n')
    # = create_engine(
      #  "mssql+pymssql://{}:{}@localhost/{}".format(user, password,
                                                   # db_name))
    engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(user, 
                                                         password, host, port, db_name))
    return engine


def ask_postgre():
    host = input('\nPlease enter the host number: like: 127.0.0.1\n')
    db_name = input('\nPlease enter the db name: like: master\n')
    user = input('\nPlease enter the username: like: test_user\n')
    password = input('\nPlease enter the password: like: password\n')
    db_string = "postgres+psycopg2://{}:{}@{}/{}".format(user, password,
                                                         host,
                                                         db_name)
    engine = create_engine(db_string)
    return engine
