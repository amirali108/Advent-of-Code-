from  day_02_part_02 import find_output , read_file
import pytest


numbers=read_file("input_02")


def test_find_01():
    global numbers
    assert find_output(1330713 , numbers)==102

def test_find_02():
    global numbers
    assert find_output(1546712 , numbers)==201


def test_find_03():
    global numbers
    assert find_output(1546723 , numbers)==212


def test_find_04():
    global numbers
    assert find_output(3706713 , numbers)==1202


def test_find_05():
    global numbers
    assert find_output(4138725 , numbers)==1414
















if __name__=="__main__":
    pytest.main(["-vv"])