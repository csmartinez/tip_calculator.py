# Python Tip Calculator - Carli Martinez
meal_price = input("How much was your total, rounded to the nearest dollar?\n")
level_of_service = input("Was your service Good, Bad or Excellent?\n")
tip=0

meal_price = int(meal_price)

if level_of_service == "Good":
    tip = meal_price * .20
elif level_of_service == "Bad":
    percentage = input("Sorry about your bad service. Would you like to tip 15% or 20%?\n")
    if percentage == "15%" or "15":
        tip = meal_price * .15
    elif percentage == "20%" or "20":
        tip = meal_price * .20
    else:
        tip = "--- Sorry, please enter 15% or 20% for bad service tip"
elif level_of_service == "Excellent":
            tip = meal_price * .25
else:
    tip = " --- Sorry, please enter Good, Bad, or Excellent for level of service."

tip = str(tip)
print("\nTip your server $" + tip)
