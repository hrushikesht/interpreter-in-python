from error import *
from expression import *

class AssignmentStatement(object):

    def __init__(self,statement):
        self.statement = statement
        self.lhs = None
        self.rhs = None

        self.parse()

    def parse(self):
        if(self.statement.count('=')==1):
            try:
                idx = self.statement.index('=')
                self.lhs = self.statement[0:idx]
                self.rhs = self.statement[idx+1:]

                #check if lhs contains a variable or not
                if(self.lhs[0].isdigit()):
                    raise AssignmentError(self.statement)

                self.rhs = Expression(self.rhs)
                return True
            except AssignmentError:
                print(self.statement)
        else:
            print("hi")
            raise AssignmentError(self.statement,"Unknown Error")

    def eval(self,state):
        try:
            y = self.rhs.eval(state)
            state[self.lhs] =  y
        except EvaluationError:
            print(self.statement,"Unknown Error")