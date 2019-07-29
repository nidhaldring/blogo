
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
