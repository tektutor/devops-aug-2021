from parent import *

class Child(Parent):

    def __init__(self):
        Parent.__init__(self)
        print ("Child Constructor ...")
        
    def childFunction(self):
        print ("Child Function")
