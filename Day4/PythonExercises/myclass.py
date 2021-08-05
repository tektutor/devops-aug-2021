#!/usr/bin/python3

class MyClass:

    def __init__(self):
        print ("Inside contructor ...")
        self.x = 10
        self.y = 20

    def setValues(self, value1, value2):
        self.x = value1
        self.y = value2

    def printValues(self):
        print ( "X = ", self.x )
        print ( "Y = ", self.y )


if __name__ == "__main__":
   myClassObj = MyClass()
   print ("Values immediately after the object is instantiated ...")
   myClassObj.printValues()
   myClassObj.setValues ( 100, 200 )
   print ("Values after setValues ")
   myClassObj.printValues()

