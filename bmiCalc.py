def calcBMI(height, weight):
	heightConv = height * 0.025
	weightConv = weight * 0.45
	bmi = round(weightConv / (heightConv**2), 1)

	if bmi < 18.5:
		category = 'Underweight'
	elif bmi <= 24.9:
		category = 'Normal Weight'
	elif bmi <= 29.9:
		category = 'Overweight'
	else:
		category = 'Obese'

	return bmi, category
    
if __name__ == "__main__":
    print('Welcome to the BMI Calculator')
    height = float(input('What is your height in inches? '))
    weight = float(input('What is your weight in pounds? '))
    bmi, category = calcBMI(height, weight)
    print(f'Your current BMI is {bmi:.1f} which would be categorized as {category}.')
