import sys
import re

sourceFile = ''
outputFile = ''

if(len(sys.argv) < 3):
    print("Minimum 2 arguments needed i.e: python dataParser.py SOURCEFILE DESTINATIONFILE")
    sys.exit()

sourceFile = sys.argv[1]
outputFile = sys.argv[2]

total = 0

def filterLine(line):
    if re.search(r'#zzzzz', line):
        return True
    else:
        return False

def parse(filteredLines):
    global total
    text = ''
    for line in filteredLines:
        total += 1
        call = re.search(r'([A-Za-z$_0-9]+\(.*\))', line).group()
        text += call + '\n'
    return text

def main():
    global total
    with open(sourceFile,'rb') as f,open(outputFile,'wb') as g:
        lines = f.readlines()
        filteredLines = []
        for line in lines:
            line = line.decode('utf-8')
            if(filterLine(line)):
                filteredLines.append(line)
        text = parse(filteredLines)

        g.write(text.encode('utf-8'))
        
        line = "Number of syscalls = " + str(total) 
        print(line)
        g.write(line.encode('utf-8'))

        # g.writelines(filter(filterLine, f))


main()
