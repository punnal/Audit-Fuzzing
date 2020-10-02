import sys
import re

auditFile = ''
syzFile = ''
outputFile = ''

if(len(sys.argv) < 4):
    print("Minimum 3 arguments needed i.e: python simpleCompare.py AUDITSOURCEFILE SYZKALLERSOURCEFILE DESTINATIONFILE")
    sys.exit()

auditFile = sys.argv[1]
syzFile = sys.argv[2]
outputFile = sys.argv[3]


def findInList(val, lst):
    for i in range(len(lst)):
        if(val == lst[len(lst)-i-1][0]):
            del lst[len(lst)-i-1]
            return True
    return False

def main():
    with open(auditFile,'rb') as f,open(syzFile,'rb') as g:
        auditLines = f.readlines()
        syzLines = g.readlines()
        extraCalls = []
        i = 0
        j = 0
        auditLine = ''
        while(j < len(syzLines)-1):
            # print(j, " ", i, auditLine)
            if(i < len(auditLines)-1):
                call = re.search(r'([A-Za-z$_0-9]+\(.*\))', auditLines[i].decode('utf-8')).group()
                auditLine = re.split(r'\$|\(|\)', call)
                call = re.search(r'([A-Za-z$_0-9]+\(.*\))', syzLines[j].decode('utf-8')).group()
                syzLine = re.split(r'\$|\(|\)', call)
                
                if(auditLine[0] == syzLine[0]):
                    j = j+1
                    i = i+1
                elif(findInList(auditLine[0], extraCalls)):
                    i = i+1
                else:
                    extraCalls.append((syzLine[0], (i, j)))   
                    # print(extraCalls)
                    j = j+1
            else:
                call = re.search(r'([A-Za-z$_0-9]+\(.*\))', syzLines[j].decode('utf-8')).group()
                syzLine = re.split(r'\$|\(|\)', call)
                extraCalls.append((syzLine[0], (i, j)))   
                j = j+1

    with open(outputFile, 'wb') as h:
        output = 'Lost Calls = ' + str(len(extraCalls)) + ' \n\n'
        for call in extraCalls:
            output = output + 'SystemCall: ' + str(call[0]) + '\n'
            output = output + 'Syzkaller call number: ' + str(call[1][1]) + '\n'
            output = output + 'Auditd call number: ' + str(call[1][0]) + '\n'
            output = output + '\n'
        h.write(output.encode('utf-8'))

    


main()
