TRANSLATE = {
    'REG=N':'LDI %REG0%,%N0',
    'REG=REG':'MOV %REG0%,%REG1',
    'DDRB=N':'SBI %DDRB%,%N0',
    'REG=@X':'LD %REG0%,%R26',
    'X=N':'LDI %R26%,%N0',
    'REG=OPN':'LDI %REG0%,%OP0%N0',
    'IFREG=NGOTOLBL':'FK',
    'PORTBOUTN':'SBI %DDRB%,%N0',
    'PORTBONN':'SBI %PORTB%,%N0',
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

def getInstruction(line):
    global REG,NUM,OP,LBL
    REG,NUM,OP,LBL = [],[],[],[]

    inst=""
    global OPERANDS

    for w in line.split(' '):
        symbol = SYMBOLS.get(w)
        if symbol is None:
            if w.isnumeric():
                symbol = "N"
            else:
                symbol = w
        inst += symbol
        addToStack(w, symbol)
    return inst

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
            t = LBL[int(t[3])]
        x += t
    return x + " ## " + original

LINE = """R6 = R5
R0 = ~ 123
R0 = @X
X = 256
R16 = ~ 128
PORTB OUT 1
PORTB ON 1
if R16 = 128 goto LBL_Start
"""
# if R16 = 128 goto label
# if R16 < 128 goto label
# if R16 > 128 goto label
# if R16 >= 128 goto label
# if R16 <= goto label
# if R16 != 128 goto label

for l in LINE.split("\n"):

    i = getInstruction(l)
    print ("translate")
    print (translate(i, l))


