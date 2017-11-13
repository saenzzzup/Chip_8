#from opcode import Opcode
from stack import Stack
from random import randint
from screen import Chip8Screen

# http://devernay.free.fr/hacks/chip8/C8TECH10.HTM

class Chip8CPU(object):

	def __init__(self, screen):

		self.opcode = 0
		self.memory = [0]*4096
		self.stk = Stack()

		self.screen = screen

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

		self.operation_Search = {
			0: self.rest_clean,
			1: self.jump_addres,
			2: self.subrutine,
			3: self.next_if_equal_reg_val,
			4: self.next_if_not_equal_reg_val,
			5: self.next_if_equal_reg_reg,
			6: self.load_val_reg,
			7: self.adds_reg_val,
			8: self.execute_locigal_operation,
			9: self.next_if_not_equal_reg_reg,
			10: self.load_val_index,
			11: self.jump_index_plus_val,
			12: self.random_val,
			13: self.draw,
			#14: self.none,
			#15: self.none,
		}

		self.logical_operation = {
			0: self.load_reg_reg,
			1: self.or_bite,
			2: self.and_bite,
			3: self.xOr_bite,
			4: self.add,
			5: self.substract,
			6: self.right_shift,
			7: self.substract1,
			14: self.left_shift,
		}

	def rom_load(self, filename, offset=0):
		romdata = open(filename, 'rb').read()
		for index, val in enumerate(romdata):
			self.memory[offset + index] = ord(val)
		# Cambiar valor a hexadecimal: format(ord(val), '02x')

	def execute_instruction(self, opcode=None):

		if opcode:
			self.opcode = opcode
		else:
			self.opcode = int(self.memory[self.registers['pc']])
			self.opcode = self.opcode << 8
			self.opcode += int(self.memory[self.registers['pc'] + 1])
			self.registers['pc'] += 2
		operation = (self.opcode & 0xF000) >> 12
		self.operation_Search[operation]()

		return self.opcode


	def execute_locigal_operation(self):
		operation = (self.opcode & 0x000F)

		try:
			self.logical_operation[operation]()
		except KeyError:
			raise Exception("Unknown op-code:" + str(self.opcode))

	# Execute Locigal Operation, if op similar to 0x8---

	def load_reg_reg(self): 
		pass

	def or_bite(self): 
		pass

	def and_bite(self): 
		pass
		
	def xOr_bite(self): 
		pass
		
	def add(self): 
		pass
		
	def substract(self): 
		pass
		
	def right_shift(self): 
		pass
		
	def substract1(self): 
		pass
		
	def left_shift(self): 
		pass

	# Normal Operations

	def rest_clean(self): 
		pass

	def jump_addres(self): 
		self.registers['pc'] = self.opcode & 0x0FFF
		
	def subrutine(self): 
		self.stk.push(self.registers['pc'] & 0x00FF)
		self.registers['sp'] += 1
		self.stk.push((self.registers['pc'] & 0xFF00) >> 8)
		self.registers['sp'] += 1
		self.registers['pc'] = self.opcode & 0x0FFF

	def next_if_equal_reg_val(self): 
		if self.registers['V'][(self.opcode & 0x0F00) >> 8] == (self.opcode & 0x00FF):
			self.registers['pc'] += 2
		
	def next_if_not_equal_reg_val(self): 
		if self.registers['V'][(self.opcode & 0x0F00) >> 8] != (self.opcode & 0x00FF):
			self.registers['pc'] += 2
		
	def next_if_equal_reg_reg(self): 
		if (self.registers['V'][(self.opcode & 0x0F00) >> 8] == self.registers['V'][(self.opcode & 0x00F0) >> 4]):
			self.registers['pc'] += 2
		
	def load_val_reg(self): 
		self.registers['V'][(self.opcode & 0x0F00)>>8] = (self.opcode & 0x00FF)
		
	def adds_reg_val(self): 
		direction = (self.opcode & 0x0F00) >>8
		temp = self.registers['V'][direction] + (self.opcode & 0x00FF)

		self.registers['V'][direction] = temp if temp < 256 else temp - 256
		
	def next_if_not_equal_reg_reg(self): 
		if (self.registers['V'][(self.opcode & 0x0F00)>>8] != self.registers['V'][(self.opcode & 0x00F0) >> 4]):
			self.registers['pc'] += 2
		
	def load_val_index(self): 
		self.registers['I'] = self.opcode & 0x0FFF
		
	def jump_index_plus_val(self): 
		registers['pc'] = registers['V'][0] + (self.opcode & 0x0FFF)

	def random_val(self):

		self.registers['V'][(self.opcode & 0x0F00)>>8] = randint(0, 255) & (self.opcode & 0x00FF)
		
	def draw(self): 
		pass
			


cpu = Chip8CPU(Chip8Screen())
cpu.execute_instruction()


