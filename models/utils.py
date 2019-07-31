
import pymysql


def executeSQL(dbCon:dict,sql):

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

def createCond(cond:dict):
	
	'''
	returns the cond part of the where
	'''

	return " and ".join(["{} = '{}' ".format(i,j) for i,j in cond.items()])


def query(dbCon,table,cond:dict) -> list:

	cond = createCond(cond)
	sql = f"select * from {table} where " + cond

	return  executeSQL(dbCon,sql)
