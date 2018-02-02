def register(string_value):
    if int(string_value) in range(32768, 32776):
        return('r' + str(int(string_value) - 32768))
    else:
        return(string_value)

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

    with open('C:\\Users\\James Jiang\\Documents\\Synacor Challenge\\disassembled.txt', 'w') as disassembled:
        memory_index = 0
        while memory_index in range(len(memory)):
            if memory[memory_index] == 0:
                disassembled.write(str(memory_index) + ' ' + 'halt\n')
                memory_index += 1
            elif memory[memory_index] == 1:
                disassembled.write(str(memory_index) + ' ' + 'set ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + '\n')
                memory_index += 3
            elif memory[memory_index] == 2:
                disassembled.write(str(memory_index) + ' ' + 'push ' + register(str(memory[memory_index + 1])) + '\n')
                memory_index += 2
            elif memory[memory_index] == 3:
                disassembled.write(str(memory_index) + ' ' + 'pop ' + register(str(memory[memory_index + 1])) + '\n')
                memory_index += 2
            elif memory[memory_index] == 4:
                disassembled.write(str(memory_index) + ' ' + 'eq ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + ' ' + register(str(memory[memory_index + 3])) + '\n')
                memory_index += 4
            elif memory[memory_index] == 5:
                disassembled.write(str(memory_index) + ' ' + 'gt ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + ' ' + register(str(memory[memory_index + 3])) + '\n')
                memory_index += 4
            elif memory[memory_index] == 6:
                disassembled.write(str(memory_index) + ' ' + 'jmp ' + register(str(memory[memory_index + 1])) + '\n')
                memory_index += 2
            elif memory[memory_index] == 7:
                disassembled.write(str(memory_index) + ' ' + 'jt ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + '\n')
                memory_index += 3
            elif memory[memory_index] == 8:
                disassembled.write(str(memory_index) + ' ' + 'jf ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + '\n')
                memory_index += 3
            elif memory[memory_index] == 9:
                disassembled.write(str(memory_index) + ' ' + 'add ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + ' ' + register(str(memory[memory_index + 3])) + '\n')
                memory_index += 4
            elif memory[memory_index] == 10:
                disassembled.write(str(memory_index) + ' ' + 'mult ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + ' ' + register(str(memory[memory_index + 3])) + '\n')
                memory_index += 4
            elif memory[memory_index] == 11:
                disassembled.write(str(memory_index) + ' ' + 'mod ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + ' ' + register(str(memory[memory_index + 3])) + '\n')
                memory_index += 4
            elif memory[memory_index] == 12:
                disassembled.write(str(memory_index) + ' ' + 'and ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + ' ' + register(str(memory[memory_index + 3])) + '\n')
                memory_index += 4
            elif memory[memory_index] == 13:
                disassembled.write(str(memory_index) + ' ' + 'or ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + ' ' + register(str(memory[memory_index + 3])) + '\n')
                memory_index += 4
            elif memory[memory_index] == 14:
                disassembled.write(str(memory_index) + ' ' + 'not ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + '\n')
                memory_index += 3
            elif memory[memory_index] == 15:
                disassembled.write(str(memory_index) + ' ' + 'rmem ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + '\n')
                memory_index += 3
            elif memory[memory_index] == 16:
                disassembled.write(str(memory_index) + ' ' + 'wmem ' + register(str(memory[memory_index + 1])) + ' ' + register(str(memory[memory_index + 2])) + '\n')
                memory_index += 3
            elif memory[memory_index] == 17:
                disassembled.write(str(memory_index) + ' ' + 'call ' + register(str(memory[memory_index + 1])) + '\n')
                memory_index += 2
            elif memory[memory_index] == 18:
                disassembled.write(str(memory_index) + ' ' + 'ret\n')
                memory_index += 1
            elif memory[memory_index] == 19:
                disassembled.write(str(memory_index) + ' ' + 'out ' + register(str(memory[memory_index + 1])) + '\n')
                memory_index += 2
            elif memory[memory_index] == 20:
                disassembled.write(str(memory_index) + ' ' + 'in ' + register(str(memory[memory_index + 1])) + '\n')
                memory_index += 2
            elif memory[memory_index] == 21:
                disassembled.write(str(memory_index) + ' ' + 'noop\n')
                memory_index += 1
            else:
                memory_index += 1

