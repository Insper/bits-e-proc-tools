#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test
import os.path


def text_to_ram(text, offset=0):
    ram = {}
    for i in range(len(text)):
        ram[i + offset] = ord(text[i])
    return ram


def test_add():
    ram = {0: 2, 1: 42}
    tst = {2: 44}
    assert nasm_test("add.nasm", ram, tst)

    ram = {0: 0, 1: 0}
    tst = {2: 0}
    assert nasm_test("add.nasm", ram, tst)

    ram = {0: 2, 1: 1}
    tst = {2: 3}
    assert nasm_test("add.nasm", ram, tst)


def test_sub():
    ram = {0: 2, 1: 4}
    tst = {2: 2}
    assert nasm_test("sub.nasm", ram, tst)


def test_mov():
    ram = {0: 33, 1: 44}
    tst = {0: 44, 1: 33, 3: 1}
    assert nasm_test("mov.nasm", ram, tst)


def test_abs():
    ram = {1: -1}
    tst = {0: 1}
    assert nasm_test("abs.nasm", ram, tst)

    ram = {1: 35}
    tst = {0: 35}
    assert nasm_test("abs.nasm", ram, tst)


def test_max():
    ram = {0: 35, 1: 7}
    tst = {2: 35}
    assert nasm_test("max.nasm", ram, tst)

    ram = {0: 7, 1: 63}
    tst = {2: 63}
    assert nasm_test("max.nasm", ram, tst)


def test_mult():
    ram = {0: 2, 1: 2}
    tst = {3: 4}
    assert nasm_test("mult.nasm", ram, tst)

    ram = {0: 32, 1: 16}
    tst = {3: 512}
    assert nasm_test("mult.nasm", ram, tst, 10000)


def test_mod():
    ram = {0: 0, 1: 0}
    tst = {2: 0}
    assert nasm_test("mod.nasm", ram, tst)

    ram = {0: 0, 1: 5}
    tst = {2: 0}
    assert nasm_test("mod.nasm", ram, tst)

    ram = {0: 32, 1: 5}
    tst = {2: 2}
    assert nasm_test("mod.nasm", ram, tst, 10000)

    ram = {0: 1023, 1: 7}
    tst = {2: 1}
    assert nasm_test("mod.nasm", ram, tst, 10000)


def test_div():
    ram = {0: 0, 1: 5}
    tst = {2: 0}
    assert nasm_test("div.nasm", ram, tst)

    ram = {0: 4, 1: 2}
    tst = {2: 2}
    assert nasm_test("div.nasm", ram, tst)

    ram = {0: 30, 1: 5}
    tst = {2: 6}
    assert nasm_test("div.nasm", ram, tst, 10000)

    ram = {0: 46, 1: 5}
    tst = {2: 9}
    assert nasm_test("div.nasm", ram, tst, 10000)

    ram = {0: 1023, 1: 7}
    tst = {2: 146}
    assert nasm_test("div.nasm", ram, tst, 10000)


def test_isEven():
    ram = {0: 2, 5: 64}
    tst = {0: 1}
    assert nasm_test("isEven.nasm", ram, tst)

    ram = {0: 2, 5: 1023}
    tst = {0: 0}
    assert nasm_test("isEven.nasm", ram, tst)


def test_pow():
    ram = {0: 2, 1: 0}
    tst = {0: 0}
    assert nasm_test("pow.nasm", ram, tst)

    ram = {1: 2}
    tst = {0: 4}
    assert nasm_test("pow.nasm", ram, tst)

    ram = {1: 16}
    tst = {0: 256}
    assert nasm_test("pow.nasm", ram, tst, 10000)


def test_stringLenght():
    ram = {}
    text = "oi tudo bem?"
    ram = text_to_ram(text, 8)
    tst = {0: len(text)}
    assert nasm_test("stringLength.nasm", ram, tst, 10000)

    text = "o saci eh um ser muito especial"
    ram = text_to_ram(text, 8)
    tst = {0: len(text)}
    assert nasm_test("stringLength.nasm", ram, tst, 10000)


def test_palindromo():
    ram = text_to_ram("ararr", 10)
    ram[0] = 2
    tst = {0: 0}
    assert nasm_test("palindromo.nasm", ram, tst, 10000)

    ram = text_to_ram("arara", 10)
    ram[0] = 2
    tst = {0: 1}
    print(ram)
    assert nasm_test("palindromo.nasm", ram, tst, 10000)
