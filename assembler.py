# Program Name: Assembler (part1)
# Author: Mehdi Mortazavian
# Std No: 9932114
# Creation Date: 24-02-1401
# Program Description: Get a file with assembly instruction in and then return it to machine code

from operator import index
# -------------------------- Put the file in inputFile and outputFile -----------------------------
inputFile = open("AssemblyInput.txt", "r")
outputFile = open("AssemblyOutput.txt", "w")

# --------------------------------- Function for ADD instruction ----------------------------------


def ADD(lst):

    if (lst[1] in reg_8_address or lst[2] in reg_8_address) or (lst[1] in reg_32_address or lst[2] in reg_32_address):
        result ="00"
    else:
        result = "11"

    resultToReturn = ""

    if lst[1] in reg_8 and lst[2] in reg_8:
        result += reg[reg_8.index(lst[2])]
        result += reg[reg_8.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "00" + " " + result[2:]

    elif lst[1] in reg_16 and lst[2] in reg_16:
        result += reg[reg_16.index(lst[2])]
        result += reg[reg_16.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "66" + " " + "01" + " " + result[2:]

    elif lst[1] in reg_32 and lst[2] in reg_32:
        result += reg[reg_32.index(lst[2])]
        result += reg[reg_32.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "01" + " " + result[2:]

    elif lst[1] in reg_8_address and lst[2] in reg_8:
        result += reg[reg_8.index(lst[2])]
        result += reg[reg_8_address.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "00" + " " + result[2:]

    elif lst[1] in reg_8 and lst[2] in reg_8_address:
        result += reg[reg_8.index(lst[1])]
        result += reg[reg_8_address.index(lst[2])]
        result = (hex(int(result, 2)))
        resultToReturn = "02" + " " + result[2:]

    elif lst[1] in reg_32_address and lst[2] in reg_32:
        result += reg[reg_32.index(lst[2])]
        result += reg[reg_32_address.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "01" + " " + result[2:]

    elif lst[1] in reg_32 and lst[2] in reg_32_address:
        result += reg[reg_32.index(lst[1])]
        result += reg[reg_32_address.index(lst[2])]
        result = (hex(int(result, 2)))
        resultToReturn = "03" + " " + result[2:]

    return resultToReturn
# --------------------------------- Function for SUB instruction ----------------------------------


def SUB(lst):


    if (lst[1] in reg_8_address or lst[2] in reg_8_address) or (lst[1] in reg_32_address or lst[2] in reg_32_address):
        result ="00"
    else:
        result = "11"

    resultToReturn = ""

    if (lst[1] in reg_8 and lst[2] in reg_8):
        result += reg[reg_8.index(lst[2])]
        result += reg[reg_8.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "28" + " " + result[2:]

    elif lst[1] in reg_16 and lst[2] in reg_16:
        result += reg[reg_16.index(lst[2])]
        result += reg[reg_16.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "66" + " " + "29" + " " + result[2:]

    elif lst[1] in reg_32 and lst[2] in reg_32:
        result += reg[reg_32.index(lst[2])]
        result += reg[reg_32.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "29" + " " + result[2:]
    
    elif (lst[1] in reg_8 and lst[2] in reg_8_address):
        result += reg[reg_8.index(lst[1])]
        result += reg[reg_8_address.index(lst[2])]
        result = (hex(int(result, 2)))
        resultToReturn = "2a" + " " + result[2:]
    
    elif (lst[1] in reg_8_address and lst[2] in reg_8):
        result += reg[reg_8.index(lst[2])]
        result += reg[reg_8_address.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "28" + " " + result[2:]

    elif lst[1] in reg_32_address and lst[2] in reg_32:
        result += reg[reg_32.index(lst[2])]
        result += reg[reg_32_address.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "29" + " " + result[2:]

    elif lst[1] in reg_32 and lst[2] in reg_32_address:
        result += reg[reg_32.index(lst[1])]
        result += reg[reg_32_address.index(lst[2])]
        result = (hex(int(result, 2)))
        resultToReturn = "2b" + " " + result[2:]

    return resultToReturn

# --------------------------------- Function for AND instruction ----------------------------------


def AND(lst):

    if (lst[1] in reg_8_address or lst[2] in reg_8_address) or (lst[1] in reg_32_address or lst[2] in reg_32_address):
        result ="00"
    else:
        result = "11"

    resultToReturn = ""

    if lst[1] in reg_8 and lst[2] in reg_8:
        result += reg[reg_8.index(lst[2])]
        result += reg[reg_8.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "20" + " " + result[2:]

    elif lst[1] in reg_16 and lst[2] in reg_16:
        result += reg[reg_16.index(lst[2])]
        result += reg[reg_16.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "66" + " " + "21" + " " + result[2:]

    elif lst[1] in reg_32 and lst[2] in reg_32:
        result += reg[reg_32.index(lst[2])]
        result += reg[reg_32.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "21" + " " + result[2:]

    elif lst[1] in reg_8_address and lst[2] in reg_8:
        result += reg[reg_8.index(lst[2])]
        result += reg[reg_8_address.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "28" + " " + result[2:]

    elif lst[1] in reg_8 and lst[2] in reg_8_address:
        result += reg[reg_8.index(lst[1])]
        result += reg[reg_8_address.index(lst[2])]
        result = (hex(int(result, 2)))
        resultToReturn = "2a" + " " + result[2:]

    elif lst[1] in reg_32_address and lst[2] in reg_32:
        result += reg[reg_32.index(lst[2])]
        result += reg[reg_32_address.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "29" + " " + result[2:]

    elif lst[1] in reg_32 and lst[2] in reg_32_address:
        result += reg[reg_32.index(lst[1])]
        result += reg[reg_32_address.index(lst[2])]
        result = (hex(int(result, 2)))
        resultToReturn = "2b" + " " + result[2:]

    return resultToReturn

# --------------------------------- Function for Or instruction -----------------------------------


def OR(lst):

    if (lst[1] in reg_8_address or lst[2] in reg_8_address) or (lst[1] in reg_32_address or lst[2] in reg_32_address):
        result ="00"
    else:
        result = "11"

    resultToReturn = ""

    if lst[1] in reg_8 and lst[2] in reg_8:
        result += reg[reg_8.index(lst[2])]
        result += reg[reg_8.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "08" + " " + result[2:]

    elif lst[1] in reg_16 and lst[2] in reg_16:
        result += reg[reg_16.index(lst[2])]
        result += reg[reg_16.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "66" + " " + "09" + " " + result[2:]

    elif lst[1] in reg_32 and lst[2] in reg_32:
        result += reg[reg_32.index(lst[2])]
        result += reg[reg_32.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "09" + " " + result[2:]

    elif lst[1] in reg_8_address and lst[2] in reg_8:
        result += reg[reg_8.index(lst[2])]
        result += reg[reg_8_address.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "08" + " " + result[2:]

    elif lst[1] in reg_8 and lst[2] in reg_8_address:
        result += reg[reg_8.index(lst[1])]
        result += reg[reg_8_address.index(lst[2])]
        result = (hex(int(result, 2)))
        resultToReturn = "0a" + " " + result[2:]

    elif lst[1] in reg_32_address and lst[2] in reg_32:
        result += reg[reg_32.index(lst[2])]
        result += reg[reg_32_address.index(lst[1])]
        result = (hex(int(result, 2)))
        resultToReturn = "09" + " " + result[2:]

    elif lst[1] in reg_32 and lst[2] in reg_32_address:
        result += reg[reg_32.index(lst[1])]
        result += reg[reg_32_address.index(lst[2])]
        result = (hex(int(result, 2)))
        resultToReturn = "0b" + " " + result[2:]

    return resultToReturn

# --------------------------------Function to decide between ADD,SUB,AND,OR -----------------------


def decide(lst):

    if lst[0] == 'ADD':
        return ADD(lst)
    elif lst[0] == 'SUB':
        return SUB(lst)
    elif lst[0] == 'AND':
        return AND(lst)
    elif lst[0] == 'OR':
        return OR(lst)
    else:
        print(lst)
        return "Invalid instruction"

# --------------------------------- Function to check if instruction is valid ---------------------
# ----------- Check the length of the instruction and if both registers has the same size ---------


def myValidator(lst):

    if len(lst) > 3 or len(lst) < 3:
        return "Invalid instruction"

    else:

        lst[0] = lst[0].upper()
        lst[1] = lst[1].upper()
        lst[2] = lst[2].upper()

        if ((lst[1] in reg_8) and (lst[2] in reg_8)) or ((lst[1] in reg_8_address) and (lst[2] in reg_8)) or ((lst[1] in reg_8) and (lst[2] in reg_8_address)) == True:
            return decide(lst)

        elif ((lst[1] in reg_16) and (lst[2] in reg_16)) == True:
            return decide(lst)

        elif ((lst[1] in reg_32) and (lst[2] in reg_32)) or ((lst[1] in reg_32_address) and (lst[2] in reg_32)) or ((lst[1] in reg_32) and (lst[2] in reg_32_address)) == True:
            return decide(lst)

        else:
            return "Invalid instruction"


# --------------------------------- Define the 8,16 and 32 bit registers --------------------------
reg = ["000", "001", "010", "011", "100", "101", "110", "111"]
# ------------------------------------------- 8 bit registers -------------------------------------
reg_8 = ["AL", "CL", "DL", "BL", "AH", "CH", "DH", "BH"]
# ------------------------------------------ 16 bit registers -------------------------------------
reg_16 = ["AX", "CX", "DX", "BX", "SP", "BP", "SI", "DI"]
# ------------------------------------------ 32 bit registers -------------------------------------
reg_32 = ["EAX", "ECX", "EDX", "EBX", "ESP", "EBP", "ESI", "EDI"]

# --------------------------------- Define the 8,16 and 32 bit registers Address-------------------
reg = ["000", "001", "010", "011", "100", "101", "110", "111"]
# ------------------------------------------- 8 bit registers -------------------------------------
reg_8_address = ["[AL]", "[CL]", "[DL]", "[BL]", "[AH]", "[CH]", "[DH]", "[BH]"]
# ------------------------------------------ 32 bit registers -------------------------------------
reg_32_address = ["[EAX]", "[ECX]", "[EDX]", "[EBX]", "[ESP]", "[EBP]", "[ESI]", "[EDI]"]

# # ------------------------------------------- Read from input file ------------------------------
Lines = inputFile.readlines()

# ---------------- For loop to check all the instructions in the input file -----------------------
for line in Lines:

    line = list(line)

    for i in range(len(line)):  # To remove ',' in all of the instructions

        if line[i] == ',':
            line[i] = ""

    line = ''.join(line)

    line = line.split()

    # TEST
    print(line)

    result = myValidator(line)

    outputFile.write(result + "\n")

outputFile.close()
