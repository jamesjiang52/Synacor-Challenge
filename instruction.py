from break_ import Break_

class Instruction:
    player_actions = iter([action.rstrip('\n') for action in open('C:\\Users\\James Jiang\\Documents\\Synacor Challenge\\auto_player.txt')])

    def __init__(self, memory, registers):
        self.memory = memory
        self.registers = registers
        self.stack = []
        self.memory_address = 0
        self.input_string = ''
        self.input_start = 0
        self.input_index = 0

    def register_value(self, n):
        if n in range(32768):
            return(n)
        else:
            return(self.registers[n])

    def halt_(self):
        raise Break_

    def set_(self):
        self.registers[self.memory[self.memory_address + 1]] = self.register_value(self.memory[self.memory_address + 2])
        self.memory_address += 3

    def push_(self):
        self.stack.append(self.register_value(self.memory[self.memory_address + 1]))
        self.memory_address += 2

    def pop_(self):
        self.registers[self.memory[self.memory_address + 1]] = self.stack.pop()
        self.memory_address += 2

    def eq_(self):
        if self.register_value(self.memory[self.memory_address + 2]) == self.register_value(self.memory[self.memory_address + 3]):
            self.registers[self.memory[self.memory_address + 1]] = 1
        else:
            self.registers[self.memory[self.memory_address + 1]] = 0
        self.memory_address += 4

    def gt_(self):
        if self.register_value(self.memory[self.memory_address + 2]) > self.register_value(self.memory[self.memory_address + 3]):
            self.registers[self.memory[self.memory_address + 1]] = 1
        else:
            self.registers[self.memory[self.memory_address + 1]] = 0
        self.memory_address += 4

    def jmp_(self):
        self.memory_address = self.register_value(self.memory[self.memory_address + 1])

    def jt_(self):
        if self.register_value(self.memory[self.memory_address + 1]) != 0:
            self.memory_address = self.register_value(self.memory[self.memory_address + 2])
        else:
            self.memory_address += 3

    def jf_(self):
        if self.register_value(self.memory[self.memory_address + 1]) == 0:
            self.memory_address = self.register_value(self.memory[self.memory_address + 2])
        else:
            self.memory_address += 3

    def add_(self):
        self.registers[self.memory[self.memory_address + 1]] = (self.register_value(self.memory[self.memory_address + 2]) + self.register_value(self.memory[self.memory_address + 3])) % 32768
        self.memory_address += 4

    def mult_(self):
        self.registers[self.memory[self.memory_address + 1]] = (self.register_value(self.memory[self.memory_address + 2])*self.register_value(self.memory[self.memory_address + 3])) % 32768
        self.memory_address += 4

    def mod_(self):
        self.registers[self.memory[self.memory_address + 1]] = self.register_value(self.memory[self.memory_address + 2]) % self.register_value(self.memory[self.memory_address + 3])
        self.memory_address += 4

    def and_(self):
        self.registers[self.memory[self.memory_address + 1]] = self.register_value(self.memory[self.memory_address + 2]) & self.register_value(self.memory[self.memory_address + 3])
        self.memory_address += 4

    def or_(self):
        self.registers[self.memory[self.memory_address + 1]] = self.register_value(self.memory[self.memory_address + 2]) | self.register_value(self.memory[self.memory_address + 3])
        self.memory_address += 4

    def not_(self):
        self.registers[self.memory[self.memory_address + 1]] = 32768 + ~self.register_value(self.memory[self.memory_address + 2])
        self.memory_address += 3

    def rmem_(self):
        self.registers[self.memory[self.memory_address + 1]] = self.memory[self.register_value(self.memory[self.memory_address + 2])]
        self.memory_address += 3

    def wmem_(self):
        self.memory[self.register_value(self.memory[self.memory_address + 1])] = self.register_value(self.memory[self.memory_address + 2])
        self.memory_address += 3

    def call_(self):
        self.stack.append(self.memory_address + 2)
        self.memory_address = self.register_value(self.memory[self.memory_address + 1])

    def ret_(self):
        if len(self.stack) > 0:
            self.memory_address = self.stack.pop()
        else:
            raise Break_

    def out_(self):
        print(chr(self.register_value(self.memory[self.memory_address + 1])), end='')
        self.memory_address += 2

    def in_(self):
        if self.input_start == 0:
            self.input_index = 0
            self.input_string = next(self.player_actions, None)
            if self.input_string == 'fix teleporter':
                self.registers[32775] = 25734
            if self.input_string == None:
                self.input_string = input()
            self.registers[self.memory[self.memory_address + 1]] = ord(self.input_string[self.input_index])
            self.input_start = 1
        else:
            self.input_index += 1
            if self.input_index < len(self.input_string):
                self.registers[self.memory[self.memory_address + 1]] = ord(self.input_string[self.input_index])
            else:
                self.registers[self.memory[self.memory_address + 1]] = ord('\n')
                self.input_start = 0
        self.memory_address += 2

    def noop_(self):
        self.memory_address += 1

    operations = [halt_, set_, push_, pop_, eq_, gt_, jmp_, jt_, jf_, add_, mult_, mod_, and_, or_, not_, rmem_, wmem_, call_, ret_, out_, in_, noop_]
