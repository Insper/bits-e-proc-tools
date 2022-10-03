#!/usr/bin/env python3

from bits import nasm_test, vm_test
import os.path


def test_simpleLt():
    vm_test("SimpleLt")


def test_simpleEq():
    vm_test("SimpleEq")


def test_simpleAdd():
    vm_test("SimpleAdd")


def test_simpleSub():
    vm_test("SimpleSub")


def test_simpleAnd():
    vm_test("SimpleAnd")


def test_simpleNeg():
    vm_test("SimpleNeg")


def test_simpleOr():
    vm_test("SimpleOr")


def test_simplePopTemp():
    vm_test("SimplePopTemp")


def test_simplePopLocal():
    vm_test("SimplePopLocal")


def test_simplePopPointer():
    vm_test("SimplePopPointer")


def test_simplePopThat():
    vm_test("SimplePopThat")


def test_simplePopThis():
    vm_test("SimplePopThis")


def test_simplePushArg():
    vm_test("SimplePushArg")


def test_simplePushConst():
    vm_test("SimplePushConst")


def test_simplePushLocal():
    vm_test("SimplePushLocal")


def test_simplePushTemp():
    vm_test("SimplePushTemp")


def test_simplePushThat():
    vm_test("SimplePushThat")


def test_simplePushThis():
    vm_test("SimplePushThis")


def test_simplePushAdd():
    vm_test("SimplePushAdd")


# def test_basicTest():
#    vm_test("BasicTest")


# def test_staticTest():
#    vm_test("StaticTest")

# def test_stackTest():
#    vm_test("StackTest")

# def test_basicLoop():
#    vm_test("BasicLoop", time=150000)

# def test_simpleFuncion():
#    vm_test("SimpleFunction", time=150000)

# def test_mult():
#    vm_test("test_mult", time=150000)
