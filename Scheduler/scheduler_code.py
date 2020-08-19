import pandas as pd

import database_setup


def mysql_syntax(diff, tablename, order):
    query = 'select top {} * from {} order by {} desc'.format(diff, tablename, order)
    return query


def postgre_syntax(diff, tablename, order):
    query = 'select * from {} order by {} desc limit {}'.format(tablename, order, diff)
    return query


def oracle_syntax(diff, tablename, order):
    query = '''SELECT *
FROM (select * from {} ORDER BY {} DESC) suppliers2
WHERE rownum <= {}
ORDER BY rownum DESC'''.format(tablename,order,diff)
    return query


if __name__ == '__main__':
    db_type = input("Please enter client's db: mysql, postgresql, oracle\n")
    db_type = db_type.lower()
    if db_type == 'oracle':
        engine_client = database_setup.ask_oracle()

    if db_type == 'mysql':
        engine_client = database_setup.ask_mysql()

    if db_type == 'postgresql':
        engine_client = database_setup.ask_postgre()

    db_type_our = input("Please enter your db: mysql, postgresql, oracle\n")
    db_type_our = db_type_our.lower()
    if db_type_our == 'oracle':
        engine_our = database_setup.ask_oracle()

    if db_type_our == 'mysql':
        engine_our = database_setup.ask_mysql()

    if db_type_our == 'postgresql':
        engine_our = database_setup.ask_postgre()

    table_name = input('\nInput the client table:\n')
    query = 'select count(*) from {}'.format(table_name)
    df_client = pd.read_sql(query, engine_client)
    our_table = input('\nInput the table name in your db\n')
    df_our = pd.read_sql(query, engine_our)
    if df_client.values[0][0] != df_our.values[0][0]:
        diff = df_client.values[0][0] - df_our.values[0][0]
        print('\nDifference of {} rows found'.format(diff))
        order_column=input('\nPlease enter a column to order the data on\n')
        if db_type == 'oracle':
            query=oracle_syntax(diff,table_name,order_column)

        if db_type == 'mysql':
            query=mysql_syntax(diff,table_name,order_column)

        if db_type == 'postgresql':
            query=postgre_syntax(diff,table_name,order_column)

        df=pd.read_sql(query,engine_client)

        df.to_sql(our_table,engine_our,if_exists='append')

    else:
        print('\nTable already Updated.')
