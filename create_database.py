import pymysql



con = pymysql.connect(host='localhost', user='poulstar', password='poulstar')


try:
    with con.cursor() as cur:
        cur.execute("CREATE DATABASE my_db_n")
except:
    print("Access Denied")

