#!/usr/bin/python3

from child import *

if __name__ == "__main__":

    child = Child()

    child.childFunction()
    child.parentPublicFunction()
    child._parentProtectedFunction()
    child.__parentPrivateFunction()
