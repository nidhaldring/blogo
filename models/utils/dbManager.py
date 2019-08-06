

import pymysql

from config import Config

class DbManager:

	def __init__(self):
		
		self.connectionSettings = dict(
								db=Config.DB_NAME,
								user=Config.USERS_TABLE,
								password=Config.DB_PASSWORD,
								host=Config.DB_HOST
							)		

	def execute(self,sql):

		'''
		executes the given sql
		returning the result or none if none
		'''

		conn = pymysql.connect(**self.connectionSettings)
		cursor = conn.cursor()

		cursor.execute(sql)
		res = cursor.fetchall()

		conn.commit()
		conn.close()

		return res
