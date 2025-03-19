import pytest
from bmiCalc import calcBMI

def testUnderweight():
	assert calcBMI(68, 110) == (17.1, 'Underweight')

def testNormalWeight():
	assert calcBMI(68, 140) == (21.8, 'Normal Weight')

def testOverweight():
	assert calcBMI(68, 180) == (28.0, 'Overweight')

def testObese():
	assert calcBMI(68, 230) == (35.8, 'Obese')

def testBoundaries():
	assert calcBMI(68, 119) == (18.5, 'Normal Weight')
	assert calcBMI(68, 160) == (24.9, 'Normal Weight')
	assert calcBMI(68, 160.5) == (25.0, 'Overweight')
	assert calcBMI(68, 192) == (29.9, 'Overweight')
	assert calcBMI(68, 192.5) == (30.0, 'Obese')

def testBoundaryShift():
    assert calcBMI(68, 118) == (18.4, 'Underweight')
    assert calcBMI(68, 119) == (18.5, 'Normal Weight')