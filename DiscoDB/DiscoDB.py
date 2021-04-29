import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Database:
	def __init__(self, fn, db={}, password, salt):

		self.password = password.encode()
		self.salt = salt
		self.file = fn
		self.tables = db

	def getlast(self, table):
		if not self.tables[table]["row_id"]:
			return 0
		else:
			return len(self.tables[table]["row_id"])

	def get_row(self, table, index):
		retv = []
		for key in self.tables[table]:
			retv.append(self.tables[table][key][index])
		return retv

	def insert(self, table, values): #"" () insert("users", {"id": })
		self.tables[table]["row_id"].append(self.getlast(table))
		for key in values:
			if key in self.tables[table]:
				self.tables[table][key].append(values[key])

	def select(self, column, table, where_args=[]): #select * from users where pass="lol"
		ret = []
		if where_args:
			for idx, row_entry in enumerate(self.tables[table][where_args[0]]):
				if row_entry == where_args[1]:
					if len(where_args) > 2:
						if self.tables[table][where_args[2]][idx] == where_args[3]:
							if column == "*":
								ret.append(self.get_row(table, idx))
							else:
								ret.append(self.tables[table][column][idx])
					else:
						if column == "*":
							ret.append(self.get_row(table, idx))
						else:
							ret.append(self.tables[table][column][idx])
		else:
			if column == "*":
				for row_entry in self.tables[table]["row_id"]:
					pairing = []
					for key in self.tables[table]:
						pairing.append(self.tables[table][key][row_entry])
					ret.append(pairing)
			else:
				ret=self.tables[table][column]
		return ret

	def update(self, table, col_tuple, where_tuple):
		for idx, row in enumerate(self.tables[table][where_tuple[0]]):
			if row == where_tuple[1]:
				self.tables[table][col_tuple[0]][idx]=col_tuple[1]

	def addTable(self, tb_name, cols):
		table = {'row_id': []}
		for col in cols:
			table.update({col:[]})
		self.tables.update({tb_name:table})

	def commit(self):
		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=self.salt,
			iterations=100000,
			backend=default_backend()
		)
		key = base64.urlsafe_b64encode(kdf.derive(self.password))
		f = Fernet(key)

		with open(self.file, 'w') as file:
			file.write(f.encrypt(str(self.tables).encode()).decode())

	def __repr__(self):
		st=""
		for table in self.tables:
			st+="TABLE: "+table
			for key in self.tables[table]:
				st += key +": "+str(k[key])+"\n"
		return st

	def __getitem__(self, tb_name):
		return self.tables[tb_name]

class Disco:
	def __init__(self):
		self.database_list = {}

	def addDatabase(self, db_name, pw="12345678", sl=b'salt_'):
		self.database_list.update({db_name:Database(db_name+'.dd', password=pw, salt=sl)})

	def __getitem__(self, db_name):
		return self.database_list[db_name]

	def loadDatabase(self, fn, pw="12345678", sl=b'salt_'):
		with open(fn+'.dd', 'r') as f:
			data = f.read().encode()
		kdf = PBKDF2HMAC(
			algorithm=hashes.SHA256(),
			length=32,
			salt=sl,
			iterations=100000,
			backend=default_backend()
		)
		key = base64.urlsafe_b64encode(kdf.derive(pw.encode()))
		f = Fernet(key)
		self.database_list.update({fn:Database(fn+'.dd', db=eval(f.decrypt(data)))})
