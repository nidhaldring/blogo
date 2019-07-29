
import pymysql


def executeSQL(sql,dbCon:dict):

	'''
	executes the given sql
	returning the result or none if none
	'''

	conn = pymysql.connect(**dbCon)
	cursor = conn.cursor()

	cursor.execute(sql)
	res = cursor.fetchall()

	conn.commit()
	conn.close()

	return res


def query(dbCon,table,cond:dict) -> list:

	cond = " and ".join(["{} = '{}' ".format(i,j) for i,j in cond.items()])
	sql = f"select * from {table} where " + cond
	res = executeSQL(sql,dbCon)

	return res