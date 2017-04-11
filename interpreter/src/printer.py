from keywords import *
import re
from error import *
from expression import *
from csv import reader

class PrintStatement(object):

	def __init__(self,statement):
		self.statement = statement
		self.parsed = None

		self.parse()

	def parse(self):
		
		# self.parsed=[]
		# for line in reader(self.statement):
		# 	self.parsed.append(line[0])

		self.parsed = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)",self.statement)


	def eval(self,state):
		for x in self.parsed:
			if x[0]=="\"":
				print(x[1:-1],end=" ")
			else:
				try:
					print(state[x],end=" ")
				except NameError:
					print(x, " is not defined.")
		print("")
