
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



def insert(dbCon,table,data:dict):

	sql = f"insert into {table}"
	sql += "(" + " , ".join(data.keys()) +")"
	sql += " values(" + " , ".join([f"'{i}'" for i in data.values()]) + ")"

	executeSQL(dbCon,sql)

def delete(dbCon,table,cond:dict):

	cond = createCond(cond)
	sql = f"delete from {table} where " + cond

	executeSQL(dbCon,sql)


def update(dbCon,table,id_,newData:dict):

	sql = f"update {table} set "
	sql +=  " , ".join(["{} = '{}' ".format(i,j) for i,j in newData.items()])
	sql += f"where id = {id_}"

	executeSQL(dbCon,sql)



def query(dbCon,table,cond:dict) -> list:

	cond = createCond(cond)
	sql = f"select * from {table} where " + cond

	return  executeSQL(dbCon,sql)
