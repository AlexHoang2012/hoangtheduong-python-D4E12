print("BMI calculation")
h = int(input("Please input your height (cm): "))
w = int(input("Please input your weight (kg): "))
BMI= w/(h*h/10000)

print("Your BMI is: ",BMI)
if(BMI<16):
    print("Severely underweight")
elif(BMI<18.5):
    print("underweight")
elif(BMI<25):
    print("Normal")
elif(BMI<30):
    print("Overweight")
else:
    print("Obese")
