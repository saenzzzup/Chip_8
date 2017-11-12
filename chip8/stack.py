class Stack(object):
	def __init__(self):
		space = [0]*16
		sp = 0

	def checkFull(index):
		if index > 15:
			return true

		else:
			return false

	def checkEmpty(self):
		if sp == 0:
			return true
		else:
			return false

	def push(self, value):
		if (not checkFull()):
			space[sp] = value
			sp += 1

	def pop(self):
		if (not checkEmpty()):
			sp -= 1
			return space[sp]