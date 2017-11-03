class cpu(object):

	gfx = [0]*2048
	opcode = 0
	memory = [0]*4096

	"""docstring for cpu"""
	def __init__(self, arg):

		self.timers = {
			'delay': 0,
			'sound': 0,
		}

		self.registers = {
			'v': [],
			'index': 0,
			'sp': 0,
			'pc': 0,
			'rpl': []
		}

		self.stack = [0]*16
		self.key = [0]*16
		