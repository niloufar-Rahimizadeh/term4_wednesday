import pymysql

con = pymysql.connect(host='localhost', user='poulstar', password='poulstar', database='my_db_n')

sql = """CREATE TABLE `users1` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255)  NOT NULL,
    `family` varchar(255) NOT NULL,
    `fage` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) """

try:
    with con.cursor() as cur:
        cur.execute(sql)
except:
    print("Access Denied")
finally:
    con.close()