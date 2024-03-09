
def calculate_bmi (feet, inches, weight):
  
  weight = float(weight)
  feet = float(feet)
  inches = float(inches)
  
  kilograms = round(weight * .45, 2)
  total_inches = feet * 12 + inches

  meters = total_inches * .025
  bmi =  round(kilograms / pow(meters,2), 1)

  return bmi

def get_bmi_category (bmi):
  if bmi < 18.5:
    return "Underweight"
  elif bmi >= 18.5 and bmi < 25:
    return "Normal weight"
  elif bmi >= 25 and bmi < 30:
    return "Overweight"
  else:
    return "Obese"


error_height = "Invalid height entered... Try again!"
error_weight = "Invalid weight entered... Try again!"

while True:
  user_height = input("Enter your height in feet: ")
  if user_height.count("'") != 1:
    print(error_height)
  else:  
    feet, inches = user_height.split("'")
    if feet.isnumeric() and inches.isnumeric():
      break
    else:
      print(error_height)

while True:
  weight = input("Enter your weight in pounds: ")
  if weight.isnumeric() and weight != '0':
    break
  else:
    print(error_weight)

user_bmi = calculate_bmi(feet, inches, weight)
user_category = get_bmi_category(user_bmi)

print("You have a BMI of %.1f. You are %s." % (user_bmi,user_category))