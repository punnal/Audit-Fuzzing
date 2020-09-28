import sys
import re
from syscalls import *


flagsList = ['-a', '-s', '-p', '-sm']
flagDescriptions = ['show everything', 'show systemcalls only', 'show programs', 'show system calls with some extra information']

sourceFile = ''
outputFile = ''
flag = '-a' 

if(len(sys.argv) < 3):
    print("Minimum 2 arguments needed i.e: python dataParser.py SOURCEFILE DESTINATIONFILE")
    sys.exit()

sourceFile = sys.argv[1]
outputFile = sys.argv[2]

time = ''

if(len(sys.argv ) == 4):
    if(sys.argv[4] in flagsList):
        flag = sys.argv[4]
    else:
        print("Invalid flag used: going with defualt flag -a")
        print("List of valid flags: ")
        for i in range(len(flagsList)):
            print(flagsList[i], ": ", flagDescriptions[i])

def parse(entry):
    global time
    check = 0
    seen = 0
    call = 0
    syscall = ''
    # print(entry)
    for line in entry:
        if((not seen) and re.search('proctitle=', line)):
            seen = 1
        if((not check) and (re.search('proctitle=\"/syz-executor\"', line) or re.search(r'proctitle=\"\(null\)\"', line) or re.search('proctitle=\"./a.out\"', line) )):
            check = 1
            # syscall += 'syz-executor' + '\n'
        # elif(line != time and re.search('time->', line)):
        #     syscall += '\n' + line + '\n'
        #     time = line
        elif(re.search('type=SYSCALL', line)):
            call = 1
            a0 = re.search(r'a0=-?[0-9a-fA-F]+', line).group()[3:]
            a1 = re.search(r'a1=-?[0-9a-fA-F]+', line).group()[3:]
            a2 = re.search(r'a2=-?[0-9a-fA-F]+', line).group()[3:]
            a3 = re.search(r'a3=-?[0-9a-fA-F]+', line).group()[3:]
            name = calls[int(re.search(r'syscall=[0-9a-fA-F]+',line).group()[8:])]
            exit = re.search(r'exit=-?[0-9a-fA-F]+', line)
            if(exit):
                ret = exit.group()[5:]
            else:
                ret = 'None'
            syscall += name + '( 0x' + a0 + ', 0x' + a1 + ', 0x'+ a2 + ', 0x'+ a3 + ' )'+ ' -> ' + ret + '\n'


    # print(syscall)
    # if re.search(r'^[A-Za-z]+\(.*\)$', line):
    #     return True
    if(call and (check or not seen)):
        return syscall
    else:
        return '!!!'

def main():
    with open(sourceFile,'rb') as f,open(outputFile,'wb') as g:
        lines = f.readlines()
        entries = []
        i = 0
        entries.append([])
        for line in lines:
            line = line.decode('utf-8')
            entries[i].append(line)
            if(re.search('----', line)):
                i += 1
                entries.append([])

        # print(entries[1])
        syscalls = []
        for entry in entries:
            syscall = parse(entry)
            if syscall != '!!!':
                syscalls.append(syscall)

        length = 0
        for syscall in syscalls:
            print(syscall)
            length +=1
            g.write(syscall.encode('utf-8'))

        print(length)
        line = "Number of syscalls = " + str(len(syscalls)) 
        print(line)
        g.write(line.encode('utf-8'))

main()
