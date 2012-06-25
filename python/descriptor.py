#!/usr/bin/env python3

class foo:
	def __init__(self, x, y):
		self.__x = x
		self.__y = y
	@property
	def x(self):
		return self.__x

if __name__ == "__main__":
	afoo = foo(1, 3)
	print(afoo.x)
