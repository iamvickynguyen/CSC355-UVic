# pip3 install tabulate
from tabulate import tabulate

def calculateJK(present, next):
    if present == '0':
        if next == '0':
            return '0','x'
        return '1', 'x'
    if next == '0':
        return 'x', '1'
    return 'x', '0'

def generatetable_JK(s):
    bits = len(s[0])
    h = []
    for i in range(bits):
        h.append('Q' + str(i))
    for i in range(bits):
        h.append('Q' + str(i) + '+')
    for i in range(bits):
        h.append('J' + str(i))
        h.append('K' + str(i))

    rows = []
    for x in range(len(s)):
        present = s[x]
        next = s[0] if x == len(s) - 1 else s[x + 1]

        row = []
        for i in range(bits):
            row.append(present[i]) 
        for i in range(bits):
            row.append(next[i])
        for i in range(bits):
            j, k = calculateJK(present[i], next[i])
            row.append(j)
            row.append(k)

        rows.append(row)           

    print(tabulate(headers=h, tabular_data=rows, tablefmt="grid"))

def calculateSR(present, next):
    if present == '0':
        if next == '0':
            return '0','x'
        return '1', '0'
    if next == '0':
        return '0', '1'
    return 'x', '0'

def generatetable_SR(s):
    bits = len(s[0])
    h = []
    for i in range(bits):
        h.append('Q' + str(i))
    for i in range(bits):
        h.append('Q' + str(i) + '+')
    for i in range(bits):
        h.append('S' + str(i))
        h.append('R' + str(i))

    rows = []
    for x in range(len(s)):
        present = s[x]
        next = s[0] if x == len(s) - 1 else s[x + 1]

        row = []
        for i in range(bits):
            row.append(present[i]) 
        for i in range(bits):
            row.append(next[i])
        for i in range(bits):
            _s, r = calculateSR(present[i], next[i])
            row.append(_s)
            row.append(r)

        rows.append(row)           

    print(tabulate(headers=h, tabular_data=rows, tablefmt="grid"))

def generatetable_D(s):
    bits = len(s[0])
    h = []
    for i in range(bits):
        h.append('Q' + str(i))
    for i in range(bits):
        h.append('Q' + str(i) + '+')
    for i in range(bits):
        h.append('D' + str(i))

    rows = []
    for x in range(len(s)):
        present = s[x]
        next = s[0] if x == len(s) - 1 else s[x + 1]

        row = []
        for i in range(bits):
            row.append(present[i]) 
        for i in range(bits):
            row.append(next[i])
        for i in range(bits):
            row.append(next[i])

        rows.append(row)           

    print(tabulate(headers=h, tabular_data=rows, tablefmt="grid"))

def calculateT(present, next):
    if present == '0':
        if next == '0':
            return '0'
        return '1'
    if next == '0':
        return '1'
    return '0'

def generatetable_T(s):
    bits = len(s[0])
    h = []
    for i in range(bits):
        h.append('Q' + str(i))
    for i in range(bits):
        h.append('Q' + str(i) + '+')
    for i in range(bits):
        h.append('T' + str(i))

    rows = []
    for x in range(len(s)):
        present = s[x]
        next = s[0] if x == len(s) - 1 else s[x + 1]

        row = []
        for i in range(bits):
            row.append(present[i]) 
        for i in range(bits):
            row.append(next[i])
        for i in range(bits):
            t = calculateT(present[i], next[i])
            row.append(t)

        rows.append(row)           

    print(tabulate(headers=h, tabular_data=rows, tablefmt="grid"))

sequence = input('Enter sequence (ie 001,011,010,110,111,101,100): ')
choice = int(input('What kind of flip flop? \n1: JK\n2: SR\n3: D\n4: T\n'))
s = sequence.replace(" ", "")
s = s.split(',')

if choice == 1:
    generatetable_JK(s)
elif choice == 2:
    generatetable_SR(s)
elif choice == 3:
    generatetable_D(s)
else:
    generatetable_T(s)