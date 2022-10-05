from setuptools import setup, find_packages

import shutil
import os
import platform

pyc_dirs = ["bits/sw/assembler", "bits/sw/vmtranslator/"]
pycache_dir = "__pycache__"


def getMajorPythonVersion():
    v = platform.python_version().split(".")
    return v[0] + v[1]


def setupPyc(dirs):
    pycVersion = getMajorPythonVersion()
    for dir in dirs:
        for f in os.listdir(os.path.join(dir, pycache_dir)):
            if f.find(pycVersion) > 0:
                baseName = f.split(".")[0] + ".pyc"
                shutil.copy(
                    os.path.join(dir, pycache_dir, f), os.path.join(dir, baseName)
                )

            print(f)


print("-------------------------------------")
setupPyc(pyc_dirs)
print("-------------------------------------")

setup(
    name="bits",
    version="1.0",
    packages=[
        "bits",
        "bits.hw",
        "bits.util",
        "bits.sw.assembler",
        "bits.sw.vmtranslator",
        "bits.sw.simulator",
    ],
    install_requires=[
        "click",
        "pyyaml",
        "pytest",
        "tabulate",
        "myhdl",
        "wheel",
        "PyQt5",
    ],
    include_package_data=True,
    data_files=[
        (
            "bits",
            [
                "bits/sw/assembler/ASMcode.pyc",
                "bits/sw/assembler/ASMparser.pyc",
                "bits/sw/assembler/ASM.pyc",
                "bits/sw/assembler/ASMsymbolTable.pyc",
                "bits/sw/assembler/ASMutil.pyc",
                "bits/sw/vmtranslator/Code.pyc",
                "bits/sw/vmtranslator/Parser.pyc",
                "bits/sw/vmtranslator/VMTranslate.pyc",
                "bits/sw/vmtranslator/VMutil.pyc",
            ],
        ),
    ],
    entry_points="""
        [console_scripts]
        bits=bits:cli
    """,
)
