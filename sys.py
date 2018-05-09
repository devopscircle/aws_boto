import psycopg2
def database_connection():
    con = psycopg2.connect(host ='localhost',user = 'postgres',password = 'admin',database = 'table',port ='5432')
    cur = con.cursor()
    sql = "SELECT *	FROM public.sample;"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print row
    cur.close()
    con.close()

if __name__ == '__main__':
    database_connection()