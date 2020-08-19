import pandas as pd

import database_setup

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

    table_name = input('\nInput the table name to fetch:\n')
    query = 'select * from {}'.format(table_name)
    df_client = pd.read_sql(query, engine_client)
    our_table = input('\nInput the table name you want in your db\n')
    df_client.to_sql(our_table, engine_our,if_exists='replace')
    print('\nTable Updated.')
