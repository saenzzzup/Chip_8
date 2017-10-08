class cpu(object):

	opcode = 0
	memory = [0]*4096
	V=[0]*16

	I = 0
	pc = 0

	gfx = [0]*2048

	delay_timer = 0
	sound_timer = 0

	stack = [0]*16
	sp = 0

	key = [0]*16

	"""docstring for cpu"""
	def __init__(self, arg):
		super(Chip8, self).__init__()
		self.arg = arg
		