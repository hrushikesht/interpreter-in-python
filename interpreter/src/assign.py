from error import *
from expression import *
from keywords import *


class AssignmentStatement(object):

    def __init__(self,statement):
        self.statement = statement
        self.lhs = None
        self.rhs = None

        self.parse()

    def parse(self):
        cnt = self.statement.count('=')
        if(cnt==1):
            idx = self.statement.index('=')
            self.lhs = self.statement[0:idx]
            self.rhs = self.statement[idx+1:]

            if self.lhs=="":
                raise AssignmentError(self.statement,"LHS of Assignment Statement Absent")

            #check if lhs contains a variable or not
            if self.lhs[0].isdigit():
                raise AssignmentError(self.statement,"Variable must start with a alphabetic character")

            self.rhs = Expression(self.rhs)
            return True
        elif cnt==0:
            raise AssignmentError(self.statement,"'=' sign not found in Assignment Statement")
        else:
            raise AssignmentError(self.statement,"More than one '=' sign found in Assignment Statement")

    def eval(self,state):
        try:
            y = self.rhs.eval(state)
            state[self.lhs] =  y
        except EvaluationError:
            print(self.statement,"Unknown Error")