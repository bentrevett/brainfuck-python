import sys

def execute(filename):
    f = open(filename, 'r')
    evaluate(f.read())
    f.close()
    
def evaluate(code):
    code = cleanup(code)
    bracemap = buildbracemap(code)
    
    cells = [0]
    code_pointer = 0
    cell_pointer = 0
    
    while code_pointer < len(code):
        command = code[code_pointer]
        
        if command == '>':
            cell_pointer += 1
            if cell_pointer == len(cells):
                cells.append(0)
        
        if command == '<':
            cell_pointer = 0 if cell_pointer <= 0 else cell_pointer - 1
            
        if command == '+':
            cells[cell_pointer] = (cells[cell_pointer] + 1) % 255
            
        if command == '-':
            cells[cell_pointer] = (cells[cell_pointer] - 1) % 255
            
        if command == '[' and cells[cell_pointer] == 0:
            code_pointer = bracemap[code_pointer]
            
        if command == ']' and cells[cell_pointer] != 0:
            code_pointer = bracemap[code_pointer]
            
        if command == '.':
            sys.stdout.write(chr(cells[cell_pointer]))
            
        if command == ',':
            sys.stdout.write('\n')
            c = ord(input('> ')[0])
            cells[cell_pointer] = c
            
        code_pointer += 1
            
    
def cleanup(code):
    OPERATORS = ',.[]<>+-'
    return [x for x in code if x in OPERATORS]

def buildbracemap(code):
    stack = []
    bracemap = {}
    
    for position, command in enumerate(code):
        if command == '[':
            stack.append(position)
        if command == ']':
            start = stack.pop()
            bracemap[start] = position
            bracemap[position] = start
    
    return bracemap
    
def main():
    if len(sys.argv) == 2: 
        execute(sys.argv[1])
    else: 
        print("Usage: {} filename".format(sys.argv[0]))

if __name__ == "__main__": 
    main()