import pymysql


con = pymysql.connect(host='localhost', user='poulstar', password='poulstar', database='my_db_n')

sql = "INSERT INTO users1(name, family, age) VALUES(%s, %s, %s)"
data = ("niloufar", "rahimizade", "27")

try:
    with con.cursor() as cur:
        cur.execute(sql, data)
        con.commit()
except:
    print("Access Denied")
finally:
    con.close()