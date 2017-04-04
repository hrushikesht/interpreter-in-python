import os
import unittest
from main import *

prog_dir = "/examples"
sol_dir = "/solutions"

class TestProgram(unitest.TestCase):

    def programTestCase(self):

        for filename in os.listdir(rootdir):
            