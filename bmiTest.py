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
