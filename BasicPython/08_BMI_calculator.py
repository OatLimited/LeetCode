weight = float(input('plz input your weight: '))
height = float(input('plz inout your height (m): '))
bmi = weight / (height)**2
if bmi < 18.5:
    result = 'Underweight'
elif bmi < 25:
    result = 'Normal'
elif bmi < 30:
    result = 'Overweight'
else:
    print('Obese')
print(f'Your BMI is {str(bmi)} and result is {result}')
