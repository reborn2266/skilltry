#!/usr/bin/env python3

class AClass(object):
	def __init__(self):
		self.d = 1

	def method(self, arg):
		print arg

aObj = AClass()

# normal usage
print aObj.d
aObj.method("hello")

# whole story of instance variable
print aObj.__dict__['d']
# why we need self as first parameter in method
type(aObj).method(aObj, "hello")

# how does the python find method
type(aObj).__dict__['method'](aObj, "hello")

# whole story of how the method be implemented by descriptor mechanism, almost whole story...
type(aObj).__dict__['method'].__get__(aObj, type(aObj))("hello")
