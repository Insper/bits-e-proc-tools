# -*- coding: utf-8 -*-
# Eduardo Marossi & Rafael Corsi @ insper.edu.br
# Dez/2017
# Disciplina Elementos de Sistemas

def z01_valid_assembly(line):
    line = line.strip()
    instrs = ["mov", "lea", "sub", "add", "jmp", "je", "jg", "jl", "jne", "jle", "jge", "nop", "rsub", "inc", "dec", "not", "neg", "and", "orw"]
    find = line.find(" ")
    if find == -1:
        find = len(line)

    find = min(find, 3)
    instr  = line[0:find]
    return instr in instrs or ":" in line and (not line.startswith(";"))


def bin_str_to_hex(data):
    if data.strip() == "":
        return ""
    return hex(int(data,2))


def hex_str_to_bin(data):
    if data.strip() == "":
        return ""
    x = bin(int(str(data), 16))[2:]
    return "0"*(16-len(x)%17) + x

def real_line(contents, pc):
    pc = pc - 1 ##TODO Bug
    instr_counter = 0
    line_counter = 0
    for line in contents.split('\n'):
        line = line.strip().replace('  ', ' ')
        if ':' in line or line == '' or (len(line) >= 1 and line[0] == ';'):
            line_counter += 1
            continue

        if instr_counter == pc:
            break
        else:
            instr_counter += 1
            line_counter += 1
    return line_counter

def z01_ram_name(pos):
    names = {
        0: "0 - SP / R0",
        1: "1 - LCL / R1",
        2: "2 - ARG / R2",
        3: "3 - THIS / R3",
        4: "4 - THAT / R4",
        5: "5 - R5",
        6: "6 - R6",
        7: "7 - R7",
        8: "8 - R8",
        9: "9 - R9",
        10: "10 - R10",
        11: "11 - R11",
        12: "12 - R12",
        13: "13 - R13",
        14: "14 - R14",
        15: "15 - R15"
    }

    return names.get(pos, str(pos))
