from  day_02_part_02 import find_output , read_file
from day_02_part_01 import calculate
import pytest


numbers=read_file("input_02")


def test_find_01():
    global numbers
    numbers_calculate=numbers.copy()
    numbers_calculate[1]=1
    numbers_calculate[2]=2
    result=calculate(numbers_calculate)

    
    assert find_output(result[0] , numbers)==102

def test_find_02():
    global numbers
    numbers_calculate=numbers.copy()
    numbers_calculate[1]=2
    numbers_calculate[2]=1
    result=calculate(numbers_calculate)

    assert find_output(result[0] , numbers)==201


def test_find_03():
    global numbers
    numbers_calculate=numbers.copy()
    numbers_calculate[1]=2
    numbers_calculate[2]=12
    result=calculate(numbers_calculate)
    assert find_output(result[0] , numbers)==212


def test_find_04():
    global numbers
    numbers_calculate=numbers.copy()
    numbers_calculate[1]=12
    numbers_calculate[2]=2
    result=calculate(numbers_calculate)
    assert find_output(result[0] , numbers)==1202


def test_find_05():
    global numbers
    numbers_calculate=numbers.copy()
    numbers_calculate[1]=14
    numbers_calculate[2]=14
    result=calculate(numbers_calculate)
    assert find_output(result[0] , numbers)==1414
















if __name__=="__main__":
    pytest.main(["-vv"])
