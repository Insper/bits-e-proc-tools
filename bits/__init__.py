#!/usr/bin/env python3

import click
import yaml
from myhdl import *
import sys
import os.path
import shutil
from .hw.hw_util import *
from .hw.test_z01 import test_z01
from .sw.assembler.ASM import ASM
from .sw.vmtranslator.VMTranslate import VMTranslate
from .sw.vmtranslator.Code import Code as VMCode
from .util.toMIF import toMIF
from .util.programFPGA import programCDF, programROM
from .util.genImg import memTopgm
from .util.debuglst import debugLst
from .util.debugStack import debugStack


def getName(nasm):
    return nasm.split(".")[0]


def clearDir(d):
    shutil.rmtree(os.path.dirname(d))


def createDir(d):
    dir = os.path.dirname(d)
    if os.path.exists(dir) is False:
        os.makedirs(dir)


def vm_to_nasm(vm, nasm):
    createDir(nasm)
    fNasm = open(nasm, "w")
    v = VMTranslate(vm, fNasm)
    v.run()


def vm_test(vm, ram, test, time=100000):
    nasm = os.path.join("nasm", vm + ".nasm")
    vm_to_nasm(vm, nasm)
    return nasm_test(nasm, ram, test, time)


def nasm_test(nasm, ram, test, time=1000):
    name = getName(nasm)
    hack = name + ".hack"
    path_atual = os.getcwd()
    if path_atual[-8:] == '/sw/nasm':
        nasm_to_hack(nasm, hack)
    else:
        nasm_to_hack(f'sw/nasm/{nasm}', hack)
    rom = rom_init_from_hack(hack)

    run = proc_run(name, rom, ram, time)

    return True if ram_test(test, run["ram"]) == 0 else False


def nasm_to_hack(nasm, hack, mif=False):
    print(" 1/1 gerando novos arquivos .hack")
    print(" destine: {}".format(hack))

    fNasm = open(nasm, "r")
    fHack = open(hack, "w")
    asm = ASM(fNasm, fHack)
    asm.run()
    fHack.close()

    if mif:
        toMIF(hack, getName(hack) + ".mif")


def proc_run(name, rom, ram, time, dump=True, img=True):
    if dump:
        mem_dump_file(ram, name + "_ram_init.txt")
    cpu = test_z01(name, rom, ram, time)
    run = cpu.run()
    if dump:
        cpu.dump()

    if img:
        memTopgm(ram, name)

    return run


# ------------------------- #


@click.group()
@click.option("--debug", "-b", is_flag=True, help="Enables verbose mode.")
@click.pass_context
def cli(ctx, debug):
    pass


# ------------------------- #


@click.group()
def debug():
    pass


@debug.command()
@click.argument("name")
def nasm(name):
    debugLst(name)


@debug.command()
@click.argument("lstfile")
def stack(lstfile):
    debugStack(lstfile)


# ------------------------- #


@cli.command()
@click.option("--mif", is_flag=True, help="also generates mif file")
@click.argument("nasm")
def assembly(nasm, mif):
    hack = getName(nasm) + ".hack"
    click.echo("Syncing")
    nasm_to_hack(nasm, hack, mif)


# ------------------------- #


@click.group()
def program():
    pass


@program.command()
@click.argument("cdf")
def fpga(cdf):
    if programCDF(cdf):
        print("FPGA NÃ̀O PROGRAMADA!")


@program.command()
@click.argument("fname")
def rom(fname):
    name, type = fname.split(".")

    if type == "nasm":
        nasm_to_hack(fname, name + ".hack", True)
    elif type == "hack":
        toMIF(fname, name + ".mif")
    elif type == "mif":
        pass
    else:
        print("Erro: pass an .nasm, .hack or .mif file")

    programROM(name + ".mif")


# ------------------------- #


@click.group()
def sim():
    pass


@sim.command()
@click.argument("romfile")
@click.argument("ramfile", required=False)
@click.option("--ram", is_flag=True, help="Prints ram table")
def cpu(romfile, ramfile, ram, time=1000):
    name, type = romfile.split(".")

    if type == "nasm":
        nasm_to_hack(romfile, name + ".hack", False)

    if ramfile is None:
        ram = {}
    else:
        import json

        with open(ramfile) as f:
            temp_ram = json.load(f)
            ram = {int(k): int(v) for k, v in temp_ram.items()}

    rom = rom_init_from_hack(name + ".hack")
    proc_run(name, rom, ram.copy(), time, dump=True)
    debugLst(name + ".lst", False, ram)


cli.add_command(debug)
cli.add_command(program)
cli.add_command(sim)

if __name__ == "__main__":
    cli()
