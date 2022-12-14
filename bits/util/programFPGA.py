#!/usr/bin/env python3

import os
import argparse
import subprocess
import time
import fileinput


def programCDF(cdf):

    # reinicia o driver do jtagd
    # para garantir que o mesmo está
    # funcionando
    os.system("killall jtagd")
    time.sleep(1)
    os.system("jtagconfig")
    time.sleep(1)

    # verifica se o .mif existe
    cdf = os.path.abspath(cdf)

    if not os.path.isfile(cdf):
        print("Arquivo {} não encontrado".format(cdf))
        return 1

    pPGM = subprocess.Popen("quartus_pgm -c 1 -m jtag " + cdf, shell=True)
    exit_codes = pPGM.wait()


def setMifFile(mif, tclFile):
    for line in fileinput.input(tclFile, inplace=1):
        if "set MIF" in line:
            print('set MIF "{}"'.format(mif))
        else:
            print(line.rstrip())


def setJTAG(value, tclFile):
    for line in fileinput.input(tclFile, inplace=1):
        if "set JTAG" in line:
            print('set JTAG "{}"'.format(value))
        else:
            print(line.rstrip())


def getJtagPort():
    proc = subprocess.Popen("jtagconfig", stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if os.name == "posix":
        h = str(out[2:20])
        h = h[3:15] + "\\" + h[15:19] + "\\" + h[19:-1]
    else:
        h = str(out)
        h = h[5:17] + "\\" + h[17:23] + "\\]"
    print(h)
    return h


def programROM(mif):
    TCL = os.path.join(
        (os.path.dirname(os.path.abspath(__file__))), "atualizaMemoria.tcl"
    )

    # verifica se o .mif existe
    mif = os.path.abspath(mif)

    if not os.path.isfile(mif):
        print("Arquivo {} não encontrado".format(mif))
        return 1

    mif = mif.replace("\\", "/")
    setMifFile(mif, TCL)

    print(mif)
    print(TCL)

    port = getJtagPort()
    setJTAG(port, TCL)

    # os.system("quartus_stp -t "+TCL)
    proc = subprocess.Popen("quartus_stp -t " + TCL, stdout=subprocess.PIPE, shell=True)
