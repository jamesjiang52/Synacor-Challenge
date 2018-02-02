from instruction import Instruction
from break_ import Break_

if __name__ == '__main__':

    with open('C:\\Users\\James Jiang\\Documents\\Synacor Challenge\\challenge.bin', 'rb') as f:
        memory = [0 for i in range(2**15)]
        byte = f.read(2)
        i = 0
        while byte != b'':
            instruction = int.from_bytes(byte, byteorder='little')
            memory[i] = instruction
            byte = f.read(2)
            i += 1

    registers = {}
    for register in range(32768, 32776):
        registers[register] = 0

    instruction = Instruction(memory, registers)

    try:
        while instruction.memory_address < len(instruction.memory):
            if instruction.memory_address == 5489:
                instruction.registers[32768] = 6
                instruction.memory_address += 2
            exec_instruction = instruction.register_value(instruction.memory[instruction.memory_address])
            Instruction.operations[exec_instruction](instruction)
    except Break_:
        pass
