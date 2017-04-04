import re
import os

from comp_stat import *

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

        # print("Printing Current State of Program......")
        for x in self.state:
            print(x,"==>",self.state[x])


if __name__ == '__main__':
    
    prog_dir = "../examples"
    for filename in os.listdir(prog_dir):    
        curr_file = open(prog_dir+"/"+filename,'r')
        text = curr_file.read()
        P = Program(text)
        P.parse()
        P.execute()
        print("State for ",filename[:-4]," : ")
        P.checkState()
        print("")