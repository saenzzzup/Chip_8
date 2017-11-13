class Opcode(object):
	values = [0x0000, 0x00E0, 0x00EE, 0x1000, 0x2000, 
			0x3000, 0x4000, 0x5000, 0x6000, 0x7000,
			0x8000, 0x8001, 0x8002, 0x8003, 0x8004,
			0x8005, 0x8006, 0x8007, 0x800E, 0x9000,
			0xA000, 0xB000, 0xC000, 0xD000, 0xE00E,
			0xE001, 0xF007, 0xF00A, 0xF015, 0xF008,
			0xF00E, 0xF009, 0xF003, 0xF055, 0xf065]

	@staticmethod
	def exists(value):
		if (value in Opcode.values):
			return True
		elif ((value & 0xF000) in Opcode.values):
			return True
		elif ((value & 0xF00F) in Opcode.values):
			return True
		elif ((value & 0xF0FF) in Opcode.values):
			return True
		else:
			return False

	@staticmethod
	def execute(opcode, registers, memory, stack):
		if((opcode & 0xF000) == 0x0000):
			print("a")
			
		elif(opcode == 0x00E0):
			print("a")

		elif(opcode == 0x00EE):
			registers['pc'] = stack.pop()
			print("00EE")

		elif((opcode & 0xF000) == 0x1000):
			registers['pc'] = opcode & 0x0FFF
			print("1NNN")

		elif((opcode & 0xF000) == 0x2000):
			stack.push(registers['pc'])
			registers['pc'] = opcode & 0x0FFF
			print("2NNN")


		elif((opcode & 0xF000) == 0x3000):
			if registers['V'][(opcode & 0x0F00) >> 8] == (opcode & 0x00FF):
				registers['pc'] += 2
			print("3XNN")

		elif((opcode & 0xF000) == 0x4000):
			if registers['V'][(opcode & 0x0F00) >> 8] != (opcode & 0x00FF):
				registers['pc'] += 2
			print("4XNN")

		elif((opcode & 0xF000) == 0x5000):
			if (registers['V'][(opcode & 0x0F00) >> 8] == registers['V'][(opcode & 0x00F0) >> 12]):
				registers['pc'] += 2
			print("5XY0")

		elif((opcode & 0xF000) == 0x6000):
			registers['V'][(opcode & 0x0F00)>>12] = (opcode & 0x00FF)
			print("6XNN")

		elif((opcode & 0xF000) == 0x7000):
			registers['V'][(opcode & 0x0F00)>>12] += (opcode & 0x00FF)
			print("7XNN")

		elif((opcode & 0xF00F) == 0x8000):
			registers['V'][(opcode & 0x0F00)>>8] = registers['V'][(opcode & 0x00F0)>>4]
			print("8XY0")

		elif((opcode & 0xF00F) == 0x8001):
			aux = registers['V'][(opcode & 0x0F00)>>12] | registers['V'][(opcode & 0x00F0)>>12]
			registers['V'][(opcode & 0x0F00)>>12] = aux
			print("8XY1")

		elif((opcode & 0xF00F) == 0x8002):
			aux = registers['V'][(opcode & 0x0F00)>>12] & registers['V'][(opcode & 0x00F0)>>12]
			registers['V'][(opcode & 0x0F00)>>12] = aux
			print("8XY2")

		elif((opcode & 0xF00F) == 0x8003):
			a = registers['V'][(opcode & 0x0F00)>>12]
			b = registers['V'][(opcode & 0x00F0)>>12]
			registers['V'][(opcode & 0x0F00)>>12] = (a and not b) or (not a and b)
			print("8XY3")

		#Añadir carry
		elif((opcode & 0xF00F) == 0x8004):
			if registers['V'][(opcode & 0x0F00)>>12] + registers['V'][(opcode & 0x00F0)>>12] > 0xFF:
				registers['V'][0xF] = 1
			else:
				registers['V'][0xF] = 0
			registers['V'][(opcode & 0x0F00)>>12] += registers['V'][(opcode & 0x00F0)>>12]
			registers['V'][(opcode & 0x0F00)>>12] &= 0xFF
			print("8XY4")

		elif((opcode & 0xF00F) == 0x8005):
			if registers['V'][(opcode & 0x0F00)>>12] < registers['V'][(opcode & 0x00F0)>>12]:
				registers['V'][0xF] = 0
			else:
				registers['V'][0xF] = 1
			registers['V'][(opcode & 0x0F00)>>12] -= registers['V'][(opcode & 0x00F0)>>12]
			registers['V'][(opcode & 0x0F00)>>12] &= 0xFF
			print("8XY5")

		elif((opcode & 0xF00F) == 0x8006):
			registers['V'][0xF] = registers['V'][(opcode & 0x00F0)>>12] & 1
			registers['V'][(opcode & 0x0F00)>>12] = registers['V'][(opcode & 0x00F0)>>12] >> 1
			print("8XY6")

		elif((opcode & 0xF00F) == 0x8007):
			if registers['V'][(opcode & 0x0F00)>>12] > registers['V'][(opcode & 0x00F0)>>12]:
				registers['V'][0xF] = 0
			else:
				registers['V'][0xF] = 1
			registers['V'][(opcode & 0x0F00)>>12] = registers['V'][(opcode & 0x00F0)>>12] - registers['V'][(opcode & 0x0F00)>>12]
			registers['V'][(opcode & 0x0F00)>>12] &= 0xFF
			print("8XY7")

		elif((opcode & 0xF00F) == 0x800E):
			print("8XYE")

		elif((opcode & 0xF000) == 0x9000):
			if (registers['V'][(opcode & 0x0F00)>>12] != registers['V'][(opcode&0x00F0)>>12]):
				registers['pc'] += 2
			print("9XY0")
	
		elif((opcode & 0xF000) == 0xA000):
			registers['I'] = opcode & 0x0FFF
			print('ANNN')

		elif((opcode & 0xF000) == 0xB000):
			registers['pc'] = registers['V'][0] + (opcode & 0x0FFF)
			print("BNNN")

		elif((opcode & 0xF000) == 0xC000):
			r = random.randint(0, 0x00FF)
			registers['V'][(opcode & 0x0f00)>>12] = r & ((opcode & 0x00FF)>>8)
			print("CXNN")

		elif((opcode & 0xF000) == 0xD000):
			print("a")

		elif((opcode & 0xF00F) == 0xE00E):
			print("a")

		elif((opcode & 0xF00F) == 0xE001):
			print("EXA1")

		elif((opcode & 0xF00F) == 0xF007):
			registers['V'][(opcode & 0x0F00)>>12] = timers['delay'] 
			print("FX07")

		elif((opcode & 0xF00F) == 0xF00A):
			print("FX0A")

		elif((opcode & 0xF0FF) == 0xF015):
			timers['delay'] = registers['V'][(opcode & 0x0F00)>>12]
			print("FX15")

		elif((opcode & 0xF00F) == 0xF008):
			timers['sound'] = registers['V'][(opcode & 0x0F00)>>12]
			print("FX18")

		elif((opcode & 0xF00F) == 0xF00E):
			print("FX1E")

		elif((opcode & 0xF00F) == 0xF009):
			registers['I'] = (5*(registers['V'][(opcode & 0x0F00)>>12])) & 0xFFF
			print("FX29")

		elif((opcode & 0xF00F) == 0xF003):
			registers['I'] = registers['V'][(opcode & 0x0F00)>>12] / 100
			registers['I' + 1] = (registers['V'][(opcode & 0x0F00)>>12] / 10) % 10
			registers['I' + 2] = (registers['V'][(opcode & 0x0F00)>>12] % 100) % 10
			print("FX33")

		elif((opcode & 0xF0FF) == 0xF055):
			i = 0
			while i <= registers['V'][(opcode & 0x0F00)>>12]:
				memory[registers['I' + i]] = registers['V'][i]
				i += 1
			registers['I'] += (registers['V'][(opcode & 0x0F00)>>12] + 1)
			print("FX55")

		elif((opcode & 0xF0FF) == 0xF065):
			i = 0
			while i <= registers['V'][(opcode & 0x0F00)>>12]:
				registers['V'][i] = memory[registers['I' + i]]
				i += 1
			registers['I'] += (registers['V'][(opcode & 0x0F00)>>12] + 1)
			print("FX65")

		else:
			print("Error")
		return registers, memory, stack


