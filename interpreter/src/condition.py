from keywords import *
from error import *
from expression import *

class GenericCondition(object):

    def __init__(self,left,right):
        self.right = Expression(right)
        self.left = Expression(left)

class GTETCondition(GenericCondition):

    def eval(self,state):
        return self.left.eval(state)>=self.right.eval(state)

class LTETCondition(GenericCondition):

    def eval(self,state):
        return self.left.eval(state)<=self.right.eval(state)

class ETCondition(GenericCondition):

    def eval(self,state):
        return self.left.eval(state)==self.right.eval(state)

class GTCondition(GenericCondition):

    def eval(self,state):
        return self.left.eval(state)>self.right.eval(state)

class LTCondition(GenericCondition):

    def eval(self,state):
        return self.left.eval(state)<self.right.eval(state)

class NECondition(GenericCondition):

    def eval(self,state):
        return self.left.eval(state)!=self.right.eval(state)

class ConditionalStatement(object):

    def __init__(self,expression):
        self.expression = expression
        self.expr_type = None

        self.parse()

    def parse(self):

        try:
            #Done for ease in implementation
            #Can be optimized for better performance
            #By checking and finding sequentially.
            pos1 = self.expression.find(">=")
            pos2 = self.expression.find("<=")
            pos3 = self.expression.find("==")
            pos4 = self.expression.find(">")
            pos5 = self.expression.find("<")
            pos6 = self.expression.find("!=")

            if pos1!=-1:
                self.expr_type = GTETCondition(self.expression[:pos1],self.expression[pos1+2:])
            elif pos2!=-1:
                self.expr_type = LTETCondition(self.expression[:pos2],self.expression[pos2+2:])
            elif pos3!=-1:
                self.expr_type = ETCondition(self.expression[:pos3],self.expression[pos3+2:])
            elif pos4!=-1:
                self.expr_type = GTCondition(self.expression[:pos4],self.expression[pos4+1:])
            elif pos5!=-1:
                self.expr_type = LTCondition(self.expression[:pos5],self.expression[pos5+1:])
            elif pos6!=-1:
                self.expr_type = NECondition(self.expression[:pos6],self.expression[pos6+2:])
            else:
                raise BranchError(self.expression,"Invalid Syntax in Conditional Statement")
        except BranchError:
            print(self.expression,"Error in Parsing Conditional Statement")

    def eval(self,state):
        try:
            return self.expr_type.eval(state)
        except BranchError:
            print(self.expression,"Error in Evaluation of conditional Statement")
