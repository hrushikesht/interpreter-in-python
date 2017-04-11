from keywords import *
from error import *
from expression import *
from condition import *
import comp_stat as cs


class WhileStatement(object):

	def __init__(self,body):
		self.block = body
		self.condition = None
		self.exec = None

		self.parse()

	def parse(self):

		do_pos = self.block.find(DO)

		if do_pos==-1:
			raise LoopError(self.block,"Missing 'do' in 'while' block")
		else:

			try:
				self.condition = ConditionalStatement(self.block[5:do_pos])
			except LoopError:
				print("Error in conditonal Statement in 'while' loop : ",self.block)

			try:	
				self.exec = cs.CompoundStatement(self.block[do_pos+2:-4])
			except LoopError:
				print("Error in body of the 'while' loop : ",self.exec)

	def eval(self,state):

		while self.condition.eval(state):
			self.exec.eval(state)