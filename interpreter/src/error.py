class Error(Exception):
    """"Base Class For Exeptions"""
    pass

class AssignmentError(Error):
    """Exception raised during parsing and evaluating of Assignment Statement"""

    def __init__(self,expression,message):
        print("Error in parsing the Assignment Statement: ",expression)
        print(message)


class EvaluationError(Error):

    def __init__(self,expression,message):
        print("Error in Evaluating: ",expression)
        print(message)

class BranchError(Error):

    def __init__(self,expression,message):
        print("Error in Branching Statement : ",expression)
        print(message)

class LoopError(Error):

    def __init__(self,expression,message):
        print("Error in Loop Statement : ",expression)
        print(message)

class CommentError(Error):

    def __init__(self,expression,message):
        print("Error in Comment Statement : ",expression)
        print(message)

class PrintError(Error):

    def __init__(self,expression,message):
        print("Error in Print Statement: ",expression)
        print(message)


# for testing purpose
if __name__ == '__main__':
    expression = "a = x + y"
    