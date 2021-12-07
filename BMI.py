def calc(*args):
    return args[0] / ((args[1]) / 100) **2

if __name__ == "__main__":
    height = int(input("Enter height: "))
    weight = int(input("Enter weight: "))
    bmi = calc(weight, height)
    
    print ("BMI is: ", bmi)
    
    if bmi <= 18.5:
        print("Underweight")
        
    elif bmi <= 24.9:
        print("Healthy")
        
    elif bmi <= 29.9:
        print("Overweight")
        
    elif bmi <= 34.9:
        print ("Obesity class I")
        
    elif bmi <= 39.9:
        print ("Obesity class II")
    
    else:
        print ('Obesity class III')
    
    