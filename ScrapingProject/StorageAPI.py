import sqlite3

#dbとのコネクションを作成
def Create_connection(dbname):
    # DBを作成する（既に作成されていたらこのDBに接続する）
    conn = sqlite3.connect(dbname)

    return conn

#Dataframe型データをdbにinsert
def Insert_df(conn, df):
    return None


#dbとのコネクションを終了する
def Close_connection(conn):
    conn.close()
    
