import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import psycopg2

spreadsheet_key = "1wDVqSpFr0ANWCrP7poWzKl2VQSML5DT_OETWbd--k0Q"
scope = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("client_secret_abc.json", scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key("1wDVqSpFr0ANWCrP7poWzKl2VQSML5DT_OETWbd--k0Q").sheet1
data = wks.get_all_records()
cols = wks.get_all_values()[0]  # keeps cols in right order
df = pd.DataFrame(data, columns=cols)

wks = gc.open_by_key("1_hUqUIS2GSckcOz-tX4m0jz95is4ktv5pKzjsBCueaQ").worksheet('sheet1')

import sqlalchemy

#connstring = “dbtype: // username: password @ hostname:port / dbname”
#engine = sqlalchemy.create_engine(connstring)

#connstring = “postgresql+psycopg2://postgres: abcd12345 @ localhost:5432/anujarora”
#engine = sqlalchemy.create_engine(connstring)

import psycopg2
connstring = "host='localhost' dbname='anujarora' user='postgres' password='abcd12345'"

engine = sqlalchemy.create_engine(connstring)

df.to_sql('users', engine)
