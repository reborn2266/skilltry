#!/usr/bin/env python

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

# whole story of how the method be implemented by descriptor mechanism
type(aObj).__dict__['method'].__get__(aObj, type(aObj))("hello")

class Proxy(object):
	def __get__(self, instance, cls):
		def handle():
			# access caller's info without passing any parameter
			return str(cls.__name__) + " " + str(instance.name) + " happpy~"
		return handle;

class Host(object):
	proxy = Proxy()
	def __init__(self, name):
		self.name = name

host = Host("ERS")
print host.proxy()
print Host.__dict__['proxy'].__get__(host, Host)()
