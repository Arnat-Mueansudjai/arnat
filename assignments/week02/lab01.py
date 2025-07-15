"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""
print("||===========BMI_Calculator=========||")
w=float(input("Enter your weight(Kg.) : "))
h=float(input("Enter your height(M.) : "))
BMI= w/(h**2)
if BMI>30 :
    print(f"Your Bmi is : {BMI:.1f} you type is Obese")
elif BMI>=25 :
    print(f"Your Bmi is : {BMI:.1f} you type is Over weight")
elif BMI>=18.5 :
    print(f"Your Bmi is : {BMI:.1f} you type is Normal weight")
else :
    print(f"Your Bmi is : {BMI:.1f} you type is Under weight")
