from day_02_part_01 import read_file,  calculate
import pytest



def test_read_file():
    
    assert read_file("input_test_2")==[1,9,10,3,2,3,11,0,99,30,40,50]


def test_calculate_01():
    result=calculate([1,0,0,0,99])
    assert result[0]==2


def test_claculate_02():
    result=calculate([2,3,0,3, 99])
    assert result[3]==6


def test_calculate_03():
    result=calculate([2 , 4 , 4 , 5, 99 , 0])
    assert result[5]==9801


def test_calculte_04():
    result=calculate([1,1,1,4,99,5,6,0,99])
    assert result[0]==30 and result[4]==2


def test_claculate_05():
    numbers=read_file("input_test_2")
    result=calculate(numbers)
    assert result[0]==3500 and result[3]==70


if __name__=="__main__":
    pytest.main(['-vv'])
