from stack import Stack
from opcode import Opcode

class cpu(object):

	gfx = [0]*2048
	opcode = 0
	memory = [0]*4096

	"""docstring for cpu"""
	def __init__(self):

		self.timers = {
			'delay': 0,
			'sound': 0,
		}

		self.registers = {
			'V': [0]*16,
			'sp': 0,
			'pc': 0,
			'I':0,
		}

		self.stack = Stack()


	def initialize(self):
	    return    
	    
	def emulateCycle(self):
	    fetch()
	    decodeExecute()
	    return
	    
	def fetch(self):
		#Prueba:
		'''self.memory[self.registers['pc']] = 0xA2
		self.memory[self.registers['pc']+1] = 0xF0'''

		byte1 = self.memory[self.registers['pc']]
		byte2 = self.memory [self.registers['pc']+1]
		self.opcode =  byte1 << 8 | byte2
		return
	    
	def decode(self):
		if (Opcode.exists(self.opcode)):
			print("si")

	def decodeExecute(self):
		registers, memory, stack= Opcode.execute(self.opcode, 
			self.registers, self.memory, self.stack)
		self.registers['pc'] += 2
		print(self.registers['pc'])



computador = cpu()
computador.memory[0] = 0xA2
computador.memory[1] = 0xF0
computador.fetch()
#print(computador.opcode)
computador.decodeExecute()
computador.memory[2] = 0xF0
computador.memory[3] = 0x65
computador.fetch()
computador.decodeExecute()
computador.memory[4] = 0xF0
computador.memory[5] = 0x55
computador.fetch()
computador.decodeExecute()

