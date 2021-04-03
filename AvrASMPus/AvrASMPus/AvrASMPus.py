TRANSLATE = {
    'REG=N':'LDI %REG0%,%N0',
    'REG=REG':'MOV %REG0%,%REG1',
    'REG=@X':'LD %REG0%,%R26',
    'X=N':'LDI %R26%,%N0',
    'REG=OPN':'LDI %REG0%,%OP0%N0',
    'IFREG=NGOTOLBL':'CPI %REG0%,%N0%\n%BREQ %LBL',
    'IFREG!=NGOTOLBL':'CPI %REG0%,%N0%\n%BRNE %LBL',
    'DDRBBIT=N':'SBI %DDRB%,%N0',
    'PORTBBIT=N':'SBI %PORTB%,%N0',
    'REG++': 'INC %REG0',
    'REG+=REG': 'ADD %REG0%,%REG1',
    'REG--':'DEC %REG0',
    'GOTOLBL':'RJMP %LBL'
    }

SYMBOLS = {
    'R0':'REG', 'R1':'REG', 'R2':'REG','R3':'REG','R4':'REG','R5':'REG',
    'R6':'REG', 'R7':'REG', 'R8':'REG','R9':'REG','R10':'REG','R11':'REG',
    'R12':'REG', 'R13':'REG', 'R14':'REG','R15':'REG','R16':'REG','R17':'REG',
    'R18':'REG', 'R19':'REG', 'R20':'REG','R21':'REG','R22':'REG','R23':'REG',
    'R24':'REG', 'R25':'REG', 'R26':'REG','R27':'REG','R28':'REG','R29':'REG',
    'R30':'REG', 'R31':'REG', 
    '~':'OP','!':'OP','<<':'OP','>>':'OP',
    }


REG = []
NUM=[]
OP=[]
LBL=[]

def addToStack(word, symbol):
    global NUM,REG,OP

    if symbol == "N":
        NUM.append(word)
    elif symbol == "REG":
        REG.append(word)
    elif symbol == "OP":
        OP.append(word)
    elif symbol == 'LBL':
        LBL.append(word)


# translate it into intermediate language for symbol lookup
def getInstruction(line):
    
    ## if line starts with _a, it is a asm directive. return the line
    if line == '':
        return line
    if line[:2] == '_a':
        return line[3:]
    if (line[1]) in [':','.',';']:
        return line

    global REG,NUM,OP,LBL
    REG,NUM,OP,LBL = [],[],[],[]

    inst=""
    global OPERANDS

    ## split line by ' ' and check each symbol in the symbol dictionary
    for w in line.split(' '):
        if w[0] == ';': # skip if it is a comment
            return inst
        symbol = SYMBOLS.get(w)
        if symbol is None:
            if w.isnumeric(): ## symbol not in dictionary. is it just a number?
                symbol = "N"
            elif w[:3] == 'LBL': ## symbol not in dict, is word a label?
                symbol = 'LBL'
            else:
                symbol = w  ## not a number either. just add it as is
        inst += symbol
        addToStack(w, symbol)
    return inst

## translate it to assembly
def translate(line, original):
    tran = TRANSLATE.get(line)
    if tran is None:
        return line
    x = ''
    for t in tran.split('%'):
        if t[0] == 'N':
            t = NUM[int(t[1])]
        elif t[:3] == 'REG':
            t = REG[int(t[3])]
        elif t[:2] == 'OP':
            t = OP[int(t[2])]
        elif t[:3] == 'LBL':
            t = LBL[0]
        x += t
    return x + " \t\t; " + original

LINE = """R6 = R5 ; my comment too
R0 = ~ 123
R0 = @X
X = 256
R16 = ~ 128
DDRB BIT = 1
PORTB BIT = 1
:LBL_loop:
IF R16 = 128 GOTO LBL_loop
R16 ++
R16 += R15
:LBL_loop2:
GOTO LBL_loop2
_a MOV R16,R17
R0 = 255
:LBL_FOR:
R0 --
IF R0 != 0 GOTO LBL_FOR
"""
# if R16 = 128 goto label
# if R16 < 128 goto label
# if R16 > 128 goto label
# if R16 >= 128 goto label
# if R16 <= goto label
# if R16 != 128 goto label

for l in LINE.split("\n"):

    i = getInstruction(l)
    print (translate(i, l))


