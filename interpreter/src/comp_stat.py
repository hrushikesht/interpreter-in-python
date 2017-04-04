import re

from error import *
import assign as ass
import branch as br

class CompoundStatement(object):

    def __init__(self,text):
        self.text = text
        self.statements = []

        self.parse()

    def parse(self):

        while(self.text!=""):

            #parse if block
            if self.text[0:2]=="if":
                count = 0
                index = 0
                for i in range(len(self.text)-1):
                    if self.text[i:i+2]=="if":
                        count+=1
                    elif self.text[i:i+2]=="fi":
                        count-=1

                    if count==0:
                        index=i
                        break

                if index==None:
                    raise BranchError(self.text,"Amount of if and fi are not balanced")
                else:
                    try:
                        branch_statement = br.BranchStatement(self.text[0:index+2])
                        self.statements.append(branch_statement)
                        self.text = self.text[index+2:]
                    except BranchError:
                        print(self.statements,"Unknown Error")
            else:
                #Parsing Assignment Statement Block
                pos = self.text.find(";")

                if(pos==-1):
                    raise ass.AssignmentError(self.text,"Unknown Error")

                statement = self.text[0:pos]
                self.text = self.text[pos+1:]

                try:
                    ass_obj = ass.AssignmentStatement(statement)
                    self.statements.append(ass_obj)
                except AssignmentError:
                    print(self.statement,"Error in Syntax of Assignment Statement")

    
    def eval(self,state):
        try:
            for x in self.statements:
                x.eval(state)
        except EvaluationError:
            print(self.text,"Unknown Error")