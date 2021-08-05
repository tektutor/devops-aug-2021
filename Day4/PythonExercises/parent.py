#!/usr/bin/python3

class Parent:

    def __init__(self):
        print ("Parent constructor ...")

    def parentPublicFunction(self):
        print ("Parent public function")

    def _parentProtectedFunction(self):
        print ("Parent protected function")
    
    def __parentPrivateFunction(self):
        print ("Parent private function")

