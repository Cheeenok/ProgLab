class Person:
    
  def __init__(self, weight, height):
      
    self.weight = weight
    self.height = height
    self.bmi = weight / ((height / 100) **2)

  def calcBMI(self):
    print(f"Your BMI is {self.bmi:.3f}")

  def printBMI(self):
    self.calcBMI();
    if self.bmi <= 18.5:
      print("Underweight ")
      
    elif 18.5 <= self.bmi and self.bmi <= 24.9:
      print("Normal ")
      
    elif 25 <= self.bmi and self.bmi <= 29.9:
      print("Overweight ")
      
    elif 30 <= self.bmi and self.bmi <= 34.9:
      print("Obese Class I ")
      
    elif 35 <= self.bmi and self.bmi <= 39.9:
        print("Obese Class II ")
        
    elif self.bmi >= 40:
      print("Obese Class III ")
  

if __name__ == "__main__":
  height = float(input("Enter height: "))
  weight = float(input("Enter weight: "))

  person = Person(weight, height)

  person.printBMI()