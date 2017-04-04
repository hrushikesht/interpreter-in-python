from error import *
from expression import *
import comp_stat as cs


class GenericCondition(object):

    def __init__(self,left,right):
        self.right = Expression(left)
        self.left = Expression(right)

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

class ConditionalStatement(object):

    def __init__(self,expression):
        self.expression = expression
        self.expr_type = None

        self.parse()

    def parse(self):

        try:
            pos1 = self.expression.find(">=")
            pos2 = self.expression.find("<=")
            pos3 = self.expression.find("==")
            pos4 = self.expression.find(">")
            pos5 = self.expression.find("<")

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
            else:
                raise BranchError(self.expression,"Invalid Syntax in Conditional Statement")
        except BranchError:
            print(self.expression,"Error in Parsing Conditional Statement")

    def eval(self,state):
        try:
            self.expr_type.eval(state)
        except BranchError:
            print(self.expression,"Error in Evaluation of conditional Statement")

class BranchStatement(object):

    def __init__(self,statement):
        self.statement = statement
        self.condition = None
        self.then = None
        self.else_body = None

        self.parse()

    def parse(self):

        then_index = self.statement.find("then")

        if then_index==-1:
            raise BranchError(self.statement,"'then' statement not found.")
        else:
            try:
                self.condition = ConditionalStatement(self.statement[2:then_index])

                if_count=0
                fi_count=0
                else_pos=None

                for i in range(2,len(self.statement)-4):
                    if self.statement[i:i+2]=="if":
                        if_count+=1
                    elif self.statement[i:i+2]=="fi":
                        fi_count+=1

                    if self.statement[i:i+4]=="else" and if_count==fi_count:
                        else_pos = i
                        break
                
                if else_pos!=None:
                    self.then = cs.CompoundStatement(self.statement[then_index+4:else_pos])
                    self.else_body = cs.CompoundStatement(self.statement[else_pos+4:-2])
                else:
                    self.then = cs.CompoundStatement(self.statement[then_index+2:-2])
            except BranchError:
                print(self.statement,"Unknown Erorr")

    def eval(self,state):
        try:
            if(self.condition.eval(state)):
                self.then.eval(state)
            elif self.else_body!=   None:
                self.else_body.eval(state)
        except BranchError:
            print(self.statement,"Error in Evaluation")