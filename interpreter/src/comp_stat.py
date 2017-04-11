import re

from error import *
import assign as ass
import branch as br
import loop
import printer

class CompoundStatement(object):

    def __init__(self,text):
        self.text = text
        self.statements = []

        self.parse()

    def parseIf(self):

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
            except BranchError:
                print("Error in Parsing : ",self.text)


            if len(self.text)>=index+3 and self.text[index+2]==';':
                self.text = self.text[index+3:]
            else:
                raise BranchError(self.text,"Semi colon missing after 'fi'")

    def parseAssign(self):
        #Parsing Assignment Statement Block
        pos = self.text.find(";")

        if pos==-1:
            raise ass.AssignmentError(self.text,"Semi Colon Missing at the end of the line")

        statement = self.text[0:pos]
        self.text = self.text[pos+1:]

        try:
            ass_obj = ass.AssignmentStatement(statement)
            self.statements.append(ass_obj)
        except AssignmentError:
            print(self.text,"Error in Syntax of Assignment Statement")

    def parseWhile(self):

        count = 0
        index = None
        for i in range(len(self.text)-4):
            if i<=len(self.text)-5 and self.text[i:i+5]=="while":
                count+=1
            elif self.text[i:i+4]=="done":
                count-=1
            if count==0:
                index=i
                break

        if index==None:
            raise LoopError(self.text,"Unbalanced 'while' and 'done'")
        else:
            try:
                loop_statement = loop.WhileStatement(self.text[0:index+4])
                self.statements.append(loop_statement)
            except LoopError:
                print("Error in Parsing Loop Statement: ",self.text)

            if len(self.text)>=index+5 and self.text[index+4]==';':
                self.text = self.text[index+5:]
            else:
                raise LoopError(self.text,"Semi colon missing after 'done'")

    def parseComment(self):

        end_pos = self.text.find("-->")

        if end_pos==-1:
            raise CommentError(self.text,"Unfinished Comment.")
        else:
            self.text = self.text[end_pos+3:]

    def parsePrint(self):

        close_pos = self.text.find(')')

        if close_pos==-1:
            raise PrintError(self.text,"No Opening bracket at the end of statement.")
        else:
            try:
                print_statement = printer.PrintStatement(self.text[6:close_pos])
            except PrintError:
                print("Error in parsing pring statement : ",self.text)

            self.statements.append(print_statement)

            if len(self.text)>=close_pos+2 and self.text[close_pos+1]==';':
                self.text = self.text[close_pos+2:]
            else:
                raise PrintError(self.text,"Semi colon missing after the end of the statement")


    def parse(self):

        while(self.text!=""):
            if self.text[0:2]=="if":
                self.parseIf()
            elif self.text[0:5]=="while":
                self.parseWhile()
            elif self.text[0:4]=="<!--":
                self.parseComment()
            elif self.text[0:5]=="print":
                self.parsePrint()
            else:
                self.parseAssign()

    
    def eval(self,state):
        try:
            for x in self.statements:
                x.eval(state)
        except EvaluationError:
            print(self.text,"Unknown Error")