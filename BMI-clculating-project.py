#A simple BMI calculating project built on python

print("A simple BMI calculating app..")
height = float(input("Enter your hight in inch:- "))
weight = float(input("enter your weight:- "))

def BMI (height, weight):
    bmi = weight / (height**2) * 703
    if (bmi < 16):
        return "Severely underwight", bmi
    elif (bmi >= 16 and bmi < 18.5):
        return "Underwight", bmi
    elif (bmi >= 18.5 and bmi < 25):
        return "Healthy", bmi
    elif (bmi >= 25 and bmi < 30):
        return "Overeight", bmi
    elif (bmi >= 30):
        return "Obese", bmi

messag, bmi = BMI(height, weight)

print(f"Your are {messag}, and your BMI is :- {bmi}")

