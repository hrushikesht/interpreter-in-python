import re

from error import AssignmentError
from error import EvaluationError

infi = 9999999999999

class Var(object):

    def __init__(self,data):
        self.variable = data

    def eval(self,state):
        try:
            return state[self.variable]
        except EvaluationError:
            print(self.variable)
            print("Unknown Error")

class Constant(object):

    def __init__(self,data):
        self.data = int(data)

    def eval(self,state):
        try:
            return self.data
        except EvaluationError:
            print(self.data,"Unknown Error")

class Factor(object):

    def __init__(self,expression):
        self.expression = expression
        self.data_type = None

        self.parse()

    def parse(self):
        try:
            if(self.expression[0].isdigit()):
                self.data_type = Constant(self.expression)
            else:
                self.data_type = Var(self.expression)
        except AssignmentError.Syntax:
            print(self.expression)

    def eval(self,state):
        try:
            return self.data_type.eval(state)
        except EvaluationError:
            print(self.expression,"Unknown Error")

class GenericExpression(object):

    def __init__(self,expression):

        self.expression = expression
        self.left = None
        self.right = None

        self.parse()


class PlusExpression(GenericExpression):

    def parse(self):
        idx = self.expression.find("+")

        self.right = Expression(self.expression[0:idx])
        self.left = Expression(self.expression[idx+1:])

    def eval(self,state):
        try:
            return self.left.eval(state) + self.right.eval(state)
        except EvaluationError:
            print(self.expression,"Unknown Error")

class MinusExpression(GenericExpression):

    def parse(self):
        idx = self.expression.find("-")

        self.left = Expression(self.expression[0:idx])
        self.right = Expression(self.expression[idx+1:])
    
    def eval(self,state):
        try:
            return self.left.eval(state) - self.right.eval(state)
        except EvaluationError:
            print(self.expression,"Unknown Error")

class MulExpression(GenericExpression):

    def parse(self):
        idx = self.expression.find("*")

        self.left = Expression(self.expression[0:idx])
        self.right = Expression(self.expression[idx+1:])
    
    def eval(self,state):
        try:
            return self.left.eval(state) * self.right.eval(state)
        except EvaluationError:
            print(self.expression,"Unknown Error")

class DivExpression(GenericExpression):

    def parse(self):
        idx = self.expression.find("/")

        self.left = Expression(self.expression[0:idx])
        self.right = Expression(self.expression[idx+1:])
    
    def eval(self,state):
        try:
            return self.left.eval(state) / self.right.eval(state)
        except EvaluationError:
            print(self.expression,"Unknown Error")

class Expression(object):

    def __init__(self,expression):
        self.expression = expression
        self.expr_type = None

        self.parse()
    
    def parse(self):

        add_index = self.expression.find("+")
        sub_index = self.expression.find("-")

        if(add_index==-1): add_index=infi
        if(sub_index==-1): sub_index=infi

        if(add_index<sub_index):
            self.expr_type = PlusExpression(self.expression)
        elif sub_index<add_index:
            self.expr_type = MinusExpression(self.expression)
        else:
            div_index = self.expression.find("/")
            mul_index = self.expression.find("*")

            if(mul_index==-1): mul_index=infi
            if(div_index==-1): div_index=infi

            if(mul_index<div_index):
                self.expr_type=MulExpression(self.expression)
            elif(div_index<mul_index):
                self.expr_type=DivExpression(self.expression)
            else:
                self.expr_type= Factor(self.expression)

    def eval(self,state):
        print(self.expr_type)
        try:
            return self.expr_type.eval(state)
        except EvaluationError:
            print(self.expression,"Unknown Error")


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
                    raise AssignmentError.Syntax(self.statement)

                self.rhs = Expression(self.rhs)
                return True
            except AssignmentError:
                print(self.statement)
        else:
            raise AssignmentError(self.statement,"Bruh")

    def eval(self,state):
        try:
            state[self.lhs] =  self.rhs.eval(state)
        except EvaluationError:
            print(self.statement,"Unknown Error")

class CompoundStatement():

    def __init__(self,text):
        self.text = text
        self.statements = []

        self.parse()

    def parse(self):

        while(self.text!=""):
            
            if_index = self.text.find('if') 
            while_index = self.text.find('while')

            if(if_index==-1): if_index=infi
            if(while_index==-1): while_index=infi

            if(if_index==infi and while_index==infi):
                pos = self.text.find(";")

                if(pos==-1):
                    raise AssignmentError(self.text,"Unknown Error")

                statement = self.text[0:pos]
                self.text = self.text[pos+1:]

                try:
                    ass_obj = AssignmentStatement(statement)
                    self.statements.append(ass_obj)
                except AssignmentError:
                    print(statement)

    
    def eval(self,state):
        try:
            for x in self.statements:
                x.eval(state)
        except EvaluationError:
            print("don","Unknown Error")


class Parser():

    def __init__(self,text):
        self.text = text
        self.start = None

    def parse(self):

        #strip away tabs, whitespaces and newline
        self.text = re.sub('[\s]','',self.text)
        self.text = self.text.rstrip()
        self.start = CompoundStatement(self.text)
        return self.start

class Program(object):

    def __init__(self,text):
        self.parser = Parser(text)
        self.state = {}
        self.parsed_prog = None

    def parse(self):
        self.parsed_prog = self.parser.parse()

    def execute(self):
        self.parsed_prog.eval(self.state)

    def checkState(self):

        print("Printing Current State of Program......")
        for x in self.state:
            print(x,"==>",self.state[x])


if __name__ == '__main__':
        
    curr_file = open("example1.txt",'r')
    text = curr_file.read()
    P = Program(text)
    P.parse()
    P.execute()
    P.checkState()
