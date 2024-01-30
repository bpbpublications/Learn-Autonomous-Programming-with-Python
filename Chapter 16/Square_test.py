#Perform test
from Calculate_Square import Square

def test_Square():
    intNum = 10
    intSquare = Square(intNum)
    assert intSquare == 100