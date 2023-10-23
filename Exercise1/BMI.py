def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi=float(weight)/pow(float(height),2)
    print("BMI = " + str(bmi))
    print("Weight Classification:")
    if bmi < 18.5:
        print("Under Weight")
    elif bmi >= 18.5 and bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")

calculate_bmi(weight=57, height=1.73)